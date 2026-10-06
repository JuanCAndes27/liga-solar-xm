"""Reto 5 — ¿El ensamble de 5 semillas reduce la varianza del error?

Experimento: entrenamos SolarNet-GRU con 15 semillas distintas.
  - 'Individual': el MAE de cada una de las 15 redes por separado.
  - 'Ensamble×5': agrupamos las 15 en 3 ensambles de 5 (semillas 0-4, 5-9, 10-14) y promediamos.
Si el ensamble funciona: (a) la desviación estándar del MAE entre ensambles es menor que entre redes
individuales (el resultado depende menos de la suerte de la inicialización) y (b) el MAE medio baja o
se mantiene.

Uso:  python -m experimentos.varianza_semillas            (datos sintéticos, ~5 min en CPU)
      python -m experimentos.varianza_semillas --real     (datos reales cacheados en datos/)
"""
import argparse

import numpy as np

from ._comun import cargar, dias_backtest, mae_sol
import _solarnet_comun as sn

N_SEMILLAS, TAM = 15, 5


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--real", action="store_true")
    ap.add_argument("--dias", type=int, default=5)
    a = ap.parse_args()
    hist, clima = cargar(a.real)

    mae_ind, mae_ens = [], []                     # filas = días
    for d, h, c, real in dias_backtest(hist, clima, a.dias):
        preds = np.array([sn.predecir_con(sn.GRU, h, c, semilla=s) for s in range(N_SEMILLAS)])
        ens = preds.reshape(N_SEMILLAS // TAM, TAM, 24).mean(1)
        mae_ind.append([mae_sol(p, real) for p in preds])
        mae_ens.append([mae_sol(p, real) for p in ens])
        print(f"{d}  individual: {np.mean(mae_ind[-1]):6.1f} ± {np.std(mae_ind[-1]):5.1f} MWh   "
              f"ensamble×5: {np.mean(mae_ens[-1]):6.1f} ± {np.std(mae_ens[-1]):5.1f} MWh")

    ind, ens = np.array(mae_ind), np.array(mae_ens)
    # Varianza 'por semilla': para cada día, dispersión entre redes; luego promediamos sobre días
    sd_ind, sd_ens = ind.std(1).mean(), ens.std(1).mean()
    print("\nResumen sobre", len(ind), "días")
    print(f"  MAE medio      individual {ind.mean():6.1f}   ensamble×5 {ens.mean():6.1f} MWh")
    print(f"  Desv. estándar individual {sd_ind:6.2f}   ensamble×5 {sd_ens:6.2f} MWh"
          f"   → reducción {1 - sd_ens / sd_ind:+.0%}")
    print("  (Teoría: si los errores de las semillas fueran independientes, la desviación bajaría"
          f" ×1/√{TAM} ≈ {1 - 1 / np.sqrt(TAM):.0%}. Bajar mucho menos indica errores correlacionados"
          " entre semillas: sesgo común que ningún ensamble quita. Ojo: con solo"
          f" {N_SEMILLAS // TAM} ensambles por día la desviación del ensamble es una estimación ruidosa.)")


if __name__ == "__main__":
    main()
