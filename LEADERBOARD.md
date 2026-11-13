# ☀️ Liga de Pronóstico Solar Colombia — Leaderboard

_Actualizado: 2026-11-13 14:01 (hora Colombia) · Métrica: MAE en horas de sol (06–18 h) · Skill = 1 − MAE/MAE_persistencia (positivo = le ganas a la persistencia)_

## 🏆 Liga oficial (predicciones hechas ANTES de conocer el dato real)

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | SolarNet-Cuantiles (q50) | profe (reto 6) | 34 | 236.4 | 16.0% | +29.1% |
| 🥈 | SolarNet-CNN | profe (reto 4) | 34 | 240.3 | 16.2% | +24.0% |
| 🥉 | SolarNet-Nubes | profe (reto 2) | 34 | 242.8 | 16.4% | +26.1% |
| 4 | SolarNet-GRU | profe | 34 | 246.9 | 16.7% | +25.8% |
| 5 | SolarNet-Ensamble×5 | profe (reto 5) | 34 | 249.0 | 16.8% | +26.2% |
| 6 | SolarNet-Ponderada | profe (reto 3) | 34 | 253.5 | 17.1% | +26.5% |
| 7 | SolarNet-Transformer | profe (reto 4) | 34 | 261.9 | 17.7% | +20.9% |
| 8 | Persistencia × radiación | profe | 34 | 279.7 | 18.9% | +25.6% |
| 9 | Persistencia 3 días | profe (reto 1) | 34 | 347.9 | 23.5% | +4.5% |
| 10 | Persistencia | profe | 34 | 419.5 | 28.3% | — |

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
