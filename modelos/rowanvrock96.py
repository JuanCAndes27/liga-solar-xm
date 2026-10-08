"""Rowan-SolarHybrid v2: baseline físico multiventana + red residual PyTorch.

Compatible con la interfaz oficial; no requiere nuevas dependencias ni APIs.
Los datos de entrenamiento se generan simulando el rezago real de XM.
"""
import datetime as dt

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
            nn.Linear(n_entradas, 32),
            nn.SiLU(),
            nn.Linear(32, 16),
            nn.SiLU(),
            nn.Linear(16, 1),
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
                and np.array_equal(grupo.fecha_hora.dt.hour.to_numpy(), np.arange(24))
                and np.isfinite(grupo[["solar_mwh", "radiacion"]].to_numpy(float)).all()):
            dias[fecha] = grupo
    return dias


def _caracteristicas(dias, fecha, corte, escala, clima_obj):
    """Ninguna generación de fecha posterior a corte interviene en la referencia."""
    disponibles = [d for d in dias if d <= corte]
    if not disponibles:
        raise ValueError("No hay generación publicada disponible")
    historicos = [dias[d] for d in disponibles[-21:]]
    gen = np.stack([g["solar_mwh"].to_numpy(float) for g in historicos])
    rad = np.stack([g["radiacion"].to_numpy(float) for g in historicos])
    c = clima_obj.sort_values("fecha_hora")
    if len(c) != 24 or not np.array_equal(
        c.fecha_hora.dt.hour.to_numpy(), np.arange(24)
    ):
        raise ValueError("Se requieren 24 horas ordenables de 00 a 23")
    g = np.clip(np.nan_to_num(c["radiacion"].to_numpy(float), nan=0), 0, 1400)
    nube = np.clip(np.nan_to_num(c["nubosidad"].to_numpy(float), nan=50), 0, 100)
    temp = np.clip(np.nan_to_num(c["temperatura"].to_numpy(float), nan=25), 0, 50)

    # Persistencia de 7 días y referencia más estable de hasta 21 días.
    gen7 = gen[-7:].mean(axis=0)
    gen21 = gen.mean(axis=0)
    rad7 = rad[-7:].mean(axis=0)
    rad21 = rad.mean(axis=0)
    # La irradiancia horizontal media regional es imperfecta al amanecer.
    # Combinamos la proporcionalidad física con la persistencia para evitar
    # sobrecorrecciones extremas cerca de irradiancia cero.
    base7 = gen7 * np.clip(g / np.maximum(rad7, 120), 0, 2.2)
    base21 = gen21 * np.clip(g / np.maximum(rad21, 120), 0, 2.2)
    mezcla7 = 0.75 * base7 + 0.25 * gen7
    mezcla21 = 0.75 * base21 + 0.25 * gen21
    fisica = 0.65 * mezcla7 + 0.35 * mezcla21

    # Corrección térmica suave: aproximación relativa, no temperatura de celda.
    temp_ref = np.mean(
        np.stack([np.nan_to_num(x["temperatura"].to_numpy(float), nan=25)
                  for x in historicos[-7:]]), axis=0
    )
    factor_temp = np.clip(1 - 0.003 * (temp - temp_ref), 0.9, 1.1)
    fisica = np.clip(fisica * factor_temp, 0, None)
    hora = np.arange(24)
    est = 2 * np.pi * pd.Timestamp(fecha).dayofyear / 365.25
    x = np.column_stack([
        fisica / escala, gen7 / escala, gen21 / escala,
        base7 / escala, base21 / escala,
        g / 1000, rad7 / 1000, rad21 / 1000,
        nube / 100, (temp - 25) / 20,
        np.sin(2 * np.pi * hora / 24),
        np.cos(2 * np.pi * hora / 24),
        np.full(24, np.sin(est)), np.full(24, np.cos(est)),
    ]).astype(np.float32)
    return fisica, x, g


def predecir(historia, clima_dia):
    torch.manual_seed(SEMILLA)
    torch.set_num_threads(1)
    dias = _dias_completos(historia)
    if len(dias) < 14:
        raise ValueError("Se necesitan al menos 14 días completos")
    fechas = sorted(dias)
    futuro = clima_dia.copy()
    futuro["fecha_hora"] = pd.to_datetime(futuro["fecha_hora"])
    objetivo = futuro.fecha_hora.min().date()
    rezago = max((objetivo - fechas[-1]).days, 1)
    escala = max(float(np.nanpercentile(historia["solar_mwh"], 99)), 1)
    base, x_obj, radiacion = _caracteristicas(
        dias, objetivo, fechas[-1], escala, futuro
    )

    xs, ys, pesos = [], [], []
    for dia in fechas:
        corte = dia - dt.timedelta(days=rezago)
        # Exigir al menos 14 días conocidos antes de esta fecha.
        if sum(d <= corte for d in fechas) < 14:
            continue
        dato = dias[dia]
        if not np.isfinite(dato[["nubosidad", "temperatura"]].to_numpy(float)).all():
            continue
        fis, x, _ = _caracteristicas(dias, dia, corte, escala, dato)
        real = dato["solar_mwh"].to_numpy(float)
        xs.append(x)
        ys.append(((real - fis) / escala).astype(np.float32))
        # Los rankings evalúan las horas 06 a 18, no las 24 por igual.
        pesos.append(np.where((np.arange(24) >= 6) & (np.arange(24) <= 18),
                              1.0, 0.15).astype(np.float32))

    if not xs:
        return np.clip(base, 0, None)
    X = torch.from_numpy(np.concatenate(xs))
    Y = torch.from_numpy(np.concatenate(ys))
    W = torch.from_numpy(np.concatenate(pesos))
    red = RedResidual(X.shape[1])
    opt = torch.optim.AdamW(red.parameters(), lr=0.005, weight_decay=0.02)
    for _ in range(180):
        opt.zero_grad()
        err = nn.functional.smooth_l1_loss(red(X), Y, beta=0.1, reduction="none")
        perdida = (err * W).sum() / W.sum()
        perdida.backward()
        opt.step()

    red.eval()
    with torch.no_grad():
        residual = red(torch.from_numpy(x_obj)).numpy() * escala
    # En las horas nocturnas no permitir correcciones positivas espurias.
    pred = np.clip(base + residual, 0, None)
    pred[(np.arange(24) < 6) | (np.arange(24) > 19)] = 0
    return pred.astype(float)
