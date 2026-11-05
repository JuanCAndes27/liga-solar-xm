# ☀️ Liga de Pronóstico Solar Colombia — Leaderboard

_Actualizado: 2026-11-05 14:17 (hora Colombia) · Métrica: MAE en horas de sol (06–18 h) · Skill = 1 − MAE/MAE_persistencia (positivo = le ganas a la persistencia)_

## 🏆 Liga oficial (predicciones hechas ANTES de conocer el dato real)

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | SolarNet-CNN | profe (reto 4) | 26 | 239.4 | 16.5% | +31.6% |
| 🥈 | SolarNet-Cuantiles (q50) | profe (reto 6) | 26 | 242.5 | 16.7% | +34.8% |
| 🥉 | SolarNet-Nubes | profe (reto 2) | 26 | 246.4 | 16.9% | +33.4% |
| 4 | SolarNet-GRU | profe | 26 | 252.2 | 17.3% | +32.5% |
| 5 | SolarNet-Ensamble×5 | profe (reto 5) | 26 | 253.7 | 17.5% | +33.2% |
| 6 | SolarNet-Ponderada | profe (reto 3) | 26 | 255.1 | 17.5% | +34.5% |
| 7 | SolarNet-Transformer | profe (reto 4) | 26 | 266.2 | 18.3% | +29.0% |
| 8 | Persistencia × radiación | profe | 26 | 297.4 | 20.5% | +26.2% |
| 9 | Persistencia 3 días | profe (reto 1) | 26 | 355.6 | 24.5% | +5.1% |
| 10 | Persistencia | profe | 26 | 447.0 | 30.7% | — |

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
