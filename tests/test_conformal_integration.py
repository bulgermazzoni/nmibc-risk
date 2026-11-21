from __future__ import annotations

from nmibc_multimodal_risk.conformal import GroupConformalCalibrator


def test_group_conformal_coverage_keys() -> None:
    cal = GroupConformalCalibrator(0.9)
    probs = [0.05, 0.2, 0.8, 0.95, 0.3, 0.7]
    labels = [0, 0, 1, 1, 0, 1]
    groups = ["A", "A", "A", "B", "B", "B"]
    cal.fit(probs, labels, groups)
    coverage = cal.coverage(probs, labels, groups)
    assert set(coverage) == {"A", "B"}
    assert all(0.0 <= value <= 1.0 for value in coverage.values())
