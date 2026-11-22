# ☀️ Liga de Pronóstico Solar Colombia — Leaderboard

_Actualizado: 2026-11-22 13:54 (hora Colombia) · Métrica: MAE en horas de sol (06–18 h) · Skill = 1 − MAE/MAE_persistencia (positivo = le ganas a la persistencia)_

## 🏆 Liga oficial (predicciones hechas ANTES de conocer el dato real)

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | SolarNet-Cuantiles (q50) | profe (reto 6) | 43 | 222.0 | 14.8% | +25.7% |
| 🥈 | SolarNet-Nubes | profe (reto 2) | 43 | 228.4 | 15.3% | +21.4% |
| 🥉 | SolarNet-CNN | profe (reto 4) | 43 | 229.8 | 15.4% | +18.0% |
| 4 | SolarNet-GRU | profe | 43 | 233.2 | 15.6% | +21.1% |
| 5 | SolarNet-Ensamble×5 | profe (reto 5) | 43 | 233.7 | 15.6% | +22.1% |
| 6 | SolarNet-Ponderada | profe (reto 3) | 43 | 236.7 | 15.8% | +22.0% |
| 7 | SolarNet-Transformer | profe (reto 4) | 43 | 242.7 | 16.2% | +18.1% |
| 8 | Persistencia × radiación | profe | 43 | 259.0 | 17.3% | +23.9% |
| 9 | Persistencia 3 días | profe (reto 1) | 43 | 328.1 | 21.9% | +4.9% |
| 10 | Persistencia | profe | 43 | 393.1 | 26.3% | — |

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
