# ☀️ Liga de Pronóstico Solar Colombia — Leaderboard

_Actualizado: 2026-11-11 13:57 (hora Colombia) · Métrica: MAE en horas de sol (06–18 h) · Skill = 1 − MAE/MAE_persistencia (positivo = le ganas a la persistencia)_

## 🏆 Liga oficial (predicciones hechas ANTES de conocer el dato real)

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | Rowan-SolarHybrid | rowanvrock96 | 32 | 213.2 | 14.7% | +24.3% |
| 🥈 | SolarNet-Cuantiles (q50) | profe (reto 6) | 33 | 214.5 | 14.8% | +20.3% |
| 🥉 | SolarNet-GRU | profe | 33 | 217.2 | 15.0% | +19.8% |
| 4 | SolarNet-Nubes | profe (reto 2) | 33 | 218.7 | 15.1% | +17.5% |
| 5 | SolarNet-Ensamble×5 | profe (reto 5) | 33 | 218.8 | 15.1% | +17.8% |
| 6 | SolarNet-Ponderada | profe (reto 3) | 33 | 225.4 | 15.6% | +15.4% |
| 7 | SolarNet-Transformer | profe (reto 4) | 33 | 230.9 | 16.0% | +10.9% |
| 8 | SolarNet-CNN | profe (reto 4) | 33 | 231.4 | 16.0% | +13.1% |
| 9 | Persistencia × radiación | profe | 33 | 254.8 | 17.6% | +10.9% |
| 10 | Persistencia 3 días | profe (reto 1) | 33 | 279.9 | 19.3% | +3.7% |
| 11 | Persistencia | profe | 33 | 333.3 | 23.0% | — |

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
