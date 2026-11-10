# ☀️ Liga de Pronóstico Solar Colombia — Leaderboard

_Actualizado: 2026-11-10 14:00 (hora Colombia) · Métrica: MAE en horas de sol (06–18 h) · Skill = 1 − MAE/MAE_persistencia (positivo = le ganas a la persistencia)_

## 🏆 Liga oficial (predicciones hechas ANTES de conocer el dato real)

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | Rowan-SolarHybrid | rowanvrock96 | 31 | 212.6 | 14.7% | +23.2% |
| 🥈 | SolarNet-Cuantiles (q50) | profe (reto 6) | 32 | 215.3 | 14.9% | +18.9% |
| 🥉 | SolarNet-GRU | profe | 32 | 218.1 | 15.1% | +18.3% |
| 4 | SolarNet-Nubes | profe (reto 2) | 32 | 219.8 | 15.2% | +15.9% |
| 5 | SolarNet-Ensamble×5 | profe (reto 5) | 32 | 219.9 | 15.2% | +16.2% |
| 6 | SolarNet-Ponderada | profe (reto 3) | 32 | 226.5 | 15.7% | +13.8% |
| 7 | SolarNet-CNN | profe (reto 4) | 32 | 230.4 | 16.0% | +11.9% |
| 8 | SolarNet-Transformer | profe (reto 4) | 32 | 231.1 | 16.0% | +9.3% |
| 9 | Persistencia × radiación | profe | 32 | 248.7 | 17.2% | +10.6% |
| 10 | Persistencia 3 días | profe (reto 1) | 32 | 279.3 | 19.4% | +2.4% |
| 11 | Persistencia | profe | 32 | 326.1 | 22.6% | — |

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
