# ☀️ Liga de Pronóstico Solar Colombia — Leaderboard

_Actualizado: 2026-10-28 12:43 (hora Colombia) · Métrica: MAE en horas de sol (06–18 h) · Skill = 1 − MAE/MAE_persistencia (positivo = le ganas a la persistencia)_

## 🏆 Liga oficial (predicciones hechas ANTES de conocer el dato real)

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | SolarNet-Cuantiles (q50) | profe (reto 6) | 17 | 216.3 | 15.2% | +27.5% |
| 🥈 | SolarNet-Nubes | profe (reto 2) | 17 | 219.0 | 15.3% | +25.7% |
| 🥉 | SolarNet-Ponderada | profe (reto 3) | 17 | 221.4 | 15.5% | +28.4% |
| 4 | SolarNet-Ensamble×5 | profe (reto 5) | 17 | 222.0 | 15.6% | +26.3% |
| 5 | SolarNet-CNN | profe (reto 4) | 17 | 225.5 | 15.8% | +22.4% |
| 6 | SolarNet-GRU | profe | 17 | 227.6 | 15.9% | +24.9% |
| 7 | SolarNet-Transformer | profe (reto 4) | 17 | 228.2 | 16.0% | +22.4% |
| 8 | Persistencia × radiación | profe | 17 | 252.2 | 17.7% | +20.1% |
| 9 | Persistencia 3 días | profe (reto 1) | 17 | 314.8 | 22.1% | -6.1% |
| 10 | Persistencia | profe | 17 | 350.2 | 24.5% | — |

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
