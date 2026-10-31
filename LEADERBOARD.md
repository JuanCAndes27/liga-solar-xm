# ☀️ Liga de Pronóstico Solar Colombia — Leaderboard

_Actualizado: 2026-10-31 11:37 (hora Colombia) · Métrica: MAE en horas de sol (06–18 h) · Skill = 1 − MAE/MAE_persistencia (positivo = le ganas a la persistencia)_

## 🏆 Liga oficial (predicciones hechas ANTES de conocer el dato real)

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | SolarNet-Cuantiles (q50) | profe (reto 6) | 21 | 215.7 | 15.1% | +33.8% |
| 🥈 | SolarNet-Nubes | profe (reto 2) | 21 | 216.4 | 15.1% | +32.9% |
| 🥉 | SolarNet-Ponderada | profe (reto 3) | 21 | 219.5 | 15.4% | +34.7% |
| 4 | SolarNet-GRU | profe | 21 | 220.8 | 15.5% | +32.4% |
| 5 | SolarNet-Ensamble×5 | profe (reto 5) | 21 | 221.4 | 15.5% | +32.9% |
| 6 | SolarNet-CNN | profe (reto 4) | 21 | 221.7 | 15.5% | +29.9% |
| 7 | SolarNet-Transformer | profe (reto 4) | 21 | 229.1 | 16.0% | +29.2% |
| 8 | Persistencia × radiación | profe | 21 | 256.4 | 17.9% | +26.3% |
| 9 | Persistencia 3 días | profe (reto 1) | 21 | 298.0 | 20.9% | +6.2% |
| 10 | Persistencia | profe | 21 | 391.9 | 27.4% | — |

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
