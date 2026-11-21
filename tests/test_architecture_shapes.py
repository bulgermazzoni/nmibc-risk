from __future__ import annotations

import torch

from nmibc_multimodal_risk.architecture import NMIBCRiskModel


def test_model_output_shapes() -> None:
    model = NMIBCRiskModel(input_dim=16, embedding_dim=16, hidden_dim=32, heads=2, dropout=0.0)
    x = torch.randn(5, 16)
    out = model(x, x, x)
    assert out.recurrence.shape == (5,)
    assert out.progression.shape == (5,)
    assert out.reconstruction.shape == (5, 16)
    assert out.fused.shape == (5, 144)
    assert sorted(out.attribution) == [
        "cystoscopy_molecular",
        "pathology_cystoscopy",
        "pathology_molecular",
    ]
