# ☀️ Liga de Pronóstico Solar Colombia — Leaderboard

_Actualizado: 2026-10-14 07:20 (hora Colombia) · Métrica: MAE en horas de sol (06–18 h) · Skill = 1 − MAE/MAE_persistencia (positivo = le ganas a la persistencia)_

## 🏆 Liga oficial (predicciones hechas ANTES de conocer el dato real)

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | SolarNet-Ponderada | profe (reto 3) | 3 | 149.0 | 10.1% | +37.1% |
| 🥈 | SolarNet-GRU | profe | 3 | 174.8 | 11.9% | +25.0% |
| 🥉 | SolarNet-Nubes | profe (reto 2) | 3 | 185.2 | 12.6% | +20.5% |
| 4 | SolarNet-Ensamble×5 | profe (reto 5) | 3 | 193.9 | 13.2% | +19.0% |
| 5 | SolarNet-Cuantiles (q50) | profe (reto 6) | 3 | 196.7 | 13.4% | +17.8% |
| 6 | Rowan-SolarHybrid | rowanvrock96 | 2 | 202.2 | 12.7% | +23.5% |
| 7 | SolarNet-Transformer | profe (reto 4) | 3 | 208.7 | 14.2% | +11.5% |
| 8 | SolarNet-CNN | profe (reto 4) | 3 | 229.3 | 15.6% | +3.0% |
| 9 | Persistencia | profe | 3 | 243.5 | 16.6% | — |
| 10 | Persistencia 3 días | profe (reto 1) | 3 | 293.5 | 20.0% | -15.8% |
| 11 | Persistencia × radiación | profe | 3 | 294.4 | 20.0% | -30.3% |

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
