# ☀️ Liga de Pronóstico Solar Colombia — Leaderboard

_Actualizado: 2026-10-22 11:22 (hora Colombia) · Métrica: MAE en horas de sol (06–18 h) · Skill = 1 − MAE/MAE_persistencia (positivo = le ganas a la persistencia)_

## 🏆 Liga oficial (predicciones hechas ANTES de conocer el dato real)

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | SolarNet-Ponderada | profe (reto 3) | 12 | 200.5 | 13.6% | +31.7% |
| 🥈 | SolarNet-Cuantiles (q50) | profe (reto 6) | 12 | 201.2 | 13.7% | +28.4% |
| 🥉 | SolarNet-Nubes | profe (reto 2) | 12 | 202.3 | 13.7% | +26.5% |
| 4 | SolarNet-Ensamble×5 | profe (reto 5) | 12 | 206.0 | 14.0% | +27.7% |
| 5 | SolarNet-GRU | profe | 12 | 215.2 | 14.6% | +25.5% |
| 6 | SolarNet-CNN | profe (reto 4) | 12 | 216.9 | 14.7% | +19.5% |
| 7 | SolarNet-Transformer | profe (reto 4) | 12 | 220.3 | 15.0% | +21.0% |
| 8 | Persistencia 3 días | profe (reto 1) | 12 | 258.6 | 17.6% | +9.6% |
| 9 | Persistencia × radiación | profe | 12 | 261.8 | 17.8% | +15.1% |
| 10 | Persistencia | profe | 12 | 351.0 | 23.8% | — |

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
