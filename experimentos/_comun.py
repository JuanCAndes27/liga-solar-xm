"""Utilidades de los experimentos: mismos datos y mismo corte de rezago que el backtest de la liga."""
import datetime as dt
import sys
from pathlib import Path

import numpy as np

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "modelos"))
from liga import datos  # noqa: E402
from liga.run_diario import HORAS_SOL, clima_de  # noqa: E402


def cargar(real: bool):
    """--real usa datos/ ya descargados (corran antes la liga sin --demo); si no, datos sintéticos."""
    if real:
        return datos.cargar()
    gen, clima = datos.datos_sinteticos()
    return gen.merge(clima, on="fecha_hora", how="left"), clima


def dias_backtest(hist, clima, n):
    """Para cada uno de los últimos n días: (día, historia con rezago de 2 días, clima del día, real)."""
    for d in sorted(hist.fecha_hora.dt.date.unique())[-n:]:
        h = hist[hist.fecha_hora.dt.date < d - dt.timedelta(days=1)]
        real = hist[hist.fecha_hora.dt.date == d].sort_values("fecha_hora")["solar_mwh"].to_numpy()
        yield d, h, clima_de(clima, d), real


def mae_sol(pred, real):
    return float(np.abs(np.asarray(pred)[HORAS_SOL] - real[HORAS_SOL]).mean())
