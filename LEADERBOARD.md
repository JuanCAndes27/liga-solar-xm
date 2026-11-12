# ☀️ Liga de Pronóstico Solar Colombia — Leaderboard

_Actualizado: 2026-11-12 14:16 (hora Colombia) · Métrica: MAE en horas de sol (06–18 h) · Skill = 1 − MAE/MAE_persistencia (positivo = le ganas a la persistencia)_

## 🏆 Liga oficial (predicciones hechas ANTES de conocer el dato real)

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | Rowan-SolarHybrid | rowanvrock96 | 33 | 212.8 | 14.5% | +24.5% |
| 🥈 | SolarNet-Cuantiles (q50) | profe (reto 6) | 34 | 214.4 | 14.7% | +20.5% |
| 🥉 | SolarNet-GRU | profe | 34 | 217.3 | 14.9% | +19.9% |
| 4 | SolarNet-Nubes | profe (reto 2) | 34 | 218.3 | 14.9% | +17.8% |
| 5 | SolarNet-Ensamble×5 | profe (reto 5) | 34 | 218.8 | 15.0% | +18.0% |
| 6 | SolarNet-Ponderada | profe (reto 3) | 34 | 225.3 | 15.4% | +15.6% |
| 7 | SolarNet-CNN | profe (reto 4) | 34 | 230.1 | 15.7% | +13.8% |
| 8 | SolarNet-Transformer | profe (reto 4) | 34 | 230.7 | 15.8% | +11.2% |
| 9 | Persistencia × radiación | profe | 34 | 253.0 | 17.3% | +11.6% |
| 10 | Persistencia 3 días | profe (reto 1) | 34 | 288.2 | 19.7% | +0.9% |
| 11 | Persistencia | profe | 34 | 332.0 | 22.7% | — |

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
