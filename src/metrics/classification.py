from __future__ import annotations

import numpy as np

from src.core.types import Array


def binary_accuracy(y_true: Array, y_pred: Array, threshold: float = 0.5) -> float:
    y_true = np.asarray(y_true, dtype=float)
    y_pred = np.asarray(y_pred, dtype=float)
    predicted = (y_pred >= threshold).astype(float)
    return float(np.mean(predicted == y_true))
