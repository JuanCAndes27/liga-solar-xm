# ☀️ Liga de Pronóstico Solar Colombia — Leaderboard

_Actualizado: 2026-10-27 12:39 (hora Colombia) · Métrica: MAE en horas de sol (06–18 h) · Skill = 1 − MAE/MAE_persistencia (positivo = le ganas a la persistencia)_

## 🏆 Liga oficial (predicciones hechas ANTES de conocer el dato real)

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | Modelo LauraTamayo | LauraTamayo12 | 8 | 182.8 | 13.2% | +24.5% |
| 🥈 | SolarNet-GRU | profe | 8 | 225.4 | 16.2% | +11.4% |
| 🥉 | Persistencia × radiación | profe | 8 | 314.5 | 22.7% | -22.6% |
| 4 | Persistencia | profe | 8 | 322.6 | 23.2% | — |

![último día](resultados/ultimo_dia.png)

## 🧪 Backtest (días pasados, para arrancar en frío)

_Ojo: en el backtest el 'pronóstico' de clima es casi el clima observado → resultados optimistas._

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | SolarNet-GRU | profe | 14 | 167.4 | 11.4% | +34.0% |
| 🥈 | Persistencia × radiación | profe | 14 | 231.5 | 15.8% | +16.3% |
| 🥉 | Modelo LauraTamayo | LauraTamayo12 | 14 | 237.5 | 16.2% | +26.2% |
| 4 | Persistencia | profe | 14 | 329.5 | 22.4% | — |

![backtest](resultados/backtest.png)
