from __future__ import annotations

from nmibc_multimodal_risk.measures import (
    binary_metrics,
    categorical_nri,
    decision_curve,
)


def test_metrics_known_values() -> None:
    labels = [0, 0, 1, 1]
    scores = [0.1, 0.4, 0.35, 0.9]
    metrics = binary_metrics(labels, scores)
    assert round(metrics.auroc, 3) == 0.750
    assert round(metrics.brier, 4) == 0.1506
    curve = decision_curve(labels, scores, [0.3])
    assert 0.3 in curve


def test_categorical_nri_direction() -> None:
    labels = [0, 0, 1, 1]
    old = [0.2, 0.4, 0.2, 0.4]
    new = [0.1, 0.2, 0.4, 0.8]
    assert categorical_nri(labels, old, new) > 0.0
