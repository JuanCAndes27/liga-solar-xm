# ☀️ Liga de Pronóstico Solar Colombia — Leaderboard

_Actualizado: 2026-11-14 12:31 (hora Colombia) · Métrica: MAE en horas de sol (06–18 h) · Skill = 1 − MAE/MAE_persistencia (positivo = le ganas a la persistencia)_

## 🏆 Liga oficial (predicciones hechas ANTES de conocer el dato real)

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | SolarNet-Cuantiles (q50) | profe (reto 6) | 35 | 232.4 | 15.6% | +30.5% |
| 🥈 | SolarNet-CNN | profe (reto 4) | 35 | 236.2 | 15.9% | +25.6% |
| 🥉 | SolarNet-Nubes | profe (reto 2) | 35 | 238.8 | 16.0% | +27.6% |
| 4 | SolarNet-GRU | profe | 35 | 242.5 | 16.3% | +27.3% |
| 5 | SolarNet-Ensamble×5 | profe (reto 5) | 35 | 245.0 | 16.5% | +27.6% |
| 6 | SolarNet-Ponderada | profe (reto 3) | 35 | 249.1 | 16.7% | +27.9% |
| 7 | SolarNet-Transformer | profe (reto 4) | 35 | 257.2 | 17.3% | +22.6% |
| 8 | Persistencia × radiación | profe | 35 | 277.4 | 18.6% | +26.5% |
| 9 | Persistencia 3 días | profe (reto 1) | 35 | 343.3 | 23.1% | +6.0% |
| 10 | Persistencia | profe | 35 | 420.3 | 28.2% | — |

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
