# ☀️ Liga de Pronóstico Solar Colombia — Leaderboard

_Actualizado: 2026-11-05 14:10 (hora Colombia) · Métrica: MAE en horas de sol (06–18 h) · Skill = 1 − MAE/MAE_persistencia (positivo = le ganas a la persistencia)_

## 🏆 Liga oficial (predicciones hechas ANTES de conocer el dato real)

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | SolarNet-Cuantiles (q50) | profe (reto 6) | 27 | 206.8 | 14.3% | +26.3% |
| 🥈 | Rowan-SolarHybrid | rowanvrock96 | 26 | 207.8 | 14.3% | +28.1% |
| 🥉 | SolarNet-Nubes | profe (reto 2) | 27 | 211.2 | 14.6% | +24.7% |
| 4 | SolarNet-Ensamble×5 | profe (reto 5) | 27 | 211.8 | 14.6% | +24.6% |
| 5 | SolarNet-Ponderada | profe (reto 3) | 27 | 213.9 | 14.8% | +23.7% |
| 6 | SolarNet-GRU | profe | 27 | 214.7 | 14.8% | +23.1% |
| 7 | SolarNet-Transformer | profe (reto 4) | 27 | 217.9 | 15.1% | +21.9% |
| 8 | SolarNet-CNN | profe (reto 4) | 27 | 225.9 | 15.6% | +19.1% |
| 9 | Persistencia × radiación | profe | 27 | 258.8 | 17.9% | +9.5% |
| 10 | Persistencia 3 días | profe (reto 1) | 27 | 286.0 | 19.8% | -1.5% |
| 11 | Persistencia | profe | 27 | 332.8 | 23.0% | — |

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
