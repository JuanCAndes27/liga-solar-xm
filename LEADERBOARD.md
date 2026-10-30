# ☀️ Liga de Pronóstico Solar Colombia — Leaderboard

_Actualizado: 2026-10-30 12:22 (hora Colombia) · Métrica: MAE en horas de sol (06–18 h) · Skill = 1 − MAE/MAE_persistencia (positivo = le ganas a la persistencia)_

## 🏆 Liga oficial (predicciones hechas ANTES de conocer el dato real)

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | SolarNet-Cuantiles (q50) | profe (reto 6) | 21 | 208.9 | 14.8% | +27.3% |
| 🥈 | SolarNet-Ponderada | profe (reto 3) | 21 | 209.3 | 14.8% | +28.3% |
| 🥉 | SolarNet-Nubes | profe (reto 2) | 21 | 211.4 | 15.0% | +26.6% |
| 4 | Rowan-SolarHybrid | rowanvrock96 | 20 | 211.7 | 14.9% | +29.8% |
| 5 | SolarNet-Ensamble×5 | profe (reto 5) | 21 | 213.0 | 15.1% | +26.5% |
| 6 | SolarNet-Transformer | profe (reto 4) | 21 | 216.7 | 15.4% | +24.4% |
| 7 | SolarNet-GRU | profe | 21 | 218.2 | 15.5% | +24.1% |
| 8 | SolarNet-CNN | profe (reto 4) | 21 | 227.7 | 16.1% | +20.8% |
| 9 | Persistencia × radiación | profe | 21 | 259.7 | 18.4% | +9.4% |
| 10 | Persistencia 3 días | profe (reto 1) | 21 | 302.2 | 21.4% | -4.5% |
| 11 | Persistencia | profe | 21 | 330.5 | 23.4% | — |

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
