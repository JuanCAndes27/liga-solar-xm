# ☀️ Liga de Pronóstico Solar Colombia — Leaderboard

_Actualizado: 2026-11-14 12:45 (hora Colombia) · Métrica: MAE en horas de sol (06–18 h) · Skill = 1 − MAE/MAE_persistencia (positivo = le ganas a la persistencia)_

## 🏆 Liga oficial (predicciones hechas ANTES de conocer el dato real)

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | SolarNet-GRU | profe | 19 | 226.0 | 15.0% | +24.7% |
| 🥈 | Modelo LauraTamayo | LauraTamayo12 | 19 | 259.7 | 17.3% | +15.9% |
| 🥉 | Persistencia × radiación | profe | 19 | 289.3 | 19.2% | +5.2% |
| 4 | Persistencia | profe | 19 | 367.5 | 24.4% | — |

![último día](resultados/ultimo_dia.png)

## 🧪 Backtest (días pasados, para arrancar en frío)

_Ojo: en el backtest el 'pronóstico' de clima es casi el clima observado → resultados optimistas._

| # | Modelo | Autor | Días | MAE (MWh) | nMAE | Skill vs persistencia |
|---|---|---|---|---|---|---|
| 🥇 | SolarNet-GRU | profe | 14 | 167.4 | 11.4% | +34.0% |
| 🥈 | Persistencia × radiación | profe | 14 | 231.5 | 15.8% | +16.3% |
| 🥉 | Modelo LauraTamayo | LauraTamayo12 | 14 | 237.5 | 16.2% | +26.2% |
| 4 | Persistencia | profe | 14 | 329.4 | 22.4% | — |

![backtest](resultados/backtest.png)
