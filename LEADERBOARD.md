# ☀️ Liga de Pronóstico Solar Colombia — Leaderboard

_Actualizado: 2026-10-15 07:19 (hora Colombia) · Métrica: MAE en horas de sol (06–18 h) · Skill = 1 − MAE/MAE_persistencia (positivo = le ganas a la persistencia)_

## 🏆 Liga oficial (predicciones hechas ANTES de conocer el dato real)

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | SolarNet-Ponderada | profe (reto 3) | 6 | 206.2 | 14.6% | +11.1% |
| 🥈 | SolarNet-Cuantiles (q50) | profe (reto 6) | 6 | 217.9 | 15.5% | +5.4% |
| 🥉 | Rowan-SolarHybrid | rowanvrock96 | 5 | 224.4 | 15.5% | +7.4% |
| 4 | SolarNet-Nubes | profe (reto 2) | 6 | 224.8 | 15.9% | +1.8% |
| 5 | SolarNet-GRU | profe | 6 | 224.8 | 15.9% | +3.3% |
| 6 | SolarNet-Ensamble×5 | profe (reto 5) | 6 | 229.3 | 16.3% | +2.8% |
| 7 | SolarNet-Transformer | profe (reto 4) | 6 | 230.4 | 16.3% | +1.1% |
| 8 | Persistencia | profe | 6 | 248.0 | 17.6% | — |
| 9 | SolarNet-CNN | profe (reto 4) | 6 | 268.2 | 19.0% | -11.5% |
| 10 | Persistencia 3 días | profe (reto 1) | 6 | 272.1 | 19.3% | -14.8% |
| 11 | Persistencia × radiación | profe | 6 | 332.2 | 23.6% | -45.1% |

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
