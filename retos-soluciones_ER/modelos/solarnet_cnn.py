"""Reto 4b: reemplazar la GRU por una CNN 1D con convoluciones dilatadas.

La convolución asume que la relación clima→generación es 'local' en el tiempo y igual a cualquier hora
(con la hora como feature para romper esa simetría). Menos parámetros y entrena más rápido que la GRU.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import _solarnet_comun as sn  # noqa: E402

NOMBRE = "SolarNet-CNN"
AUTOR = "profe (reto 4)"


def predecir(historia, clima_dia):
    return sn.predecir_con(sn.CNN1D, historia, clima_dia)
