"""Reto 6 — ¿Los intervalos 10–90 de SolarNet-Cuantiles están bien calibrados?

Un intervalo 10–90 bien calibrado contiene el valor real ~80 % de las horas de sol.
  cobertura ≪ 80 %  → la red está sobreconfiada (intervalos muy angostos)
  cobertura ≫ 80 %  → intervalos demasiado anchos (poco útiles)
También reportamos el ancho medio del intervalo y la pérdida pinball, y guardamos una gráfica.

Uso:  python -m experimentos.cobertura_cuantiles [--real] [--dias 7]
"""
import argparse
import importlib.util

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

from ._comun import HORAS_SOL, RAIZ, cargar, dias_backtest, mae_sol  # noqa: E402


def _modelo():
    spec = importlib.util.spec_from_file_location("q", RAIZ / "modelos" / "solarnet_cuantiles.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--real", action="store_true")
    ap.add_argument("--dias", type=int, default=7)
    a = ap.parse_args()
    hist, clima = cargar(a.real)
    mod = _modelo()

    dentro, anchos, pin, maes, ultimo = [], [], [], [], None
    for d, h, c, real in dias_backtest(hist, clima, a.dias):
        q = mod.predecir_cuantiles(h, c)
        r, qs = real[HORAS_SOL], q[HORAS_SOL]
        dentro += list((r >= qs[:, 0]) & (r <= qs[:, 2]))
        anchos += list(qs[:, 2] - qs[:, 0])
        e = r[:, None] - qs
        tau = np.array([0.1, 0.5, 0.9])
        pin.append(np.maximum(tau * e, (tau - 1) * e).mean())
        maes.append(mae_sol(q[:, 1], real))
        print(f"{d}  MAE(q50) {maes[-1]:6.1f} MWh   cobertura 10–90: {np.mean(dentro[-13:]):.0%}")
        ultimo = (d, q, real)

    print(f"\nCobertura 10–90: {np.mean(dentro):.0%} (ideal 80 %) · ancho medio {np.mean(anchos):.0f} MWh"
          f" · pinball {np.mean(pin):.1f} · MAE(q50) {np.mean(maes):.1f} MWh")

    d, q, real = ultimo
    fig, ax = plt.subplots(figsize=(9, 4.2), dpi=120)
    ax.fill_between(range(24), q[:, 0], q[:, 2], color="#2A6F97", alpha=.2, label="Intervalo 10–90")
    ax.plot(range(24), q[:, 1], color="#2A6F97", lw=2, label="Mediana (q50)")
    ax.plot(range(24), real, color="#8A6D1F", lw=2, ls="--", label="Real")
    ax.set(title=f"SolarNet-Cuantiles — {d}", xlabel="Hora", ylabel="Generación solar SIN (MWh)", xlim=(4, 20))
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(frameon=False, fontsize=8)
    fig.tight_layout()
    (RAIZ / "resultados").mkdir(exist_ok=True)
    fig.savefig(RAIZ / "resultados" / "cuantiles.png")
    print("Gráfica: resultados/cuantiles.png")


if __name__ == "__main__":
    main()
