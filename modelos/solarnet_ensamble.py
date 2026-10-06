"""Reto 5: ensamble de 5 semillas de SolarNet-GRU.

Cada semilla cambia la inicialización de los pesos → cada red cae en un mínimo distinto.
Promediarlas reduce la parte 'aleatoria' del error (varianza) sin tocar el sesgo.
Para medir si de verdad baja la varianza: python -m experimentos.varianza_semillas
"""
import numpy as np

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import _solarnet_comun as sn  # noqa: E402

NOMBRE = "SolarNet-Ensamble×5"
AUTOR = "profe (reto 5)"
SEMILLAS = [0, 1, 2, 3, 4]


def predecir(historia, clima_dia):
    return np.mean([sn.predecir_con(sn.GRU, historia, clima_dia, semilla=s) for s in SEMILLAS], axis=0)
