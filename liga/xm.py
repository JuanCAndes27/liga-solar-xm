"""Descarga de datos de XM con la librería oficial pydataxm.

Repositorio oficial de XM: https://github.com/EquipoAnaliticaXM/API_XM
Instalación:              pip install pydataxm

Uso básico de la librería (lo mismo que se ve en clase):
    from pydataxm.pydataxm import ReadDB
    api = ReadDB()                                   # descarga el inventario de métricas
    api.get_collections()                            # qué métricas existen (MetricId, Entity, Type…)
    api.request_data("Gene", "Recurso", fecha_ini, fecha_fin)          # generación horaria por planta
    api.request_data("ListadoRecursos", "Sistema", fecha_ini, fecha_fin)  # catálogo de plantas

pydataxm parte la consulta por meses y hace las peticiones en paralelo (asyncio).
"""
from __future__ import annotations

import datetime as dt
import time
from functools import lru_cache

import pandas as pd
import requests
from pydataxm.pydataxm import ReadDB

# pydataxm llama a requests SIN timeout: si el servidor de XM no contesta, la conexión se queda
# colgada varios minutos. Ponemos un timeout por defecto (20 s para conectar, 120 s para leer).
_request_original = requests.Session.request


def _request_con_timeout(self, method, url, **kw):
    if kw.get("timeout") is None:
        kw["timeout"] = (20, 120)
    return _request_original(self, method, url, **kw)


requests.Session.request = _request_con_timeout


def _con_reintentos(f, intentos=4, espera=20):
    """XM a veces no responde (mantenimiento o bloqueo temporal): reintentamos con espera creciente."""
    for i in range(1, intentos + 1):
        try:
            return f()
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
            print(f"  XM no responde (intento {i}/{intentos}): {type(e).__name__}")
            if i == intentos:
                raise
            time.sleep(espera * i)

HORAS = [f"Hour{h:02d}" for h in range(1, 25)]


@lru_cache(maxsize=1)
def api() -> ReadDB:
    return ReadDB()   # los reintentos se hacen en cada consulta (abajo)


def _col(df: pd.DataFrame, sufijo: str) -> str:
    """Busca una columna sin importar mayúsculas: 'code' → 'Values_code' o 'Values_Code'."""
    for c in df.columns:
        if c.lower().endswith(sufijo.lower()):
            return c
    raise KeyError(f"No encontré la columna '*{sufijo}' en {list(df.columns)}")


def recursos_solares() -> list[str]:
    """Códigos de las plantas cuya fuente de energía es radiación solar (Values_EnerSource = 'RAD SOLAR')."""
    hoy = dt.date.today()
    df = _con_reintentos(lambda: api().request_data("ListadoRecursos", "Sistema", hoy - dt.timedelta(days=1), hoy))
    try:
        es_solar = df[_col(df, "EnerSource")].astype(str).str.upper().str.contains("SOLAR")
    except KeyError:  # respaldo: buscar 'SOLAR' en cualquier columna de texto
        es_solar = df.astype(str).apply(lambda c: c.str.upper().str.contains("SOLAR")).any(axis=1)
    codigos = sorted(df.loc[es_solar, _col(df, "Code")].astype(str).str.upper().unique())
    print(f"  XM: {len(codigos)} recursos solares encontrados")
    if not codigos:
        raise RuntimeError(f"No se encontraron plantas solares. Columnas: {list(df.columns)}")
    return codigos


def generacion_por_recurso(inicio: dt.date, fin: dt.date) -> pd.DataFrame:
    """Generación horaria real (kWh) por planta, en formato largo: fecha_hora, codigo, kwh."""
    df = _con_reintentos(lambda: api().request_data("Gene", "Recurso", inicio, fin))
    if df is None or df.empty:
        return pd.DataFrame(columns=["fecha_hora", "codigo", "kwh"])
    col_codigo = _col(df, "code")
    cols_h = [c for c in df.columns if c.split("_")[-1] in HORAS]
    largo = df.melt(id_vars=["Date", col_codigo], value_vars=cols_h, var_name="h", value_name="kwh")
    largo["hora"] = largo["h"].str[-2:].astype(int) - 1          # Hour01 = 00:00–01:00
    largo["fecha_hora"] = pd.to_datetime(largo["Date"]) + pd.to_timedelta(largo["hora"], unit="h")
    largo["kwh"] = pd.to_numeric(largo["kwh"], errors="coerce")
    largo["codigo"] = largo[col_codigo].astype(str).str.upper()
    return largo[["fecha_hora", "codigo", "kwh"]]


def generacion_solar_nacional(inicio: dt.date, fin: dt.date) -> pd.DataFrame:
    """Serie horaria de generación solar total del SIN en MWh."""
    codigos = set(recursos_solares())
    gen = generacion_por_recurso(inicio, fin)
    sol = gen[gen["codigo"].isin(codigos)]
    serie = sol.groupby("fecha_hora", as_index=False)["kwh"].sum()
    serie["solar_mwh"] = serie["kwh"] / 1000.0
    return serie[["fecha_hora", "solar_mwh"]].sort_values("fecha_hora").reset_index(drop=True)
