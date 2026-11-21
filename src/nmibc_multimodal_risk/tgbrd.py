from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class AxisVector:
    ground_truth: float
    prevalence: float
    domain: float
    workflow: float
    demographic: float

    def as_array(self) -> np.ndarray:
        return np.asarray(
            [self.ground_truth, self.prevalence, self.domain, self.workflow, self.demographic],
            dtype=float,
        )


@dataclass(frozen=True)
class TGBRDResult:
    weights: tuple[float, float, float, float, float]
    bound: float
    lower: float
    upper: float


def project_simplex(values: np.ndarray) -> np.ndarray:
    v = np.asarray(values, dtype=float)
    if v.ndim != 1:
        raise ValueError("values must be one-dimensional")
    u = np.sort(v)[::-1]
    cssv = np.cumsum(u) - 1
    ind = np.arange(1, v.size + 1)
    cond = u - cssv / ind > 0
    if not np.any(cond):
        return np.ones_like(v) / v.size
    rho = ind[cond][-1]
    theta = cssv[cond][-1] / rho
    return np.asarray(np.maximum(v - theta, 0.0), dtype=float)


def fit_axis_weights(
    axes: list[AxisVector], drops: list[float], steps: int = 1500, lr: float = 0.05
) -> np.ndarray:
    x = np.stack([axis.as_array() for axis in axes])
    y = np.asarray(drops, dtype=float)
    w = np.ones(5, dtype=float) / 5.0
    for _ in range(steps):
        grad = 2.0 * x.T @ (x @ w - y) / max(len(y), 1)
        w = project_simplex(w - lr * grad)
    return w


def prospective_bound(weights: np.ndarray, deployment_axis: AxisVector) -> float:
    return float(np.dot(weights, deployment_axis.as_array()))


def bootstrap_tgbrd(
    axes: list[AxisVector],
    drops: list[float],
    deployment_axis: AxisVector,
    iterations: int = 1000,
    seed: int = 42,
) -> TGBRDResult:
    rng = np.random.default_rng(seed)
    weights = fit_axis_weights(axes, drops)
    bound = prospective_bound(weights, deployment_axis)
    values: list[float] = []
    n = len(axes)
    for _ in range(iterations):
        idx = rng.integers(0, n, n)
        sample_axes = [axes[int(i)] for i in idx]
        sample_drops = [drops[int(i)] for i in idx]
        sample_weights = fit_axis_weights(sample_axes, sample_drops, steps=500)
        values.append(prospective_bound(sample_weights, deployment_axis))
    fitted = tuple(float(v) for v in weights)
    if len(fitted) != 5:
        raise ValueError("expected five TGBRD weights")
    return TGBRDResult(
        weights=(fitted[0], fitted[1], fitted[2], fitted[3], fitted[4]),
        bound=float(bound),
        lower=float(np.percentile(values, 2.5)),
        upper=float(np.percentile(values, 97.5)),
    )


def manuscript_axes() -> tuple[list[AxisVector], list[float], AxisVector]:
    axes = [
        AxisVector(3.5, 2.5, 8.0, 4.0, 3.5),
        AxisVector(2.5, 1.5, 10.0, 5.0, 4.0),
        AxisVector(2.0, 2.0, 6.0, 3.0, 3.0),
        AxisVector(3.0, 1.0, 5.0, 5.0, 4.0),
        AxisVector(3.2, 1.2, 5.4, 4.8, 3.8),
        AxisVector(2.8, 1.4, 4.8, 4.4, 4.2),
        AxisVector(3.4, 1.6, 5.8, 5.2, 3.6),
    ]
    drops = [5.03, 6.40, 3.50, 4.50, 4.70, 4.20, 4.90]
    deployment = AxisVector(3.0, 2.0, 8.0, 5.0, 4.0)
    return axes, drops, deployment
