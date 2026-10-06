"""Reto 1: persistencia de 3 días.

gen_mañana(h) = promedio de los últimos 3 días conocidos a la hora h.
Promediar suaviza un día atípico (un aguacero en el Cesar) que la persistencia simple copia tal cual.
"""
import numpy as np

NOMBRE = "Persistencia 3 días"
AUTOR = "profe (reto 1)"
N_DIAS = 3


def predecir(historia, clima_dia):
    h = historia.assign(fecha=historia.fecha_hora.dt.date)
    completos = h.groupby("fecha").filter(lambda g: len(g) == 24)
    ultimos = sorted(completos.fecha.unique())[-N_DIAS:]
    sel = completos[completos.fecha.isin(ultimos)]
    return sel.groupby(sel.fecha_hora.dt.hour)["solar_mwh"].mean().reindex(range(24), fill_value=0).to_numpy()
