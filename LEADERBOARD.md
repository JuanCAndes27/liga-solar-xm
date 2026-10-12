# ☀️ Liga de Pronóstico Solar Colombia — Leaderboard

_Actualizado: 2026-10-12 15:40 (hora Colombia) · Métrica: MAE en horas de sol (06–18 h) · Skill = 1 − MAE/MAE_persistencia (positivo = le ganas a la persistencia)_

## 🏆 Liga oficial (predicciones hechas ANTES de conocer el dato real)

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | SolarNet-Ponderada | profe (reto 3) | 3 | 164.9 | 11.2% | +3.6% |
| 🥈 | Persistencia | profe | 3 | 194.8 | 13.2% | — |
| 🥉 | SolarNet-GRU | profe | 3 | 199.2 | 13.5% | -15.3% |
| 4 | SolarNet-Ensamble×5 | profe (reto 5) | 3 | 203.0 | 13.8% | -17.9% |
| 5 | SolarNet-Cuantiles (q50) | profe (reto 6) | 3 | 204.9 | 13.9% | -19.0% |
| 6 | SolarNet-Nubes | profe (reto 2) | 3 | 220.8 | 15.0% | -27.0% |
| 7 | SolarNet-Transformer | profe (reto 4) | 3 | 225.5 | 15.3% | -30.4% |
| 8 | SolarNet-CNN | profe (reto 4) | 3 | 240.7 | 16.4% | -39.8% |
| 9 | Persistencia 3 días | profe (reto 1) | 3 | 247.8 | 16.8% | -42.3% |
| 10 | Persistencia × radiación | profe | 3 | 286.6 | 19.5% | -45.9% |

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
