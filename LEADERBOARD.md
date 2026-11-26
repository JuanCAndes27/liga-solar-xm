# ☀️ Liga de Pronóstico Solar Colombia — Leaderboard

_Actualizado: 2026-11-26 15:45 (hora Colombia) · Métrica: MAE en horas de sol (06–18 h) · Skill = 1 − MAE/MAE_persistencia (positivo = le ganas a la persistencia)_

## 🏆 Liga oficial (predicciones hechas ANTES de conocer el dato real)

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | SolarNet-Cuantiles (q50) | profe (reto 6) | 47 | 222.2 | 14.8% | +16.5% |
| 🥈 | SolarNet-Nubes | profe (reto 2) | 47 | 230.0 | 15.3% | +11.6% |
| 🥉 | SolarNet-CNN | profe (reto 4) | 47 | 231.7 | 15.5% | +7.2% |
| 4 | SolarNet-GRU | profe | 47 | 232.7 | 15.5% | +12.6% |
| 5 | SolarNet-Ensamble×5 | profe (reto 5) | 47 | 234.8 | 15.7% | +12.4% |
| 6 | SolarNet-Ponderada | profe (reto 3) | 47 | 237.6 | 15.9% | +11.9% |
| 7 | SolarNet-Transformer | profe (reto 4) | 47 | 242.9 | 16.2% | +9.0% |
| 8 | Persistencia × radiación | profe | 47 | 248.2 | 16.6% | +22.5% |
| 9 | Persistencia 3 días | profe (reto 1) | 47 | 310.0 | 20.7% | +3.8% |
| 10 | Persistencia | profe | 47 | 372.5 | 24.8% | — |

![último día](resultados/ultimo_dia.png)

## 🧪 Backtest (días pasados, para arrancar en frío)

_Ojo: en el backtest el 'pronóstico' de clima es casi el clima observado → resultados optimistas._

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | SolarNet-GRU | profe | 30 | 149.8 | 9.8% | +43.5% |
| 🥈 | SolarNet-Cuantiles (q50) | profe (reto 6) | 30 | 154.2 | 10.1% | +42.1% |
| 🥉 | SolarNet-Ensamble×5 | profe (reto 5) | 30 | 157.2 | 10.3% | +41.5% |
| 4 | SolarNet-Nubes | profe (reto 2) | 30 | 158.3 | 10.4% | +41.2% |
| 5 | SolarNet-Transformer | profe (reto 4) | 30 | 160.1 | 10.5% | +39.9% |
| 6 | SolarNet-Ponderada | profe (reto 3) | 30 | 171.0 | 11.2% | +37.7% |
| 7 | SolarNet-CNN | profe (reto 4) | 30 | 178.4 | 11.7% | +33.3% |
| 8 | Persistencia × radiación | profe | 30 | 217.0 | 14.2% | +22.4% |
| 9 | Persistencia 3 días | profe (reto 1) | 30 | 268.5 | 17.6% | +14.1% |
| 10 | Persistencia | profe | 30 | 319.4 | 20.9% | — |

![backtest](resultados/backtest.png)
