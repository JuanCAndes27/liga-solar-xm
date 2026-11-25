# ☀️ Liga de Pronóstico Solar Colombia — Leaderboard

_Actualizado: 2026-11-25 15:54 (hora Colombia) · Métrica: MAE en horas de sol (06–18 h) · Skill = 1 − MAE/MAE_persistencia (positivo = le ganas a la persistencia)_

## 🏆 Liga oficial (predicciones hechas ANTES de conocer el dato real)

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | SolarNet-Cuantiles (q50) | profe (reto 6) | 46 | 224.6 | 15.0% | +15.7% |
| 🥈 | SolarNet-Nubes | profe (reto 2) | 46 | 231.4 | 15.5% | +11.1% |
| 🥉 | SolarNet-CNN | profe (reto 4) | 46 | 233.6 | 15.6% | +6.4% |
| 4 | SolarNet-GRU | profe | 46 | 234.6 | 15.7% | +12.0% |
| 5 | SolarNet-Ensamble×5 | profe (reto 5) | 46 | 235.7 | 15.8% | +12.2% |
| 6 | SolarNet-Ponderada | profe (reto 3) | 46 | 239.0 | 16.0% | +11.5% |
| 7 | SolarNet-Transformer | profe (reto 4) | 46 | 244.3 | 16.3% | +8.6% |
| 8 | Persistencia × radiación | profe | 46 | 250.5 | 16.7% | +22.0% |
| 9 | Persistencia 3 días | profe (reto 1) | 46 | 314.1 | 21.0% | +2.8% |
| 10 | Persistencia | profe | 46 | 375.2 | 25.1% | — |

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
