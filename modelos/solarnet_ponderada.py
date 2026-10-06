"""Reto 3: SolarNet-GRU con pérdida ponderada por hora.

Con MSE normal, equivocarse 10 % a las 7 h y a las 12 h 'cuenta' parecido para el optimizador si
los valores normalizados son similares, pero en MWh el error del mediodía es mucho mayor.
Ponderamos cada hora por su generación promedio → la red invierte su capacidad donde están los MWh.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import _solarnet_comun as sn  # noqa: E402

NOMBRE = "SolarNet-Ponderada"
AUTOR = "profe (reto 3)"


def predecir(historia, clima_dia):
    return sn.predecir_con(sn.GRU, historia, clima_dia,
                           perdida=lambda Y: sn.mse_ponderado(sn.pesos_por_hora(Y)))
