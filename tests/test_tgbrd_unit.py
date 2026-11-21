from __future__ import annotations

import numpy as np

from nmibc_multimodal_risk.tgbrd import (
    AxisVector,
    bootstrap_tgbrd,
    fit_axis_weights,
    project_simplex,
)


def test_simplex_projection() -> None:
    out = project_simplex(np.asarray([0.7, 0.7, -1.0]))
    assert np.isclose(out.sum(), 1.0)
    assert np.all(out >= 0.0)


def test_tgbrd_fit_and_bootstrap() -> None:
    axes = [AxisVector(1, 2, 3, 4, 5), AxisVector(2, 1, 4, 3, 5), AxisVector(1, 1, 5, 4, 3)]
    drops = [3.5, 3.8, 3.3]
    weights = fit_axis_weights(axes, drops, steps=20)
    assert np.isclose(weights.sum(), 1.0)
    result = bootstrap_tgbrd(axes, drops, AxisVector(1, 2, 3, 4, 5), iterations=5)
    assert result.bound > 0.0
    assert len(result.weights) == 5
