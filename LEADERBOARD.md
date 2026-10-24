# ☀️ Liga de Pronóstico Solar Colombia — Leaderboard

_Actualizado: 2026-10-24 10:08 (hora Colombia) · Métrica: MAE en horas de sol (06–18 h) · Skill = 1 − MAE/MAE_persistencia (positivo = le ganas a la persistencia)_

## 🏆 Liga oficial (predicciones hechas ANTES de conocer el dato real)

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | SolarNet-Cuantiles (q50) | profe (reto 6) | 14 | 200.4 | 14.1% | +28.6% |
| 🥈 | SolarNet-Nubes | profe (reto 2) | 14 | 203.3 | 14.3% | +26.3% |
| 🥉 | SolarNet-Ponderada | profe (reto 3) | 14 | 203.9 | 14.3% | +30.2% |
| 4 | SolarNet-Ensamble×5 | profe (reto 5) | 14 | 207.2 | 14.5% | +27.2% |
| 5 | SolarNet-CNN | profe (reto 4) | 14 | 209.5 | 14.7% | +23.0% |
| 6 | SolarNet-Transformer | profe (reto 4) | 14 | 213.3 | 15.0% | +22.8% |
| 7 | SolarNet-GRU | profe | 14 | 215.1 | 15.1% | +25.2% |
| 8 | Persistencia × radiación | profe | 14 | 240.2 | 16.9% | +20.6% |
| 9 | Persistencia 3 días | profe (reto 1) | 14 | 299.0 | 21.0% | -6.0% |
| 10 | Persistencia | profe | 14 | 344.5 | 24.2% | — |

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
