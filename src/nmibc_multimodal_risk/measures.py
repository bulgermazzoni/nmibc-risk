from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

import numpy as np
from sklearn.metrics import average_precision_score, brier_score_loss, roc_auc_score


@dataclass(frozen=True)
class BinaryMetrics:
    auroc: float
    auprc: float
    brier: float
    ece: float
    sensitivity_at_spec90: float


def as_arrays(
    y_true: list[int] | np.ndarray, y_score: list[float] | np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    y = np.asarray(y_true, dtype=int)
    s = np.asarray(y_score, dtype=float)
    if y.shape[0] != s.shape[0]:
        raise ValueError("labels and scores must have equal length")
    if y.ndim != 1 or s.ndim != 1:
        raise ValueError("labels and scores must be one-dimensional")
    return y, s


def auroc(y_true: list[int] | np.ndarray, y_score: list[float] | np.ndarray) -> float:
    y, s = as_arrays(y_true, y_score)
    if len(np.unique(y)) < 2:
        return float("nan")
    return float(roc_auc_score(y, s))


def auprc(y_true: list[int] | np.ndarray, y_score: list[float] | np.ndarray) -> float:
    y, s = as_arrays(y_true, y_score)
    if len(np.unique(y)) < 2:
        return float("nan")
    return float(average_precision_score(y, s))


def brier(y_true: list[int] | np.ndarray, y_score: list[float] | np.ndarray) -> float:
    y, s = as_arrays(y_true, y_score)
    return float(brier_score_loss(y, np.clip(s, 0.0, 1.0)))


def expected_calibration_error(
    y_true: list[int] | np.ndarray,
    y_score: list[float] | np.ndarray,
    bins: int = 10,
) -> float:
    y, s = as_arrays(y_true, y_score)
    edges = np.linspace(0.0, 1.0, bins + 1)
    total = 0.0
    for low, high in zip(edges[:-1], edges[1:]):
        mask = (s >= low) & (s < high if high < 1.0 else s <= high)
        if not np.any(mask):
            continue
        total += float(mask.mean() * abs(y[mask].mean() - s[mask].mean()))
    return total


def sensitivity_at_specificity(
    y_true: list[int] | np.ndarray,
    y_score: list[float] | np.ndarray,
    specificity: float = 0.9,
) -> float:
    y, s = as_arrays(y_true, y_score)
    thresholds = np.unique(s)
    best = 0.0
    for threshold in thresholds:
        pred = s >= threshold
        tn = np.sum((pred == 0) & (y == 0))
        fp = np.sum((pred == 1) & (y == 0))
        tp = np.sum((pred == 1) & (y == 1))
        fn = np.sum((pred == 0) & (y == 1))
        spec = tn / max(tn + fp, 1)
        sens = tp / max(tp + fn, 1)
        if spec >= specificity:
            best = max(best, float(sens))
    return best


def binary_metrics(
    y_true: list[int] | np.ndarray, y_score: list[float] | np.ndarray
) -> BinaryMetrics:
    return BinaryMetrics(
        auroc=auroc(y_true, y_score),
        auprc=auprc(y_true, y_score),
        brier=brier(y_true, y_score),
        ece=expected_calibration_error(y_true, y_score),
        sensitivity_at_spec90=sensitivity_at_specificity(y_true, y_score, 0.9),
    )


def bootstrap_interval(
    y_true: list[int] | np.ndarray,
    y_score: list[float] | np.ndarray,
    metric: Callable[[np.ndarray, np.ndarray], float],
    iterations: int = 1000,
    seed: int = 42,
) -> tuple[float, float, float]:
    y, s = as_arrays(y_true, y_score)
    rng = np.random.default_rng(seed)
    values: list[float] = []
    for _ in range(iterations):
        idx = rng.integers(0, y.shape[0], y.shape[0])
        if len(np.unique(y[idx])) < 2:
            continue
        values.append(float(metric(y[idx], s[idx])))
    center = float(metric(y, s))
    if not values:
        return center, float("nan"), float("nan")
    return center, float(np.percentile(values, 2.5)), float(np.percentile(values, 97.5))


def net_benefit(
    y_true: list[int] | np.ndarray, y_score: list[float] | np.ndarray, threshold: float
) -> float:
    y, s = as_arrays(y_true, y_score)
    pred = s >= threshold
    tp = np.sum((pred == 1) & (y == 1)) / y.shape[0]
    fp = np.sum((pred == 1) & (y == 0)) / y.shape[0]
    odds = threshold / max(1.0 - threshold, 1e-12)
    return float(tp - fp * odds)


def decision_curve(
    y_true: list[int] | np.ndarray, y_score: list[float] | np.ndarray, thresholds: list[float]
) -> dict[float, float]:
    return {threshold: net_benefit(y_true, y_score, threshold) for threshold in thresholds}


def categorical_nri(
    y_true: list[int] | np.ndarray,
    old_score: list[float] | np.ndarray,
    new_score: list[float] | np.ndarray,
    thresholds: tuple[float, float] = (0.15, 0.30),
) -> float:
    y, old = as_arrays(y_true, old_score)
    _, new = as_arrays(y_true, new_score)
    old_cat = np.digitize(old, thresholds)
    new_cat = np.digitize(new, thresholds)
    event = y == 1
    nonevent = y == 0
    event_up = np.mean(new_cat[event] > old_cat[event]) if np.any(event) else 0.0
    event_down = np.mean(new_cat[event] < old_cat[event]) if np.any(event) else 0.0
    nonevent_down = np.mean(new_cat[nonevent] < old_cat[nonevent]) if np.any(nonevent) else 0.0
    nonevent_up = np.mean(new_cat[nonevent] > old_cat[nonevent]) if np.any(nonevent) else 0.0
    return float((event_up - event_down) + (nonevent_down - nonevent_up))


def integrated_discrimination_improvement(
    y_true: list[int] | np.ndarray,
    old_score: list[float] | np.ndarray,
    new_score: list[float] | np.ndarray,
) -> float:
    y, old = as_arrays(y_true, old_score)
    _, new = as_arrays(y_true, new_score)
    event = y == 1
    nonevent = y == 0
    old_sep = old[event].mean() - old[nonevent].mean()
    new_sep = new[event].mean() - new[nonevent].mean()
    return float(new_sep - old_sep)
