# ☀️ Liga de Pronóstico Solar Colombia — Leaderboard

_Actualizado: 2026-10-31 11:27 (hora Colombia) · Métrica: MAE en horas de sol (06–18 h) · Skill = 1 − MAE/MAE_persistencia (positivo = le ganas a la persistencia)_

## 🏆 Liga oficial (predicciones hechas ANTES de conocer el dato real)

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | SolarNet-Ponderada | profe (reto 3) | 22 | 209.6 | 14.7% | +30.3% |
| 🥈 | SolarNet-Cuantiles (q50) | profe (reto 6) | 22 | 210.1 | 14.8% | +29.3% |
| 🥉 | Rowan-SolarHybrid | rowanvrock96 | 21 | 211.8 | 14.8% | +31.9% |
| 4 | SolarNet-Nubes | profe (reto 2) | 22 | 213.0 | 15.0% | +28.5% |
| 5 | SolarNet-Ensamble×5 | profe (reto 5) | 22 | 213.8 | 15.0% | +28.6% |
| 6 | SolarNet-GRU | profe | 22 | 218.0 | 15.3% | +26.3% |
| 7 | SolarNet-Transformer | profe (reto 4) | 22 | 219.4 | 15.4% | +26.3% |
| 8 | SolarNet-CNN | profe (reto 4) | 22 | 228.0 | 16.0% | +23.1% |
| 9 | Persistencia × radiación | profe | 22 | 265.6 | 18.7% | +11.3% |
| 10 | Persistencia 3 días | profe (reto 1) | 22 | 299.3 | 21.0% | -1.1% |
| 11 | Persistencia | profe | 22 | 351.6 | 24.7% | — |

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
