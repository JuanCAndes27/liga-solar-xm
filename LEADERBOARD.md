# ☀️ Liga de Pronóstico Solar Colombia — Leaderboard

_Actualizado: 2026-11-08 12:27 (hora Colombia) · Métrica: MAE en horas de sol (06–18 h) · Skill = 1 − MAE/MAE_persistencia (positivo = le ganas a la persistencia)_

## 🏆 Liga oficial (predicciones hechas ANTES de conocer el dato real)

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | SolarNet-CNN | profe (reto 4) | 29 | 248.5 | 17.1% | +20.4% |
| 🥈 | SolarNet-Cuantiles (q50) | profe (reto 6) | 29 | 249.3 | 17.2% | +24.8% |
| 🥉 | SolarNet-Nubes | profe (reto 2) | 29 | 254.8 | 17.6% | +22.1% |
| 4 | SolarNet-GRU | profe | 29 | 256.0 | 17.7% | +22.8% |
| 5 | SolarNet-Ensamble×5 | profe (reto 5) | 29 | 259.7 | 17.9% | +22.8% |
| 6 | SolarNet-Ponderada | profe (reto 3) | 29 | 261.4 | 18.0% | +24.3% |
| 7 | SolarNet-Transformer | profe (reto 4) | 29 | 270.4 | 18.6% | +17.9% |
| 8 | Persistencia × radiación | profe | 29 | 289.4 | 20.0% | +23.0% |
| 9 | Persistencia 3 días | profe (reto 1) | 29 | 347.4 | 24.0% | +6.0% |
| 10 | Persistencia | profe | 29 | 429.5 | 29.6% | — |

![último día](resultados/ultimo_dia.png)

## 🧪 Backtest (días pasados, para arrancar en frío)

_Ojo: en el backtest el 'pronóstico' de clima es casi el clima observado → resultados optimistas._

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | SolarNet-GRU | profe | 30 | 149.7 | 9.8% | +43.5% |
| 🥈 | SolarNet-Cuantiles (q50) | profe (reto 6) | 30 | 154.1 | 10.1% | +42.1% |
| 🥉 | SolarNet-Ensamble×5 | profe (reto 5) | 30 | 157.2 | 10.3% | +41.5% |
| 4 | SolarNet-Nubes | profe (reto 2) | 30 | 158.2 | 10.4% | +41.3% |
| 5 | SolarNet-Transformer | profe (reto 4) | 30 | 160.0 | 10.5% | +39.9% |
| 6 | SolarNet-Ponderada | profe (reto 3) | 30 | 171.0 | 11.2% | +37.7% |
| 7 | SolarNet-CNN | profe (reto 4) | 30 | 178.3 | 11.7% | +33.4% |
| 8 | Persistencia × radiación | profe | 30 | 217.0 | 14.2% | +22.4% |
| 9 | Persistencia 3 días | profe (reto 1) | 30 | 268.5 | 17.6% | +14.1% |
| 10 | Persistencia | profe | 30 | 319.4 | 20.9% | — |

![backtest](resultados/backtest.png)
