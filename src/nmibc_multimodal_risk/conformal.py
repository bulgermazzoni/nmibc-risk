from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class ConformalSet:
    labels: tuple[str, ...]
    threshold: float
    score: float


class GroupConformalCalibrator:
    def __init__(self, target_coverage: float = 0.9) -> None:
        if not 0.0 < target_coverage < 1.0:
            raise ValueError("target_coverage must be in (0, 1)")
        self.target_coverage = target_coverage
        self.quantiles: dict[str, float] = {}
        self.global_quantile = 1.0

    def fit(self, probabilities: list[float], labels: list[int], groups: list[str]) -> None:
        p = np.asarray(probabilities, dtype=float)
        y = np.asarray(labels, dtype=int)
        scores = np.where(y == 1, 1.0 - p, p)
        self.global_quantile = float(np.quantile(scores, self.target_coverage, method="higher"))
        for group in sorted(set(groups)):
            mask = np.asarray(groups) == group
            if np.any(mask):
                self.quantiles[group] = float(
                    np.quantile(scores[mask], self.target_coverage, method="higher")
                )

    def predict_one(self, probability: float, group: str) -> ConformalSet:
        q = self.quantiles.get(group, self.global_quantile)
        labels: list[str] = []
        if probability <= q:
            labels.append("no_event")
        if 1.0 - probability <= q:
            labels.append("event")
        if not labels:
            labels = ["no_event", "event"]
        score = min(probability, 1.0 - probability)
        return ConformalSet(labels=tuple(labels), threshold=q, score=float(score))

    def coverage(
        self, probabilities: list[float], labels: list[int], groups: list[str]
    ) -> dict[str, float]:
        result: dict[str, list[float]] = {}
        for p, y, group in zip(probabilities, labels, groups):
            cset = self.predict_one(float(p), group)
            ok = (y == 1 and "event" in cset.labels) or (y == 0 and "no_event" in cset.labels)
            result.setdefault(group, []).append(float(ok))
        return {group: float(np.mean(values)) for group, values in result.items()}
