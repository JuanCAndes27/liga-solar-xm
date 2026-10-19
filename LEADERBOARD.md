# ☀️ Liga de Pronóstico Solar Colombia — Leaderboard

_Actualizado: 2026-10-19 12:52 (hora Colombia) · Métrica: MAE en horas de sol (06–18 h) · Skill = 1 − MAE/MAE_persistencia (positivo = le ganas a la persistencia)_

## 🏆 Liga oficial (predicciones hechas ANTES de conocer el dato real)

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | SolarNet-Ponderada | profe (reto 3) | 10 | 202.1 | 13.7% | +23.2% |
| 🥈 | SolarNet-Cuantiles (q50) | profe (reto 6) | 10 | 205.2 | 13.9% | +20.1% |
| 🥉 | SolarNet-GRU | profe | 10 | 212.7 | 14.4% | +17.8% |
| 4 | SolarNet-Nubes | profe (reto 2) | 10 | 214.3 | 14.5% | +17.0% |
| 5 | SolarNet-Ensamble×5 | profe (reto 5) | 10 | 221.5 | 15.0% | +15.9% |
| 6 | SolarNet-Transformer | profe (reto 4) | 10 | 224.4 | 15.2% | +13.4% |
| 7 | Rowan-SolarHybrid | rowanvrock96 | 9 | 226.7 | 15.1% | +18.1% |
| 8 | SolarNet-CNN | profe (reto 4) | 10 | 256.7 | 17.4% | +1.7% |
| 9 | Persistencia | profe | 10 | 303.1 | 20.5% | — |
| 10 | Persistencia 3 días | profe (reto 1) | 10 | 313.9 | 21.3% | -19.4% |
| 11 | Persistencia × radiación | profe | 10 | 314.1 | 21.3% | -19.4% |

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
