# ☀️ Liga de Pronóstico Solar Colombia — Leaderboard

_Actualizado: 2026-11-27 15:25 (hora Colombia) · Métrica: MAE en horas de sol (06–18 h) · Skill = 1 − MAE/MAE_persistencia (positivo = le ganas a la persistencia)_

## 🏆 Liga oficial (predicciones hechas ANTES de conocer el dato real)

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | SolarNet-Cuantiles (q50) | profe (reto 6) | 49 | 203.1 | 13.6% | +16.0% |
| 🥈 | SolarNet-Nubes | profe (reto 2) | 49 | 207.1 | 13.8% | +13.0% |
| 🥉 | Rowan-SolarHybrid | rowanvrock96 | 48 | 207.7 | 13.8% | +15.8% |
| 4 | SolarNet-GRU | profe | 49 | 209.1 | 14.0% | +13.6% |
| 5 | SolarNet-Ensamble×5 | profe (reto 5) | 49 | 209.9 | 14.0% | +11.8% |
| 6 | SolarNet-Ponderada | profe (reto 3) | 49 | 217.6 | 14.5% | +8.0% |
| 7 | SolarNet-Transformer | profe (reto 4) | 49 | 219.6 | 14.7% | +6.2% |
| 8 | SolarNet-CNN | profe (reto 4) | 49 | 221.2 | 14.8% | +6.9% |
| 9 | Persistencia × radiación | profe | 49 | 227.3 | 15.2% | +14.3% |
| 10 | Persistencia 3 días | profe (reto 1) | 49 | 271.8 | 18.2% | +3.0% |
| 11 | Persistencia | profe | 49 | 310.1 | 20.7% | — |

![último día](resultados/ultimo_dia.png)

## 🧪 Backtest (días pasados, para arrancar en frío)

_Ojo: en el backtest el 'pronóstico' de clima es casi el clima observado → resultados optimistas._

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | SolarNet-GRU | profe | 14 | 170.5 | 11.8% | +34.8% |
| 🥈 | Rowan-SolarHybrid | rowanvrock96 | 14 | 171.9 | 11.9% | +33.3% |
| 🥉 | SolarNet-Cuantiles (q50) | profe (reto 6) | 14 | 183.4 | 12.7% | +32.3% |
| 4 | SolarNet-Nubes | profe (reto 2) | 14 | 187.6 | 13.0% | +30.5% |
| 5 | SolarNet-Ensamble×5 | profe (reto 5) | 14 | 193.9 | 13.4% | +27.6% |
| 6 | SolarNet-CNN | profe (reto 4) | 14 | 195.3 | 13.5% | +30.9% |
| 7 | SolarNet-Transformer | profe (reto 4) | 14 | 196.6 | 13.6% | +26.5% |
| 8 | SolarNet-Ponderada | profe (reto 3) | 14 | 212.7 | 14.7% | +23.6% |
| 9 | Persistencia × radiación | profe | 14 | 244.9 | 17.0% | +13.4% |
| 10 | Persistencia 3 días | profe (reto 1) | 14 | 298.9 | 20.7% | +10.6% |
| 11 | Persistencia | profe | 14 | 334.9 | 23.2% | — |

![backtest](resultados/backtest.png)
