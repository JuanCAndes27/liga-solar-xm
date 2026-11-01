# ☀️ Liga de Pronóstico Solar Colombia — Leaderboard

_Actualizado: 2026-11-01 12:28 (hora Colombia) · Métrica: MAE en horas de sol (06–18 h) · Skill = 1 − MAE/MAE_persistencia (positivo = le ganas a la persistencia)_

## 🏆 Liga oficial (predicciones hechas ANTES de conocer el dato real)

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | Persistencia × radiación | profe | 22 | 1459.7 | 50.9% | -3.8% |
| 🥈 | Persistencia 3 días | profe (reto 1) | 22 | 1467.6 | 51.2% | +0.5% |
| 🥉 | SolarNet-Ponderada | profe (reto 3) | 22 | 1468.1 | 51.2% | -5.6% |
| 4 | SolarNet-Ensamble×5 | profe (reto 5) | 22 | 1470.7 | 51.3% | -5.6% |
| 5 | SolarNet-Cuantiles (q50) | profe (reto 6) | 22 | 1470.9 | 51.3% | -6.2% |
| 6 | SolarNet-GRU | profe | 22 | 1471.9 | 51.3% | -6.1% |
| 7 | SolarNet-Nubes | profe (reto 2) | 22 | 1476.1 | 51.5% | -6.8% |
| 8 | SolarNet-Transformer | profe (reto 4) | 22 | 1483.3 | 51.7% | -7.2% |
| 9 | SolarNet-CNN | profe (reto 4) | 22 | 1490.5 | 52.0% | -7.7% |
| 10 | Persistencia | profe | 22 | 1525.8 | 53.2% | — |

![último día](resultados/ultimo_dia.png)

## 🧪 Backtest (días pasados, para arrancar en frío)

_Ojo: en el backtest el 'pronóstico' de clima es casi el clima observado → resultados optimistas._

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | SolarNet-GRU | profe | 30 | 267.2 | 16.1% | +33.1% |
| 🥈 | SolarNet-Cuantiles (q50) | profe (reto 6) | 30 | 273.3 | 16.5% | +31.6% |
| 🥉 | SolarNet-Transformer | profe (reto 4) | 30 | 273.6 | 16.5% | +30.1% |
| 4 | SolarNet-Ensamble×5 | profe (reto 5) | 30 | 275.1 | 16.6% | +31.2% |
| 5 | SolarNet-Nubes | profe (reto 2) | 30 | 278.6 | 16.8% | +30.4% |
| 6 | SolarNet-Ponderada | profe (reto 3) | 30 | 288.4 | 17.4% | +27.7% |
| 7 | SolarNet-CNN | profe (reto 4) | 30 | 289.9 | 17.5% | +24.5% |
| 8 | Persistencia × radiación | profe | 30 | 317.7 | 19.2% | +14.8% |
| 9 | Persistencia 3 días | profe (reto 1) | 30 | 335.0 | 20.2% | +12.7% |
| 10 | Persistencia | profe | 30 | 376.8 | 22.7% | — |

![backtest](resultados/backtest.png)
