# ☀️ Liga de Pronóstico Solar Colombia — Leaderboard

_Actualizado: 2026-11-27 15:31 (hora Colombia) · Métrica: MAE en horas de sol (06–18 h) · Skill = 1 − MAE/MAE_persistencia (positivo = le ganas a la persistencia)_

## 🏆 Liga oficial (predicciones hechas ANTES de conocer el dato real)

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | SolarNet-Cuantiles (q50) | profe (reto 6) | 48 | 220.6 | 14.7% | +16.2% |
| 🥈 | SolarNet-Nubes | profe (reto 2) | 48 | 227.9 | 15.2% | +11.6% |
| 🥉 | SolarNet-CNN | profe (reto 4) | 48 | 230.1 | 15.3% | +6.9% |
| 4 | SolarNet-GRU | profe | 48 | 231.2 | 15.4% | +12.2% |
| 5 | SolarNet-Ensamble×5 | profe (reto 5) | 48 | 233.4 | 15.6% | +11.9% |
| 6 | SolarNet-Ponderada | profe (reto 3) | 48 | 235.9 | 15.7% | +11.6% |
| 7 | SolarNet-Transformer | profe (reto 4) | 48 | 242.0 | 16.1% | +8.1% |
| 8 | Persistencia × radiación | profe | 48 | 246.2 | 16.4% | +22.0% |
| 9 | Persistencia 3 días | profe (reto 1) | 48 | 306.0 | 20.4% | +4.2% |
| 10 | Persistencia | profe | 48 | 367.8 | 24.5% | — |

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
