# ☀️ Liga de Pronóstico Solar Colombia — Leaderboard

_Actualizado: 2026-10-06 17:51 (hora Colombia) · Métrica: MAE en horas de sol (06–18 h) · Skill = 1 − MAE/MAE_persistencia (positivo = le ganas a la persistencia)_

## 🏆 Liga oficial (predicciones hechas ANTES de conocer el dato real)

_Aún no hay días calificados: XM publica con 1-2 días de rezago._

## 🧪 Backtest (días pasados, para arrancar en frío)

_Ojo: en el backtest el 'pronóstico' de clima es casi el clima observado → resultados optimistas._

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | SolarNet-Cuantiles (q50) | profe (reto 6) | 7 | 142.2 | 10.0% | +44.9% |
| 🥈 | SolarNet-Ensamble×5 | profe (reto 5) | 7 | 152.2 | 10.7% | +40.8% |
| 🥉 | SolarNet-GRU | profe | 7 | 154.5 | 10.8% | +40.1% |
| 4 | SolarNet-Nubes | profe (reto 2) | 7 | 158.3 | 11.1% | +40.1% |
| 5 | SolarNet-Transformer | profe (reto 4) | 7 | 158.6 | 11.1% | +38.9% |
| 6 | SolarNet-Ponderada | profe (reto 3) | 7 | 168.3 | 11.8% | +34.1% |
| 7 | SolarNet-CNN | profe (reto 4) | 7 | 170.6 | 12.0% | +34.6% |
| 8 | Persistencia × radiación | profe | 7 | 252.0 | 17.7% | +8.3% |
| 9 | Persistencia 3 días | profe (reto 1) | 7 | 316.3 | 22.2% | +4.7% |
| 10 | Persistencia | profe | 7 | 333.3 | 23.4% | — |

![backtest](resultados/backtest.png)
