# ☀️ Liga de Pronóstico Solar Colombia — Leaderboard

_Actualizado: 2026-11-03 13:46 (hora Colombia) · Métrica: MAE en horas de sol (06–18 h) · Skill = 1 − MAE/MAE_persistencia (positivo = le ganas a la persistencia)_

## 🏆 Liga oficial (predicciones hechas ANTES de conocer el dato real)

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | SolarNet-Cuantiles (q50) | profe (reto 6) | 25 | 208.2 | 14.4% | +26.9% |
| 🥈 | Rowan-SolarHybrid | rowanvrock96 | 24 | 210.0 | 14.4% | +29.1% |
| 🥉 | SolarNet-Nubes | profe (reto 2) | 25 | 211.0 | 14.6% | +26.1% |
| 4 | SolarNet-Ensamble×5 | profe (reto 5) | 25 | 212.3 | 14.7% | +25.9% |
| 5 | SolarNet-Ponderada | profe (reto 3) | 25 | 213.7 | 14.8% | +25.5% |
| 6 | SolarNet-GRU | profe | 25 | 217.3 | 15.0% | +23.3% |
| 7 | SolarNet-Transformer | profe (reto 4) | 25 | 218.5 | 15.1% | +23.4% |
| 8 | SolarNet-CNN | profe (reto 4) | 25 | 228.6 | 15.8% | +19.3% |
| 9 | Persistencia × radiación | profe | 25 | 262.3 | 18.2% | +9.3% |
| 10 | Persistencia 3 días | profe (reto 1) | 25 | 293.6 | 20.3% | -2.6% |
| 11 | Persistencia | profe | 25 | 337.4 | 23.4% | — |

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
