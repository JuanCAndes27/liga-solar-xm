"""Modelo inicial de Rowan: promedio horario de los últimos siete días disponibles.

Interfaz de la Liga Solar XM:
- historia: DataFrame con fecha_hora y solar_mwh.
- clima_dia: pronóstico meteorológico de las 24 horas objetivo.
- salida: vector de 24 valores de generación solar (MWh).

Este modelo de referencia no usa todavía las variables meteorológicas.
"""
import numpy as np

NOMBRE = "Rowan"
AUTOR = "rowanvrock96"


def predecir(historia, clima_dia):
    """Devuelve la media de generación por hora de los últimos siete días."""
    ult = historia[historia.fecha_hora >= historia.fecha_hora.max() - np.timedelta64(7, "D")]
    return (
        ult.groupby(ult.fecha_hora.dt.hour)["solar_mwh"]
        .mean()
        .reindex(range(24), fill_value=0)
        .to_numpy()
    )
