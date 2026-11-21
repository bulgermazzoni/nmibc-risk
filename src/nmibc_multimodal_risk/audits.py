from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from nmibc_multimodal_risk.measures import (
    auroc,
    expected_calibration_error,
    sensitivity_at_specificity,
)


@dataclass(frozen=True)
class SubgroupRow:
    axis: str
    stratum: str
    n: int
    auroc: float
    ece: float


def subgroup_table(
    labels: list[int], scores: list[float], strata: dict[str, list[str]]
) -> list[SubgroupRow]:
    y = np.asarray(labels, dtype=int)
    s = np.asarray(scores, dtype=float)
    rows: list[SubgroupRow] = []
    for axis, values in strata.items():
        arr = np.asarray(values)
        for stratum in sorted(set(values)):
            mask = arr == stratum
            if mask.sum() < 2:
                continue
            rows.append(
                SubgroupRow(
                    axis=axis,
                    stratum=stratum,
                    n=int(mask.sum()),
                    auroc=auroc(y[mask], s[mask]),
                    ece=expected_calibration_error(y[mask], s[mask]),
                )
            )
    return rows


def max_axis_gap(rows: list[SubgroupRow]) -> dict[str, float]:
    result: dict[str, list[float]] = {}
    for row in rows:
        if np.isfinite(row.auroc):
            result.setdefault(row.axis, []).append(row.auroc)
    return {axis: float(max(values) - min(values)) for axis, values in result.items() if values}


def high_grade_error(
    labels: list[int], scores: list[float], grade: list[str], threshold: float = 0.3
) -> dict[str, float]:
    y = np.asarray(labels, dtype=int)
    s = np.asarray(scores, dtype=float)
    g = np.asarray(grade)
    mask = g == "HG"
    pred = s >= threshold
    fn = np.sum((pred == 0) & (y == 1) & mask)
    tp = np.sum((pred == 1) & (y == 1) & mask)
    fp = np.sum((pred == 1) & (y == 0) & mask)
    tn = np.sum((pred == 0) & (y == 0) & mask)
    return {"fnr": float(fn / max(fn + tp, 1)), "fpr": float(fp / max(fp + tn, 1))}


def reader_delta(
    labels: list[int], model: list[float], unaided: list[float], team: list[float]
) -> dict[str, float]:
    return {
        "model_auroc": auroc(labels, model),
        "unaided_auroc": auroc(labels, unaided),
        "team_auroc": auroc(labels, team),
        "team_sens_spec90": sensitivity_at_specificity(labels, team, 0.9),
    }
