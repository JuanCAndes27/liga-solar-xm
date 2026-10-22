# ☀️ Liga de Pronóstico Solar Colombia — Leaderboard

_Actualizado: 2026-10-22 11:13 (hora Colombia) · Métrica: MAE en horas de sol (06–18 h) · Skill = 1 − MAE/MAE_persistencia (positivo = le ganas a la persistencia)_

## 🏆 Liga oficial (predicciones hechas ANTES de conocer el dato real)

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | SolarNet-Ponderada | profe (reto 3) | 13 | 189.7 | 13.0% | +31.6% |
| 🥈 | SolarNet-Cuantiles (q50) | profe (reto 6) | 13 | 190.4 | 13.1% | +29.6% |
| 🥉 | SolarNet-Ensamble×5 | profe (reto 5) | 13 | 202.2 | 13.9% | +26.6% |
| 4 | SolarNet-Nubes | profe (reto 2) | 13 | 204.5 | 14.0% | +25.4% |
| 5 | Rowan-SolarHybrid | rowanvrock96 | 12 | 205.3 | 13.9% | +28.6% |
| 6 | SolarNet-Transformer | profe (reto 4) | 13 | 207.1 | 14.2% | +23.8% |
| 7 | SolarNet-GRU | profe | 13 | 207.5 | 14.2% | +24.8% |
| 8 | SolarNet-CNN | profe (reto 4) | 13 | 225.1 | 15.4% | +16.9% |
| 9 | Persistencia 3 días | profe (reto 1) | 13 | 271.5 | 18.6% | -0.2% |
| 10 | Persistencia × radiación | profe | 13 | 273.9 | 18.8% | -1.0% |
| 11 | Persistencia | profe | 13 | 316.1 | 21.7% | — |

![último día](resultados/ultimo_dia.png)

## 🧪 Backtest (días pasados, para arrancar en frío)

_Ojo: en el backtest el 'pronóstico' de clima es casi el clima observado → resultados optimistas._

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | SolarNet-GRU | profe | 14 | 170.3 | 11.8% | +34.8% |
| 🥈 | Rowan-SolarHybrid | rowanvrock96 | 14 | 171.8 | 11.9% | +33.3% |
| 🥉 | SolarNet-Cuantiles (q50) | profe (reto 6) | 14 | 183.2 | 12.7% | +32.4% |
| 4 | SolarNet-Nubes | profe (reto 2) | 14 | 187.4 | 13.0% | +30.5% |
| 5 | SolarNet-Ensamble×5 | profe (reto 5) | 14 | 193.7 | 13.4% | +27.6% |
| 6 | SolarNet-CNN | profe (reto 4) | 14 | 195.1 | 13.5% | +30.9% |
| 7 | SolarNet-Transformer | profe (reto 4) | 14 | 196.4 | 13.6% | +26.5% |
| 8 | SolarNet-Ponderada | profe (reto 3) | 14 | 212.4 | 14.7% | +23.6% |
| 9 | Persistencia × radiación | profe | 14 | 244.8 | 17.0% | +13.4% |
| 10 | Persistencia 3 días | profe (reto 1) | 14 | 298.8 | 20.7% | +10.6% |
| 11 | Persistencia | profe | 14 | 334.7 | 23.2% | — |

![backtest](resultados/backtest.png)
