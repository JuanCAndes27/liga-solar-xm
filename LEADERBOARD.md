# ☀️ Liga de Pronóstico Solar Colombia — Leaderboard

_Actualizado: 2026-10-25 10:20 (hora Colombia) · Métrica: MAE en horas de sol (06–18 h) · Skill = 1 − MAE/MAE_persistencia (positivo = le ganas a la persistencia)_

## 🏆 Liga oficial (predicciones hechas ANTES de conocer el dato real)

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | SolarNet-Ponderada | profe (reto 3) | 15 | 198.7 | 13.8% | +32.7% |
| 🥈 | SolarNet-Cuantiles (q50) | profe (reto 6) | 15 | 198.8 | 13.8% | +30.2% |
| 🥉 | SolarNet-Nubes | profe (reto 2) | 15 | 199.5 | 13.9% | +28.6% |
| 4 | SolarNet-Ensamble×5 | profe (reto 5) | 15 | 202.1 | 14.0% | +29.7% |
| 5 | SolarNet-CNN | profe (reto 4) | 15 | 204.8 | 14.2% | +25.6% |
| 6 | SolarNet-GRU | profe | 15 | 209.5 | 14.6% | +27.9% |
| 7 | SolarNet-Transformer | profe (reto 4) | 15 | 210.0 | 14.6% | +25.0% |
| 8 | Persistencia × radiación | profe | 15 | 242.0 | 16.8% | +21.1% |
| 9 | Persistencia 3 días | profe (reto 1) | 15 | 295.4 | 20.5% | -3.3% |
| 10 | Persistencia | profe | 15 | 346.6 | 24.1% | — |

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
