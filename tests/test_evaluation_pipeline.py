from __future__ import annotations

import torch
from torch.utils.data import DataLoader

from nmibc_multimodal_risk.architecture import NMIBCRiskModel
from nmibc_multimodal_risk.evaluation import (
    collect_predictions,
    evaluate_predictions,
    table_ready,
)
from nmibc_multimodal_risk.synthetic import SyntheticNMIBCDataset, collate_nmibc


def test_evaluation_bundle_has_table_values() -> None:
    dataset = SyntheticNMIBCDataset(n=20, dim=16, seed=9)
    loader = DataLoader(dataset, batch_size=5, collate_fn=collate_nmibc)
    model = NMIBCRiskModel(16, 16, 32, 2, 0.0)
    with torch.no_grad():
        frame = collect_predictions(model, loader)
    bundle = evaluate_predictions(frame, bootstrap=5)
    table = table_ready(bundle)
    assert "recurrence_auroc" in table
    assert "dca_15" in table
