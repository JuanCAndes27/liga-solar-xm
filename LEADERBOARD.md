# ☀️ Liga de Pronóstico Solar Colombia — Leaderboard

_Actualizado: 2026-11-21 13:32 (hora Colombia) · Métrica: MAE en horas de sol (06–18 h) · Skill = 1 − MAE/MAE_persistencia (positivo = le ganas a la persistencia)_

## 🏆 Liga oficial (predicciones hechas ANTES de conocer el dato real)

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | SolarNet-Cuantiles (q50) | profe (reto 6) | 40 | 226.6 | 15.2% | +31.9% |
| 🥈 | SolarNet-CNN | profe (reto 4) | 40 | 230.7 | 15.5% | +27.7% |
| 🥉 | SolarNet-Nubes | profe (reto 2) | 40 | 230.8 | 15.5% | +29.8% |
| 4 | SolarNet-GRU | profe | 40 | 236.8 | 15.9% | +28.5% |
| 5 | SolarNet-Ensamble×5 | profe (reto 5) | 40 | 237.9 | 15.9% | +29.4% |
| 6 | SolarNet-Ponderada | profe (reto 3) | 40 | 239.8 | 16.1% | +30.4% |
| 7 | SolarNet-Transformer | profe (reto 4) | 40 | 246.9 | 16.5% | +25.4% |
| 8 | Persistencia × radiación | profe | 40 | 268.4 | 18.0% | +27.8% |
| 9 | Persistencia 3 días | profe (reto 1) | 40 | 345.1 | 23.1% | +5.2% |
| 10 | Persistencia | profe | 40 | 414.8 | 27.8% | — |

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
