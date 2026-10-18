# ☀️ Liga de Pronóstico Solar Colombia — Leaderboard

_Actualizado: 2026-10-18 10:10 (hora Colombia) · Métrica: MAE en horas de sol (06–18 h) · Skill = 1 − MAE/MAE_persistencia (positivo = le ganas a la persistencia)_

## 🏆 Liga oficial (predicciones hechas ANTES de conocer el dato real)

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | SolarNet-Nubes | profe (reto 2) | 8 | 206.6 | 13.8% | +15.8% |
| 🥈 | SolarNet-Ponderada | profe (reto 3) | 8 | 212.6 | 14.2% | +21.3% |
| 🥉 | SolarNet-GRU | profe | 8 | 222.7 | 14.9% | +15.3% |
| 4 | SolarNet-Ensamble×5 | profe (reto 5) | 8 | 224.3 | 15.0% | +14.4% |
| 5 | SolarNet-Cuantiles (q50) | profe (reto 6) | 8 | 225.2 | 15.0% | +13.4% |
| 6 | SolarNet-CNN | profe (reto 4) | 8 | 244.6 | 16.3% | +1.3% |
| 7 | SolarNet-Transformer | profe (reto 4) | 8 | 247.1 | 16.5% | +4.3% |
| 8 | Persistencia × radiación | profe | 8 | 308.6 | 20.6% | -4.8% |
| 9 | Persistencia 3 días | profe (reto 1) | 8 | 319.3 | 21.3% | -17.1% |
| 10 | Persistencia | profe | 8 | 341.9 | 22.8% | — |

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
