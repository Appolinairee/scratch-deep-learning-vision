from __future__ import annotations

import numpy as np

from src.core.types import Array


def bernoulli_nll(y: float, p: float, eps: float = 1e-12) -> float:
    p = float(np.clip(p, eps, 1.0 - eps))
    return float(-(y * np.log(p) + (1.0 - y) * np.log(1.0 - p)))


def dataset_binary_cross_entropy(y: Array, p: Array, eps: float = 1e-12) -> float:
    y = np.asarray(y, dtype=float)
    p = np.asarray(p, dtype=float)
    p = np.clip(p, eps, 1.0 - eps)
    loss = -(y * np.log(p) + (1.0 - y) * np.log(1.0 - p))
    return float(np.mean(loss))
