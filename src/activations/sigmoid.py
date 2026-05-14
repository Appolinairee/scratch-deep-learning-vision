from __future__ import annotations

import numpy as np

from src.core.types import Array


def sigmoid(z: Array | float) -> Array | float:
    z = np.asarray(z, dtype=float)
    return 1.0 / (1.0 + np.exp(-z))
