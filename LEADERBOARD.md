# ☀️ Liga de Pronóstico Solar Colombia — Leaderboard

_Actualizado: 2026-11-21 13:23 (hora Colombia) · Métrica: MAE en horas de sol (06–18 h) · Skill = 1 − MAE/MAE_persistencia (positivo = le ganas a la persistencia)_

## 🏆 Liga oficial (predicciones hechas ANTES de conocer el dato real)

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | SolarNet-Cuantiles (q50) | profe (reto 6) | 43 | 205.5 | 13.8% | +22.0% |
| 🥈 | Rowan-SolarHybrid | rowanvrock96 | 42 | 206.4 | 13.8% | +25.8% |
| 🥉 | SolarNet-Nubes | profe (reto 2) | 43 | 207.8 | 13.9% | +20.1% |
| 4 | SolarNet-Ensamble×5 | profe (reto 5) | 43 | 208.3 | 13.9% | +20.1% |
| 5 | SolarNet-GRU | profe | 43 | 209.5 | 14.0% | +21.0% |
| 6 | SolarNet-Ponderada | profe (reto 3) | 43 | 216.3 | 14.5% | +16.4% |
| 7 | SolarNet-Transformer | profe (reto 4) | 43 | 218.4 | 14.6% | +14.5% |
| 8 | SolarNet-CNN | profe (reto 4) | 43 | 221.3 | 14.8% | +15.2% |
| 9 | Persistencia × radiación | profe | 43 | 240.6 | 16.1% | +14.6% |
| 10 | Persistencia 3 días | profe (reto 1) | 43 | 293.3 | 19.6% | +0.2% |
| 11 | Persistencia | profe | 43 | 331.1 | 22.2% | — |

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
