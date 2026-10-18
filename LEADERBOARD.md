# ☀️ Liga de Pronóstico Solar Colombia — Leaderboard

_Actualizado: 2026-10-18 07:10 (hora Colombia) · Métrica: MAE en horas de sol (06–18 h) · Skill = 1 − MAE/MAE_persistencia (positivo = le ganas a la persistencia)_

## 🏆 Liga oficial (predicciones hechas ANTES de conocer el dato real)

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | SolarNet-Ponderada | profe (reto 3) | 9 | 213.1 | 14.5% | +17.5% |
| 🥈 | SolarNet-Cuantiles (q50) | profe (reto 6) | 9 | 218.5 | 14.8% | +13.6% |
| 🥉 | SolarNet-Nubes | profe (reto 2) | 9 | 226.5 | 15.4% | +10.7% |
| 4 | SolarNet-GRU | profe | 9 | 227.3 | 15.4% | +10.9% |
| 5 | SolarNet-Ensamble×5 | profe (reto 5) | 9 | 233.2 | 15.8% | +9.8% |
| 6 | SolarNet-Transformer | profe (reto 4) | 9 | 236.4 | 16.1% | +7.0% |
| 7 | Rowan-SolarHybrid | rowanvrock96 | 8 | 238.8 | 15.9% | +11.9% |
| 8 | SolarNet-CNN | profe (reto 4) | 9 | 271.7 | 18.4% | -5.8% |
| 9 | Persistencia | profe | 9 | 292.7 | 19.9% | — |
| 10 | Persistencia × radiación | profe | 9 | 312.6 | 21.2% | -23.5% |
| 11 | Persistencia 3 días | profe (reto 1) | 9 | 331.3 | 22.5% | -28.2% |

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
