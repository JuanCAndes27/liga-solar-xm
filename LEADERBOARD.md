# ☀️ Liga de Pronóstico Solar Colombia — Leaderboard

_Actualizado: 2026-11-04 14:14 (hora Colombia) · Métrica: MAE en horas de sol (06–18 h) · Skill = 1 − MAE/MAE_persistencia (positivo = le ganas a la persistencia)_

## 🏆 Liga oficial (predicciones hechas ANTES de conocer el dato real)

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | SolarNet-Cuantiles (q50) | profe (reto 6) | 25 | 213.7 | 14.6% | +34.4% |
| 🥈 | SolarNet-Nubes | profe (reto 2) | 25 | 215.3 | 14.8% | +33.0% |
| 🥉 | SolarNet-Ponderada | profe (reto 3) | 25 | 217.4 | 14.9% | +34.5% |
| 4 | SolarNet-CNN | profe (reto 4) | 25 | 219.4 | 15.0% | +30.5% |
| 5 | SolarNet-Ensamble×5 | profe (reto 5) | 25 | 219.5 | 15.0% | +33.0% |
| 6 | SolarNet-GRU | profe | 25 | 220.6 | 15.1% | +32.1% |
| 7 | SolarNet-Transformer | profe (reto 4) | 25 | 229.2 | 15.7% | +28.8% |
| 8 | Persistencia × radiación | profe | 25 | 257.0 | 17.6% | +26.2% |
| 9 | Persistencia 3 días | profe (reto 1) | 25 | 302.6 | 20.7% | +5.1% |
| 10 | Persistencia | profe | 25 | 393.2 | 26.9% | — |

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
