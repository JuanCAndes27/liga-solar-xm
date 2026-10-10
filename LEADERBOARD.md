# ☀️ Liga de Pronóstico Solar Colombia — Leaderboard

_Actualizado: 2026-10-10 11:42 (hora Colombia) · Métrica: MAE en horas de sol (06–18 h) · Skill = 1 − MAE/MAE_persistencia (positivo = le ganas a la persistencia)_

## 🏆 Liga oficial (predicciones hechas ANTES de conocer el dato real)

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | SolarNet-Ponderada | profe (reto 3) | 2 | 142.3 | 10.5% | +34.9% |
| 🥈 | SolarNet-Ensamble×5 | profe (reto 5) | 2 | 177.7 | 13.1% | +19.1% |
| 🥉 | SolarNet-Cuantiles (q50) | profe (reto 6) | 2 | 179.2 | 13.2% | +18.3% |
| 4 | SolarNet-GRU | profe | 2 | 179.8 | 13.2% | +17.1% |
| 5 | SolarNet-Nubes | profe (reto 2) | 2 | 199.8 | 14.7% | +8.8% |
| 6 | SolarNet-Transformer | profe (reto 4) | 2 | 203.0 | 15.0% | +6.7% |
| 7 | Persistencia 3 días | profe (reto 1) | 2 | 209.7 | 15.5% | +9.0% |
| 8 | SolarNet-CNN | profe (reto 4) | 2 | 214.9 | 15.8% | +0.8% |
| 9 | Persistencia | profe | 2 | 226.0 | 16.7% | — |
| 10 | Persistencia × radiación | profe | 2 | 360.6 | 26.6% | -66.4% |

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
