"""Piezas compartidas por las variantes de SolarNet (retos 2–6).

El archivo empieza por '_' así que la liga NO lo carga como modelo; los modelos lo importan.
Todo sigue la misma receta de SolarNet-GRU:
  1. armar un ejemplo por día: features de 24 horas → generación de 24 horas,
  2. usar el MISMO rezago que XM entre el día de referencia y el día objetivo,
  3. re-entrenar desde cero cada día (online learning) y predecir mañana.
"""
import numpy as np
import pandas as pd
import torch
from torch import nn

H = np.arange(24)


# ---------------------------------------------------------------- features
def _vecinos(v):
    """Valor de la hora anterior y de la siguiente (repite el borde en 0 h y 23 h)."""
    v = np.asarray(v, dtype=float)
    return np.r_[v[0], v[:-1]], np.r_[v[1:], v[-1]]


def features(gen_ref, clima_dia, escala, contexto_nubes=False):
    nub = clima_dia["nubosidad"].to_numpy() / 100
    cols = [
        gen_ref / escala,
        clima_dia["radiacion"].to_numpy() / 1000,
        nub,
        (clima_dia["temperatura"].to_numpy() - 25) / 10,
        np.sin(2 * np.pi * H / 24), np.cos(2 * np.pi * H / 24),
    ]
    if contexto_nubes:                      # Reto 2: nubosidad en h-1 y h+1
        antes, despues = _vecinos(nub)
        cols += [antes, despues]
    return np.column_stack(cols).astype(np.float32)


def dataset(historia, clima_dia, contexto_nubes=False):
    """Devuelve X (n,24,f), Y (n,24), x_mañana (1,24,f) y la escala (MWh)."""
    dias = {d: g.sort_values("fecha_hora") for d, g in historia.groupby(historia.fecha_hora.dt.date)
            if len(g) == 24}
    fechas = sorted(dias)
    objetivo = pd.Timestamp(clima_dia.fecha_hora.iloc[0]).date()
    rezago = pd.Timedelta(days=(objetivo - fechas[-1]).days).to_pytimedelta()
    escala = max(historia["solar_mwh"].max(), 1.0)

    X, Y = [], []
    for d in fechas:
        ref = d - rezago
        if ref in dias and dias[d]["radiacion"].notna().all():
            X.append(features(dias[ref]["solar_mwh"].to_numpy(), dias[d], escala, contexto_nubes))
            Y.append(dias[d]["solar_mwh"].to_numpy() / escala)
    x_man = features(dias[fechas[-1]]["solar_mwh"].to_numpy(), clima_dia.reset_index(drop=True),
                     escala, contexto_nubes)
    return (torch.tensor(np.array(X)), torch.tensor(np.array(Y), dtype=torch.float32),
            torch.tensor(x_man)[None], escala)


# ---------------------------------------------------------------- arquitecturas
class GRU(nn.Module):
    """La SolarNet original: GRU bidireccional + cabeza densa por hora."""
    def __init__(self, n_in, oculto=32, n_out=1):
        super().__init__()
        self.gru = nn.GRU(n_in, oculto, batch_first=True, bidirectional=True)
        self.cabeza = nn.Sequential(nn.Linear(2 * oculto, 16), nn.ReLU(), nn.Linear(16, n_out))

    def forward(self, x):
        z, _ = self.gru(x)
        return self.cabeza(z)               # (lote, 24, n_out)


class Transformer(nn.Module):
    """Reto 4a: encoder Transformer pequeño (1 capa, 2 cabezas).
    La atención deja que cada hora mire a TODAS las demás de una vez (no en secuencia como la GRU).
    La posición ya viene en las features (seno/coseno de la hora), y además sumamos un embedding
    aprendido por hora."""
    def __init__(self, n_in, d=32, cabezas=2, capas=1, n_out=1):
        super().__init__()
        self.entrada = nn.Linear(n_in, d)
        self.pos = nn.Parameter(torch.zeros(1, 24, d))
        capa = nn.TransformerEncoderLayer(d, cabezas, dim_feedforward=64, dropout=0.1,
                                          batch_first=True)
        self.encoder = nn.TransformerEncoder(capa, capas)
        self.cabeza = nn.Linear(d, n_out)

    def forward(self, x):
        return self.cabeza(self.encoder(self.entrada(x) + self.pos))


