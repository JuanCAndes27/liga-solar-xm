"""Reto 4a: reemplazar la GRU por un Transformer pequeño (1 capa, 2 cabezas de atención).

Con solo ~90 ejemplos (días) un Transformer puede sobreajustar: por eso es diminuto, lleva dropout
y weight decay. Comparen en el leaderboard si la atención le gana a la recurrencia con tan pocos datos.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import _solarnet_comun as sn  # noqa: E402

NOMBRE = "SolarNet-Transformer"
AUTOR = "profe (reto 4)"


def predecir(historia, clima_dia):
    return sn.predecir_con(sn.Transformer, historia, clima_dia, lr=2e-3)
