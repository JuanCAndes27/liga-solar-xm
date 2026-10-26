# ☀️ Liga de Pronóstico Solar Colombia — Leaderboard

_Actualizado: 2026-10-26 12:47 (hora Colombia) · Métrica: MAE en horas de sol (06–18 h) · Skill = 1 − MAE/MAE_persistencia (positivo = le ganas a la persistencia)_

## 🏆 Liga oficial (predicciones hechas ANTES de conocer el dato real)

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | SolarNet-Cuantiles (q50) | profe (reto 6) | 17 | 192.3 | 13.2% | +30.4% |
| 🥈 | SolarNet-Ponderada | profe (reto 3) | 17 | 194.2 | 13.4% | +30.7% |
| 🥉 | SolarNet-Nubes | profe (reto 2) | 17 | 198.0 | 13.6% | +28.3% |
| 4 | SolarNet-Ensamble×5 | profe (reto 5) | 17 | 200.6 | 13.8% | +28.1% |
| 5 | Rowan-SolarHybrid | rowanvrock96 | 16 | 200.9 | 13.7% | +30.5% |
| 6 | SolarNet-GRU | profe | 17 | 203.3 | 14.0% | +27.0% |
| 7 | SolarNet-Transformer | profe (reto 4) | 17 | 204.6 | 14.1% | +25.7% |
| 8 | SolarNet-CNN | profe (reto 4) | 17 | 217.7 | 15.0% | +20.8% |
| 9 | Persistencia × radiación | profe | 17 | 253.3 | 17.5% | +7.8% |
| 10 | Persistencia 3 días | profe (reto 1) | 17 | 310.2 | 21.4% | -12.5% |
| 11 | Persistencia | profe | 17 | 316.5 | 21.8% | — |

![último día](resultados/ultimo_dia.png)

## 🧪 Backtest (días pasados, para arrancar en frío)

_Ojo: en el backtest el 'pronóstico' de clima es casi el clima observado → resultados optimistas._

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | SolarNet-GRU | profe | 14 | 170.3 | 11.8% | +34.8% |
| 🥈 | Rowan-SolarHybrid | rowanvrock96 | 14 | 171.8 | 11.9% | +33.3% |
| 🥉 | SolarNet-Cuantiles (q50) | profe (reto 6) | 14 | 183.2 | 12.7% | +32.4% |
| 4 | SolarNet-Nubes | profe (reto 2) | 14 | 187.4 | 13.0% | +30.5% |
| 5 | SolarNet-Ensamble×5 | profe (reto 5) | 14 | 193.7 | 13.4% | +27.6% |
| 6 | SolarNet-CNN | profe (reto 4) | 14 | 195.1 | 13.5% | +30.9% |
| 7 | SolarNet-Transformer | profe (reto 4) | 14 | 196.4 | 13.6% | +26.5% |
| 8 | SolarNet-Ponderada | profe (reto 3) | 14 | 212.4 | 14.7% | +23.6% |
| 9 | Persistencia × radiación | profe | 14 | 244.8 | 17.0% | +13.4% |
| 10 | Persistencia 3 días | profe (reto 1) | 14 | 298.8 | 20.7% | +10.6% |
| 11 | Persistencia | profe | 14 | 334.7 | 23.2% | — |

![backtest](resultados/backtest.png)
