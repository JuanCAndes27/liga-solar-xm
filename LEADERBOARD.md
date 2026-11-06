# ☀️ Liga de Pronóstico Solar Colombia — Leaderboard

_Actualizado: 2026-11-06 13:48 (hora Colombia) · Métrica: MAE en horas de sol (06–18 h) · Skill = 1 − MAE/MAE_persistencia (positivo = le ganas a la persistencia)_

## 🏆 Liga oficial (predicciones hechas ANTES de conocer el dato real)

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | SolarNet-CNN | profe (reto 4) | 27 | 238.6 | 16.4% | +30.2% |
| 🥈 | SolarNet-Cuantiles (q50) | profe (reto 6) | 27 | 239.5 | 16.4% | +34.3% |
| 🥉 | SolarNet-Nubes | profe (reto 2) | 27 | 243.5 | 16.7% | +32.8% |
| 4 | SolarNet-GRU | profe | 27 | 248.9 | 17.1% | +32.1% |
| 5 | SolarNet-Ensamble×5 | profe (reto 5) | 27 | 250.1 | 17.2% | +32.8% |
| 6 | SolarNet-Ponderada | profe (reto 3) | 27 | 251.6 | 17.3% | +34.0% |
| 7 | SolarNet-Transformer | profe (reto 4) | 27 | 263.3 | 18.1% | +28.2% |
| 8 | Persistencia × radiación | profe | 27 | 291.7 | 20.0% | +26.3% |
| 9 | Persistencia 3 días | profe (reto 1) | 27 | 348.3 | 23.9% | +5.8% |
| 10 | Persistencia | profe | 27 | 438.0 | 30.0% | — |

![último día](resultados/ultimo_dia.png)

## 🧪 Backtest (días pasados, para arrancar en frío)

_Ojo: en el backtest el 'pronóstico' de clima es casi el clima observado → resultados optimistas._

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | SolarNet-GRU | profe | 30 | 149.7 | 9.8% | +43.5% |
| 🥈 | SolarNet-Cuantiles (q50) | profe (reto 6) | 30 | 154.1 | 10.1% | +42.1% |
| 🥉 | SolarNet-Ensamble×5 | profe (reto 5) | 30 | 157.2 | 10.3% | +41.5% |
| 4 | SolarNet-Nubes | profe (reto 2) | 30 | 158.2 | 10.4% | +41.3% |
| 5 | SolarNet-Transformer | profe (reto 4) | 30 | 160.0 | 10.5% | +39.9% |
| 6 | SolarNet-Ponderada | profe (reto 3) | 30 | 171.0 | 11.2% | +37.7% |
| 7 | SolarNet-CNN | profe (reto 4) | 30 | 178.3 | 11.7% | +33.4% |
| 8 | Persistencia × radiación | profe | 30 | 217.0 | 14.2% | +22.4% |
| 9 | Persistencia 3 días | profe (reto 1) | 30 | 268.5 | 17.6% | +14.1% |
| 10 | Persistencia | profe | 30 | 319.4 | 20.9% | — |

![backtest](resultados/backtest.png)
