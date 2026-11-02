# ☀️ Liga de Pronóstico Solar Colombia — Leaderboard

_Actualizado: 2026-11-02 15:58 (hora Colombia) · Métrica: MAE en horas de sol (06–18 h) · Skill = 1 − MAE/MAE_persistencia (positivo = le ganas a la persistencia)_

## 🏆 Liga oficial (predicciones hechas ANTES de conocer el dato real)

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | SolarNet-Cuantiles (q50) | profe (reto 6) | 24 | 213.3 | 14.8% | +25.2% |
| 🥈 | Rowan-SolarHybrid | rowanvrock96 | 23 | 214.4 | 14.8% | +27.6% |
| 🥉 | SolarNet-Ponderada | profe (reto 3) | 24 | 214.9 | 14.9% | +25.1% |
| 4 | SolarNet-Nubes | profe (reto 2) | 24 | 216.7 | 15.0% | +24.1% |
| 5 | SolarNet-Ensamble×5 | profe (reto 5) | 24 | 217.5 | 15.1% | +24.1% |
| 6 | SolarNet-GRU | profe | 24 | 222.3 | 15.4% | +21.6% |
| 7 | SolarNet-Transformer | profe (reto 4) | 24 | 222.7 | 15.5% | +21.9% |
| 8 | SolarNet-CNN | profe (reto 4) | 24 | 234.1 | 16.2% | +17.4% |
| 9 | Persistencia × radiación | profe | 24 | 263.9 | 18.3% | +8.8% |
| 10 | Persistencia 3 días | profe (reto 1) | 24 | 298.3 | 20.7% | -4.2% |
| 11 | Persistencia | profe | 24 | 339.6 | 23.6% | — |

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
