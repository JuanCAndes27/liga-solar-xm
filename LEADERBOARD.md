# ☀️ Liga de Pronóstico Solar Colombia — Leaderboard

_Actualizado: 2026-11-26 15:39 (hora Colombia) · Métrica: MAE en horas de sol (06–18 h) · Skill = 1 − MAE/MAE_persistencia (positivo = le ganas a la persistencia)_

## 🏆 Liga oficial (predicciones hechas ANTES de conocer el dato real)

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | SolarNet-Cuantiles (q50) | profe (reto 6) | 48 | 204.3 | 13.7% | +16.3% |
| 🥈 | SolarNet-Nubes | profe (reto 2) | 48 | 208.8 | 14.0% | +12.9% |
| 🥉 | Rowan-SolarHybrid | rowanvrock96 | 47 | 209.6 | 14.0% | +15.7% |
| 4 | SolarNet-GRU | profe | 48 | 210.1 | 14.1% | +14.0% |
| 5 | SolarNet-Ensamble×5 | profe (reto 5) | 48 | 210.8 | 14.1% | +12.3% |
| 6 | SolarNet-Ponderada | profe (reto 3) | 48 | 218.9 | 14.6% | +8.2% |
| 7 | SolarNet-Transformer | profe (reto 4) | 48 | 220.1 | 14.7% | +7.0% |
| 8 | SolarNet-CNN | profe (reto 4) | 48 | 223.7 | 15.0% | +6.4% |
| 9 | Persistencia × radiación | profe | 48 | 228.9 | 15.3% | +14.6% |
| 10 | Persistencia 3 días | profe (reto 1) | 48 | 274.9 | 18.4% | +2.7% |
| 11 | Persistencia | profe | 48 | 313.4 | 21.0% | — |

![último día](resultados/ultimo_dia.png)

## 🧪 Backtest (días pasados, para arrancar en frío)

_Ojo: en el backtest el 'pronóstico' de clima es casi el clima observado → resultados optimistas._

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | SolarNet-GRU | profe | 14 | 170.5 | 11.8% | +34.8% |
| 🥈 | Rowan-SolarHybrid | rowanvrock96 | 14 | 171.9 | 11.9% | +33.3% |
| 🥉 | SolarNet-Cuantiles (q50) | profe (reto 6) | 14 | 183.4 | 12.7% | +32.3% |
| 4 | SolarNet-Nubes | profe (reto 2) | 14 | 187.6 | 13.0% | +30.5% |
| 5 | SolarNet-Ensamble×5 | profe (reto 5) | 14 | 193.9 | 13.4% | +27.6% |
| 6 | SolarNet-CNN | profe (reto 4) | 14 | 195.3 | 13.5% | +30.9% |
| 7 | SolarNet-Transformer | profe (reto 4) | 14 | 196.6 | 13.6% | +26.5% |
| 8 | SolarNet-Ponderada | profe (reto 3) | 14 | 212.7 | 14.7% | +23.6% |
| 9 | Persistencia × radiación | profe | 14 | 244.9 | 17.0% | +13.4% |
| 10 | Persistencia 3 días | profe (reto 1) | 14 | 298.9 | 20.7% | +10.6% |
| 11 | Persistencia | profe | 14 | 334.9 | 23.2% | — |

![backtest](resultados/backtest.png)
