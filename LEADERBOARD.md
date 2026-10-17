# ☀️ Liga de Pronóstico Solar Colombia — Leaderboard

_Actualizado: 2026-10-17 07:11 (hora Colombia) · Métrica: MAE en horas de sol (06–18 h) · Skill = 1 − MAE/MAE_persistencia (positivo = le ganas a la persistencia)_

## 🏆 Liga oficial (predicciones hechas ANTES de conocer el dato real)

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | SolarNet-Ponderada | profe (reto 3) | 7 | 225.3 | 16.7% | +16.9% |
| 🥈 | SolarNet-Cuantiles (q50) | profe (reto 6) | 7 | 229.6 | 17.0% | +12.8% |
| 🥉 | SolarNet-GRU | profe | 7 | 238.7 | 17.7% | +10.6% |
| 4 | SolarNet-Nubes | profe (reto 2) | 7 | 240.9 | 17.8% | +9.0% |
| 5 | SolarNet-Transformer | profe (reto 4) | 7 | 243.6 | 18.0% | +8.7% |
| 6 | SolarNet-Ensamble×5 | profe (reto 5) | 7 | 245.0 | 18.1% | +9.9% |
| 7 | Rowan-SolarHybrid | rowanvrock96 | 6 | 251.8 | 18.4% | +13.6% |
| 8 | SolarNet-CNN | profe (reto 4) | 7 | 277.5 | 20.6% | -2.3% |
| 9 | Persistencia 3 días | profe (reto 1) | 7 | 301.7 | 22.4% | -8.1% |
| 10 | Persistencia | profe | 7 | 313.6 | 23.2% | — |
| 11 | Persistencia × radiación | profe | 7 | 345.3 | 25.6% | -33.0% |

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
