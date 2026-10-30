# ☀️ Liga de Pronóstico Solar Colombia — Leaderboard

_Actualizado: 2026-10-30 12:48 (hora Colombia) · Métrica: MAE en horas de sol (06–18 h) · Skill = 1 − MAE/MAE_persistencia (positivo = le ganas a la persistencia)_

## 🏆 Liga oficial (predicciones hechas ANTES de conocer el dato real)

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | Modelo LauraTamayo | LauraTamayo12 | 9 | 190.0 | 13.8% | +27.9% |
| 🥈 | SolarNet-GRU | profe | 9 | 226.4 | 16.5% | +16.4% |
| 🥉 | Persistencia × radiación | profe | 9 | 314.6 | 22.9% | -15.4% |
| 4 | Persistencia | profe | 9 | 347.4 | 25.3% | — |

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
