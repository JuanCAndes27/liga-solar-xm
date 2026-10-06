"""Reto 6 (Pro): SolarNet-GRU probabilística — cuantiles 10, 50 y 90 con pérdida pinball.

Un operador de red no solo quiere 'cuánto', sino 'qué tan seguro': el intervalo 10–90 debería contener
el valor real ~80 % de las horas. La red tiene 3 salidas por hora; una transformación garantiza
q10 ≤ q50 ≤ q90 (los cuantiles no se cruzan).

La liga califica con MAE, así que predecir() entrega la mediana (q50), que es justo el valor que
minimiza el MAE. predecir_cuantiles() entrega las 3 curvas (24×3) para graficar o medir cobertura:
python -m experimentos.cobertura_cuantiles
"""
import torch

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import _solarnet_comun as sn  # noqa: E402

NOMBRE = "SolarNet-Cuantiles (q50)"
AUTOR = "profe (reto 6)"


def predecir_cuantiles(historia, clima_dia, semilla=42):
    X, Y, x, escala = sn.dataset(historia, clima_dia)
    red = sn.GRU(X.shape[-1], n_out=3)
    f = sn.entrenar(red, X, Y, perdida=sn.pinball, salida=sn.cuantiles_monotonos, semilla=semilla)
    with torch.no_grad():
        return f(x)[0].numpy() * escala      # (24, 3): columnas q10, q50, q90


def predecir(historia, clima_dia):
    return predecir_cuantiles(historia, clima_dia)[:, 1]
