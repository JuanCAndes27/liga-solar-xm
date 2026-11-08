# ☀️ Liga de Pronóstico Solar Colombia — Leaderboard

_Actualizado: 2026-11-08 12:19 (hora Colombia) · Métrica: MAE en horas de sol (06–18 h) · Skill = 1 − MAE/MAE_persistencia (positivo = le ganas a la persistencia)_

## 🏆 Liga oficial (predicciones hechas ANTES de conocer el dato real)

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | Rowan-SolarHybrid | rowanvrock96 | 29 | 215.4 | 14.8% | +21.8% |
| 🥈 | SolarNet-Cuantiles (q50) | profe (reto 6) | 30 | 217.0 | 15.0% | +17.6% |
| 🥉 | SolarNet-GRU | profe | 30 | 222.0 | 15.4% | +16.4% |
| 4 | SolarNet-Ensamble×5 | profe (reto 5) | 30 | 222.9 | 15.4% | +14.4% |
| 5 | SolarNet-Nubes | profe (reto 2) | 30 | 223.5 | 15.5% | +13.9% |
| 6 | SolarNet-Ponderada | profe (reto 3) | 30 | 230.6 | 16.0% | +11.7% |
| 7 | SolarNet-Transformer | profe (reto 4) | 30 | 231.7 | 16.0% | +8.2% |
| 8 | SolarNet-CNN | profe (reto 4) | 30 | 234.8 | 16.3% | +9.6% |
| 9 | Persistencia × radiación | profe | 30 | 254.8 | 17.6% | +8.1% |
| 10 | Persistencia 3 días | profe (reto 1) | 30 | 285.0 | 19.7% | +0.0% |
| 11 | Persistencia | profe | 30 | 327.3 | 22.7% | — |

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
