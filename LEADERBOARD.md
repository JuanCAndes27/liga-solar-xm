# ☀️ Liga de Pronóstico Solar Colombia — Leaderboard

_Actualizado: 2026-11-22 13:47 (hora Colombia) · Métrica: MAE en horas de sol (06–18 h) · Skill = 1 − MAE/MAE_persistencia (positivo = le ganas a la persistencia)_

## 🏆 Liga oficial (predicciones hechas ANTES de conocer el dato real)

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | SolarNet-Cuantiles (q50) | profe (reto 6) | 44 | 203.9 | 13.7% | +20.1% |
| 🥈 | Rowan-SolarHybrid | rowanvrock96 | 43 | 206.8 | 13.8% | +21.4% |
| 🥉 | SolarNet-Ensamble×5 | profe (reto 5) | 44 | 207.1 | 13.9% | +17.8% |
| 4 | SolarNet-Nubes | profe (reto 2) | 44 | 207.1 | 13.9% | +17.1% |
| 5 | SolarNet-GRU | profe | 44 | 208.0 | 13.9% | +19.0% |
| 6 | SolarNet-Ponderada | profe (reto 3) | 44 | 214.8 | 14.4% | +14.3% |
| 7 | SolarNet-Transformer | profe (reto 4) | 44 | 216.9 | 14.5% | +12.4% |
| 8 | SolarNet-CNN | profe (reto 4) | 44 | 221.2 | 14.8% | +11.4% |
| 9 | Persistencia × radiación | profe | 44 | 237.3 | 15.9% | +14.0% |
| 10 | Persistencia 3 días | profe (reto 1) | 44 | 288.6 | 19.3% | +0.1% |
| 11 | Persistencia | profe | 44 | 325.6 | 21.8% | — |

![último día](resultados/ultimo_dia.png)

## 🧪 Backtest (días pasados, para arrancar en frío)

_Ojo: en el backtest el 'pronóstico' de clima es casi el clima observado → resultados optimistas._

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | SolarNet-GRU | profe | 14 | 170.4 | 11.8% | +34.8% |
| 🥈 | Rowan-SolarHybrid | rowanvrock96 | 14 | 171.9 | 11.9% | +33.3% |
| 🥉 | SolarNet-Cuantiles (q50) | profe (reto 6) | 14 | 183.3 | 12.7% | +32.4% |
| 4 | SolarNet-Nubes | profe (reto 2) | 14 | 187.4 | 13.0% | +30.5% |
| 5 | SolarNet-Ensamble×5 | profe (reto 5) | 14 | 193.8 | 13.4% | +27.6% |
| 6 | SolarNet-CNN | profe (reto 4) | 14 | 195.2 | 13.5% | +30.9% |
| 7 | SolarNet-Transformer | profe (reto 4) | 14 | 196.4 | 13.6% | +26.5% |
| 8 | SolarNet-Ponderada | profe (reto 3) | 14 | 212.5 | 14.7% | +23.6% |
| 9 | Persistencia × radiación | profe | 14 | 244.8 | 17.0% | +13.4% |
| 10 | Persistencia 3 días | profe (reto 1) | 14 | 298.8 | 20.7% | +10.6% |
| 11 | Persistencia | profe | 14 | 334.8 | 23.2% | — |

![backtest](resultados/backtest.png)
