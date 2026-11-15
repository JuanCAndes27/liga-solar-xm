# ☀️ Liga de Pronóstico Solar Colombia — Leaderboard

_Actualizado: 2026-11-15 13:18 (hora Colombia) · Métrica: MAE en horas de sol (06–18 h) · Skill = 1 − MAE/MAE_persistencia (positivo = le ganas a la persistencia)_

## 🏆 Liga oficial (predicciones hechas ANTES de conocer el dato real)

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | SolarNet-Cuantiles (q50) | profe (reto 6) | 36 | 234.6 | 15.7% | +30.0% |
| 🥈 | SolarNet-CNN | profe (reto 4) | 36 | 238.0 | 15.9% | +25.3% |
| 🥉 | SolarNet-Nubes | profe (reto 2) | 36 | 240.6 | 16.1% | +27.2% |
| 4 | SolarNet-GRU | profe | 36 | 244.4 | 16.3% | +26.9% |
| 5 | SolarNet-Ensamble×5 | profe (reto 5) | 36 | 247.1 | 16.5% | +27.1% |
| 6 | SolarNet-Ponderada | profe (reto 3) | 36 | 250.9 | 16.8% | +27.5% |
| 7 | SolarNet-Transformer | profe (reto 4) | 36 | 259.2 | 17.3% | +22.1% |
| 8 | Persistencia × radiación | profe | 36 | 278.9 | 18.6% | +25.9% |
| 9 | Persistencia 3 días | profe (reto 1) | 36 | 342.1 | 22.9% | +6.3% |
| 10 | Persistencia | profe | 36 | 418.5 | 28.0% | — |

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
