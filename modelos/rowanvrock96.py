"""Rowan-SolarHybrid: modelo físico simple + red residual PyTorch.

Usa solamente las entradas oficiales de la Liga Solar XM; no consulta APIs.
La referencia física ajusta generación histórica por irradiancia pronosticada.
Una MLP pequeña aprende correcciones de potencia sobre esa referencia.
"""
import numpy as np
import pandas as pd
import torch
from torch import nn

NOMBRE = "Rowan-SolarHybrid"
AUTOR = "rowanvrock96"
SEMILLA = 42


class RedResidual(nn.Module):
    def __init__(self, n_entradas):
        super().__init__()
        self.red = nn.Sequential(
            nn.Linear(n_entradas, 24),
            nn.Tanh(),
            nn.Linear(24, 12),
            nn.Tanh(),
            nn.Linear(12, 1),
        )

    def forward(self, x):
        return self.red(x).squeeze(-1)


def _dias_completos(historia):
    dias = {}
    h = historia.copy()
    h["fecha_hora"] = pd.to_datetime(h["fecha_hora"])
    for fecha, grupo in h.groupby(h.fecha_hora.dt.date):
        grupo = grupo.sort_values("fecha_hora")
        if (len(grupo) == 24 and grupo.fecha_hora.dt.hour.nunique() == 24
                and grupo[["solar_mwh", "radiacion"]].notna().all().all()):
            dias[fecha] = grupo.set_index(grupo.fecha_hora.dt.hour)
    return dias


def _entradas(dias, fecha, ult_fecha, escala, clima_obj):
    """Predicción física y características, sin consultar el futuro real."""
    disponibles = [d for d in sorted(dias) if d <= ult_fecha]
    ultimos = disponibles[-7:]
    if not ultimos:
        raise ValueError("No hay historia anterior al objetivo")
    gen = np.stack([dias[d]["solar_mwh"].to_numpy(float) for d in ultimos])
    rad = np.stack([dias[d]["radiacion"].to_numpy(float) for d in ultimos])
    gen_ref = np.nanmean(gen, axis=0)
    rad_ref = np.nanmean(rad, axis=0)
    futuro = clima_obj.sort_values("fecha_hora")
    g = np.nan_to_num(futuro["radiacion"].to_numpy(float), nan=0.0)
    nube = np.nan_to_num(futuro["nubosidad"].to_numpy(float), nan=50.0)
    temp = np.nan_to_num(futuro["temperatura"].to_numpy(float), nan=25.0)
    hora = futuro.fecha_hora.dt.hour.to_numpy()
    if len(hora) != 24 or np.unique(hora).size != 24:
        raise ValueError("clima_dia debe contener 24 horas distintas")
    # Cociente acotado: evita divisiones explosivas al amanecer/atardecer.
    cociente = np.clip(g / np.maximum(rad_ref, 100.0), 0, 2.5)
    fisica = np.clip(gen_ref * cociente, 0, None)
    fisica[g < 5] = 0.0
    dia_ano = pd.Timestamp(fecha).dayofyear
    x = np.column_stack([
        fisica / escala,
        gen_ref / escala,
        np.clip(g, 0, 1400) / 1000,
        np.clip(rad_ref, 0, 1400) / 1000,
        np.clip(nube, 0, 100) / 100,
        np.clip(temp - 25, -25, 25) / 20,
        np.sin(2 * np.pi * hora / 24),
        np.cos(2 * np.pi * hora / 24),
        np.full(24, np.sin(2 * np.pi * dia_ano / 365.25)),
        np.full(24, np.cos(2 * np.pi * dia_ano / 365.25)),
    ]).astype(np.float32)
    return fisica, x, g


def predecir(historia, clima_dia):
    torch.manual_seed(SEMILLA)
    torch.set_num_threads(1)
    dias = _dias_completos(historia)
    if len(dias) < 14:
        raise ValueError("Se requieren al menos 14 días completos de historia")
    fechas = sorted(dias)
    futuro = clima_dia.copy()
    futuro["fecha_hora"] = pd.to_datetime(futuro["fecha_hora"])
    objetivo = futuro.fecha_hora.min().date()
    rezago = max((objetivo - fechas[-1]).days, 1)
    escala = max(float(np.nanpercentile(historia["solar_mwh"], 99)), 1.0)

    fis_fut, x_fut, g_fut = _entradas(
        dias, objetivo, fechas[-1], escala, futuro
    )
    xs, ys = [], []
    # El entrenamiento simula el mismo rezago de publicación que la predicción.
    for fecha in fechas:
        referencia = fecha - pd.Timedelta(days=rezago).to_pytimedelta()
        if referencia not in dias:
            continue
        target = dias[fecha].reset_index(drop=True)
        if target[["nubosidad", "temperatura"]].isna().any().any():
            continue
        fis, x, _ = _entradas(dias, fecha, referencia, escala, target)
        real = target["solar_mwh"].to_numpy(float)
        valido = np.isfinite(real)
        xs.append(x[valido])
        ys.append(((real - fis) / escala)[valido].astype(np.float32))

    if not xs:
        return np.maximum(fis_fut, 0)
    X = torch.from_numpy(np.concatenate(xs, axis=0))
    Y = torch.from_numpy(np.concatenate(ys, axis=0))
    red = RedResidual(X.shape[1])
    opt = torch.optim.AdamW(red.parameters(), lr=0.008, weight_decay=0.01)
    for _ in range(140):
        opt.zero_grad()
        estimacion = red(X)
        perdida = nn.functional.smooth_l1_loss(estimacion, Y, beta=0.1)
        perdida.backward()
        opt.step()

    red.eval()
    with torch.no_grad():
        residual = red(torch.from_numpy(x_fut)).numpy() * escala
    pred = np.clip(fis_fut + residual, 0, None)
    pred[g_fut < 5] = 0
    return pred.astype(float)
