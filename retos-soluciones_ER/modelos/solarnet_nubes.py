"""Reto 2: SolarNet-GRU + nubosidad de la hora anterior y la siguiente.

Una nube que llega a las 10 h afecta la producción de 9–11 h (las plantas son extensas y la nubosidad
de Open-Meteo es un promedio horario). Dar h-1 y h+1 explícitos le ahorra a la red tener que
'descubrir' ese contexto con la recurrencia.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import _solarnet_comun as sn  # noqa: E402

NOMBRE = "SolarNet-Nubes"
AUTOR = "profe (reto 2)"


def predecir(historia, clima_dia):
    return sn.predecir_con(sn.GRU, historia, clima_dia, contexto_nubes=True)
