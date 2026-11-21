from __future__ import annotations

import numpy as np


class BatchStandardizer:
    def __init__(self) -> None:
        self.location: dict[str, np.ndarray] = {}
        self.scale: dict[str, np.ndarray] = {}
        self.global_location: np.ndarray | None = None
        self.global_scale: np.ndarray | None = None

    def fit(self, x: np.ndarray, batches: list[str]) -> None:
        arr = np.asarray(x, dtype=float)
        self.global_location = arr.mean(axis=0)
        self.global_scale = arr.std(axis=0) + 1e-6
        for batch in sorted(set(batches)):
            mask = np.asarray(batches) == batch
            self.location[batch] = arr[mask].mean(axis=0)
            self.scale[batch] = arr[mask].std(axis=0) + 1e-6

    def transform(self, x: np.ndarray, batches: list[str]) -> np.ndarray:
        if self.global_location is None or self.global_scale is None:
            raise RuntimeError("standardizer is not fitted")
        arr = np.asarray(x, dtype=float)
        out = np.empty_like(arr)
        for index, batch in enumerate(batches):
            loc = self.location.get(batch, self.global_location)
            scale = self.scale.get(batch, self.global_scale)
            out[index] = (arr[index] - loc) / scale * self.global_scale + self.global_location
        return out


def maximum_mean_discrepancy(x: np.ndarray, y: np.ndarray, gamma: float | None = None) -> float:
    a = np.asarray(x, dtype=float)
    b = np.asarray(y, dtype=float)
    if gamma is None:
        gamma = 1.0 / max(a.shape[1], 1)
    kxx = np.exp(-gamma * ((a[:, None, :] - a[None, :, :]) ** 2).sum(axis=-1)).mean()
    kyy = np.exp(-gamma * ((b[:, None, :] - b[None, :, :]) ** 2).sum(axis=-1)).mean()
    kxy = np.exp(-gamma * ((a[:, None, :] - b[None, :, :]) ** 2).sum(axis=-1)).mean()
    return float(kxx + kyy - 2.0 * kxy)
