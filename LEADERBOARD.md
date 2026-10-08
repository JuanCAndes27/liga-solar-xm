# ☀️ Liga de Pronóstico Solar Colombia — Leaderboard

_Actualizado: 2026-10-07 23:53 (hora Colombia) · Métrica: MAE en horas de sol (06–18 h) · Skill = 1 − MAE/MAE_persistencia (positivo = le ganas a la persistencia)_

## 🏆 Liga oficial (predicciones hechas ANTES de conocer el dato real)

_Aún no hay días calificados: XM publica con 1-2 días de rezago._

## 🧪 Backtest (días pasados, para arrancar en frío)

_Ojo: en el backtest el 'pronóstico' de clima es casi el clima observado → resultados optimistas._

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | SolarNet-GRU | profe | 14 | 170.2 | 11.8% | +34.8% |
| 🥈 | SolarNet-Cuantiles (q50) | profe (reto 6) | 14 | 183.1 | 12.7% | +32.4% |
| 🥉 | SolarNet-Nubes | profe (reto 2) | 14 | 189.6 | 13.1% | +29.8% |
| 4 | SolarNet-Transformer | profe (reto 4) | 14 | 196.4 | 13.6% | +26.4% |
| 5 | SolarNet-Ensamble×5 | profe (reto 5) | 14 | 199.3 | 13.8% | +25.8% |
| 6 | SolarNet-CNN | profe (reto 4) | 14 | 206.8 | 14.3% | +26.5% |
| 7 | SolarNet-Ponderada | profe (reto 3) | 14 | 208.8 | 14.5% | +24.6% |
| 8 | Rowan-SolarHybrid | rowanvrock96 | 14 | 210.4 | 14.6% | +18.7% |
| 9 | Persistencia × radiación | profe | 14 | 244.7 | 17.0% | +13.3% |
| 10 | Persistencia 3 días | profe (reto 1) | 14 | 298.8 | 20.7% | +10.5% |
| 11 | Persistencia | profe | 14 | 334.7 | 23.2% | — |

![backtest](resultados/backtest.png)