class CNN1D(nn.Module):
    """Reto 4b: convoluciones 1D sobre el eje de las horas.
    Con kernel 3 y dilataciones 1-2-4 cada salida ve ±7 horas de contexto."""
    def __init__(self, n_in, canales=32, n_out=1):
        super().__init__()
        capas, c = [], n_in
        for dil in (1, 2, 4):
            capas += [nn.Conv1d(c, canales, 3, padding=dil, dilation=dil), nn.ReLU()]
            c = canales
        self.red = nn.Sequential(*capas, nn.Conv1d(canales, n_out, 1))

    def forward(self, x):                   # Conv1d quiere (lote, canales, tiempo)
        return self.red(x.transpose(1, 2)).transpose(1, 2)


# ---------------------------------------------------------------- pérdidas
def mse(pred, y):
    return nn.functional.mse_loss(pred, y)


def pesos_por_hora(Y, piso=0.1):
    """Reto 3: peso de cada hora ∝ generación promedio a esa hora (el mediodía pesa más).
    El 'piso' evita que las horas de madrugada/atardecer queden con peso cero."""
    perfil = Y.mean(0)
    w = piso + perfil / perfil.max()
    return w / w.mean()                     # normalizado: mismo orden de magnitud que el MSE


def mse_ponderado(w):
    return lambda pred, y: (w * (pred - y) ** 2).mean()


CUANTILES = torch.tensor([0.1, 0.5, 0.9])


def pinball(pred, y, q=CUANTILES):
    """Reto 6: pérdida pinball (cuantílica). pred (lote,24,3), y (lote,24).
    Si el cuantil es 0.9, quedarse corto cuesta 0.9 y pasarse cuesta solo 0.1 → la red aprende
    a poner la predicción por encima del 90 % de los casos."""
    e = y.unsqueeze(-1) - pred
    return torch.maximum(q * e, (q - 1) * e).mean()


# ---------------------------------------------------------------- entrenamiento
def entrenar(red, X, Y, perdida=mse, salida=None, epocas=400, lr=5e-3, semilla=42):
    """Entrena con lote completo (≈90 días caben de una) y AdamW, como SolarNet-GRU.
    'salida' transforma la salida cruda de la red (por defecto softplus → generación ≥ 0).

    ¿Por qué softplus y no ReLU? Con ReLU a la salida, si la inicialización deja todas las salidas
    negativas, el gradiente es exactamente 0 y la red NUNCA aprende: predice 0 MWh siempre
    ('ReLU muerta'). Con SolarNet-GRU original le pasa a ~3 de cada 5 semillas. Softplus es una ReLU
    suave: también es ≥ 0, pero su gradiente nunca es cero."""
    torch.manual_seed(semilla)
    np.random.seed(semilla)
    salida = salida or positiva
    opt = torch.optim.AdamW(red.parameters(), lr=lr, weight_decay=1e-4)
    red.train()
    for _ in range(epocas):
        opt.zero_grad()
        perdida(salida(red(X)), Y).backward()
        opt.step()
    red.eval()
    return lambda x: salida(red(x))


def positiva(z):
    """Salida ≥ 0 sin ReLU muerta (beta alto ≈ ReLU, pero con gradiente siempre > 0)."""
    return nn.functional.softplus(z, beta=5).squeeze(-1)


def cuantiles_monotonos(z):
    """Convierte 3 salidas crudas en q10 ≤ q50 ≤ q90 (los cuantiles nunca se cruzan)."""
    q50 = nn.functional.softplus(z[..., 1], beta=5)
    q10 = torch.relu(q50 - nn.functional.softplus(z[..., 0]))
    q90 = q50 + nn.functional.softplus(z[..., 2])
    return torch.stack([q10, q50, q90], -1)


def predecir_con(arquitectura, historia, clima_dia, contexto_nubes=False, perdida=None,
                 semilla=42, epocas=400, lr=5e-3):
    """Atajo: arma datos, entrena una red y devuelve las 24 horas en MWh."""
    X, Y, x, escala = dataset(historia, clima_dia, contexto_nubes)
    red = arquitectura(X.shape[-1])
    f = entrenar(red, X, Y, perdida(Y) if perdida else mse, semilla=semilla, epocas=epocas, lr=lr)
    with torch.no_grad():
        return f(x)[0].numpy() * escala
