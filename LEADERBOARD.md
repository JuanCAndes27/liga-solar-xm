# ☀️ Liga de Pronóstico Solar Colombia — Leaderboard

_Actualizado: 2026-11-07 12:05 (hora Colombia) · Métrica: MAE en horas de sol (06–18 h) · Skill = 1 − MAE/MAE_persistencia (positivo = le ganas a la persistencia)_

## 🏆 Liga oficial (predicciones hechas ANTES de conocer el dato real)

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | SolarNet-Cuantiles (q50) | profe (reto 6) | 29 | 213.6 | 14.9% | +24.7% |
| 🥈 | Rowan-SolarHybrid | rowanvrock96 | 28 | 214.0 | 14.8% | +27.2% |
| 🥉 | SolarNet-Ensamble×5 | profe (reto 5) | 29 | 217.7 | 15.2% | +23.3% |
| 4 | SolarNet-Nubes | profe (reto 2) | 29 | 218.1 | 15.2% | +23.0% |
| 5 | SolarNet-GRU | profe | 29 | 220.3 | 15.3% | +22.1% |
| 6 | SolarNet-Transformer | profe (reto 4) | 29 | 223.0 | 15.5% | +20.3% |
| 7 | SolarNet-Ponderada | profe (reto 3) | 29 | 226.1 | 15.7% | +20.1% |
| 8 | SolarNet-CNN | profe (reto 4) | 29 | 229.3 | 16.0% | +18.9% |
| 9 | Persistencia × radiación | profe | 29 | 256.7 | 17.9% | +11.2% |
| 10 | Persistencia 3 días | profe (reto 1) | 29 | 292.3 | 20.4% | -1.0% |
| 11 | Persistencia | profe | 29 | 334.8 | 23.3% | — |

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
