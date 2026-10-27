# ☀️ Liga de Pronóstico Solar Colombia — Leaderboard

_Actualizado: 2026-10-27 11:58 (hora Colombia) · Métrica: MAE en horas de sol (06–18 h) · Skill = 1 − MAE/MAE_persistencia (positivo = le ganas a la persistencia)_

## 🏆 Liga oficial (predicciones hechas ANTES de conocer el dato real)

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | SolarNet-Cuantiles (q50) | profe (reto 6) | 18 | 207.9 | 14.6% | +28.6% |
| 🥈 | SolarNet-Ponderada | profe (reto 3) | 18 | 209.3 | 14.7% | +29.0% |
| 🥉 | SolarNet-Nubes | profe (reto 2) | 18 | 212.0 | 14.9% | +27.0% |
| 4 | SolarNet-Ensamble×5 | profe (reto 5) | 18 | 214.8 | 15.1% | +26.7% |
| 5 | SolarNet-GRU | profe | 18 | 216.2 | 15.2% | +25.9% |
| 6 | SolarNet-Transformer | profe (reto 4) | 18 | 218.0 | 15.4% | +24.5% |
| 7 | Rowan-SolarHybrid | rowanvrock96 | 17 | 218.5 | 15.3% | +28.4% |
| 8 | SolarNet-CNN | profe (reto 4) | 18 | 228.0 | 16.1% | +20.5% |
| 9 | Persistencia × radiación | profe | 18 | 261.5 | 18.4% | +8.2% |
| 10 | Persistencia 3 días | profe (reto 1) | 18 | 321.1 | 22.6% | -12.3% |
| 11 | Persistencia | profe | 18 | 325.1 | 22.9% | — |

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
