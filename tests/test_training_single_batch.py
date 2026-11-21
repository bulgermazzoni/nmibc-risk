from __future__ import annotations

import torch
from torch.utils.data import DataLoader

from nmibc_multimodal_risk.architecture import NMIBCRiskModel
from nmibc_multimodal_risk.config import runtime_config
from nmibc_multimodal_risk.synthetic import SyntheticNMIBCDataset, collate_nmibc
from nmibc_multimodal_risk.training import train_steps


def test_single_batch_training_runs_and_records_loss(tmp_path) -> None:
    config = runtime_config("configs/smoke.yaml")
    config = config.__class__(**{**config.__dict__, "checkpoint_dir": tmp_path, "max_steps": 3})
    dataset = SyntheticNMIBCDataset(n=16, dim=config.embedding_dim, seed=3)
    loader = DataLoader(dataset, batch_size=8, shuffle=False, collate_fn=collate_nmibc)
    model = NMIBCRiskModel(
        config.embedding_dim, config.embedding_dim, config.hidden_dim, config.heads, 0.0
    )
    summary = train_steps(model, loader, config, steps=3)
    assert len(summary.losses) == 3
    assert torch.isfinite(torch.tensor(summary.losses)).all()
    assert (tmp_path / "last.pt").exists()
