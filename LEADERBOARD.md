# ☀️ Liga de Pronóstico Solar Colombia — Leaderboard

_Actualizado: 2026-10-23 11:02 (hora Colombia) · Métrica: MAE en horas de sol (06–18 h) · Skill = 1 − MAE/MAE_persistencia (positivo = le ganas a la persistencia)_

## 🏆 Liga oficial (predicciones hechas ANTES de conocer el dato real)

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | SolarNet-Cuantiles (q50) | profe (reto 6) | 14 | 186.9 | 12.9% | +28.7% |
| 🥈 | SolarNet-Ponderada | profe (reto 3) | 14 | 187.2 | 12.9% | +30.0% |
| 🥉 | SolarNet-Ensamble×5 | profe (reto 5) | 14 | 198.4 | 13.7% | +25.6% |
| 4 | SolarNet-Nubes | profe (reto 2) | 14 | 200.9 | 13.9% | +24.3% |
| 5 | Rowan-SolarHybrid | rowanvrock96 | 13 | 202.0 | 13.8% | +26.8% |
| 6 | SolarNet-Transformer | profe (reto 4) | 14 | 203.2 | 14.0% | +22.9% |
| 7 | SolarNet-GRU | profe | 14 | 203.7 | 14.1% | +23.7% |
| 8 | SolarNet-CNN | profe (reto 4) | 14 | 219.8 | 15.2% | +16.5% |
| 9 | Persistencia × radiación | profe | 14 | 262.9 | 18.1% | +1.2% |
| 10 | Persistencia 3 días | profe (reto 1) | 14 | 282.7 | 19.5% | -10.9% |
| 11 | Persistencia | profe | 14 | 305.8 | 21.1% | — |

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
