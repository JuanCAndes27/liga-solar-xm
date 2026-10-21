# ☀️ Liga de Pronóstico Solar Colombia — Leaderboard

_Actualizado: 2026-10-21 11:14 (hora Colombia) · Métrica: MAE en horas de sol (06–18 h) · Skill = 1 − MAE/MAE_persistencia (positivo = le ganas a la persistencia)_

## 🏆 Liga oficial (predicciones hechas ANTES de conocer el dato real)

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | SolarNet-Ponderada | profe (reto 3) | 12 | 192.1 | 13.2% | +29.3% |
| 🥈 | SolarNet-Cuantiles (q50) | profe (reto 6) | 12 | 193.5 | 13.3% | +27.1% |
| 🥉 | SolarNet-GRU | profe | 12 | 200.4 | 13.8% | +24.8% |
| 4 | SolarNet-Nubes | profe (reto 2) | 12 | 202.1 | 13.9% | +24.3% |
| 5 | SolarNet-Ensamble×5 | profe (reto 5) | 12 | 207.2 | 14.3% | +23.5% |
| 6 | SolarNet-Transformer | profe (reto 4) | 12 | 212.2 | 14.6% | +20.7% |
| 7 | Rowan-SolarHybrid | rowanvrock96 | 11 | 215.4 | 14.6% | +24.4% |
| 8 | SolarNet-CNN | profe (reto 4) | 12 | 230.9 | 15.9% | +13.3% |
| 9 | Persistencia 3 días | profe (reto 1) | 12 | 286.0 | 19.7% | -6.4% |
| 10 | Persistencia × radiación | profe | 12 | 286.9 | 19.8% | -6.8% |
| 11 | Persistencia | profe | 12 | 310.6 | 21.4% | — |

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
