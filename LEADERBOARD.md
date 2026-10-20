# ☀️ Liga de Pronóstico Solar Colombia — Leaderboard

_Actualizado: 2026-10-20 11:06 (hora Colombia) · Métrica: MAE en horas de sol (06–18 h) · Skill = 1 − MAE/MAE_persistencia (positivo = le ganas a la persistencia)_

## 🏆 Liga oficial (predicciones hechas ANTES de conocer el dato real)

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | SolarNet-Nubes | profe (reto 2) | 10 | 198.2 | 13.3% | +24.4% |
| 🥈 | SolarNet-Ponderada | profe (reto 3) | 10 | 203.2 | 13.7% | +28.7% |
| 🥉 | SolarNet-Cuantiles (q50) | profe (reto 6) | 10 | 205.9 | 13.9% | +24.3% |
| 4 | SolarNet-GRU | profe | 10 | 206.5 | 13.9% | +25.2% |
| 5 | SolarNet-Ensamble×5 | profe (reto 5) | 10 | 211.9 | 14.3% | +23.3% |
| 6 | SolarNet-CNN | profe (reto 4) | 10 | 223.5 | 15.0% | +14.1% |
| 7 | SolarNet-Transformer | profe (reto 4) | 10 | 227.9 | 15.3% | +15.9% |
| 8 | Persistencia 3 días | profe (reto 1) | 10 | 288.8 | 19.4% | -2.0% |
| 9 | Persistencia × radiación | profe | 10 | 292.6 | 19.7% | +4.7% |
| 10 | Persistencia | profe | 10 | 353.2 | 23.8% | — |

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
