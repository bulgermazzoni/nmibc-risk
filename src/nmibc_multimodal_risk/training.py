from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import torch
from torch import nn
from torch.optim import AdamW
from torch.utils.data import DataLoader

from nmibc_multimodal_risk.architecture import NMIBCRiskModel
from nmibc_multimodal_risk.checkpointing import save_checkpoint
from nmibc_multimodal_risk.objectives import risk_loss
from nmibc_multimodal_risk.randomness import set_seed
from nmibc_multimodal_risk.synthetic import SyntheticNMIBCDataset, collate_nmibc
from nmibc_multimodal_risk.typing import RuntimeConfig


@dataclass(frozen=True)
class TrainSummary:
    losses: list[float]
    checkpoint: str | None


def make_model(config: RuntimeConfig, input_dim: int | None = None) -> NMIBCRiskModel:
    dim = int(input_dim or config.embedding_dim)
    return NMIBCRiskModel(
        input_dim=dim,
        embedding_dim=config.embedding_dim,
        hidden_dim=config.hidden_dim,
        heads=config.heads,
        dropout=config.dropout,
    )


def optimizer_for(model: nn.Module, config: RuntimeConfig) -> AdamW:
    return AdamW(model.parameters(), lr=config.learning_rate, weight_decay=config.weight_decay)


def train_steps(
    model: NMIBCRiskModel,
    loader: DataLoader[Any],
    config: RuntimeConfig,
    steps: int | None = None,
) -> TrainSummary:
    set_seed(config.seed)
    device = torch.device(
        config.device if config.device == "cuda" and torch.cuda.is_available() else "cpu"
    )
    model.to(device)
    model.train()
    opt = optimizer_for(model, config)
    max_steps = int(steps or config.max_steps)
    losses: list[float] = []
    iterator = iter(loader)
    for step in range(max_steps):
        try:
            batch = next(iterator)
        except StopIteration:
            iterator = iter(loader)
            batch = next(iterator)
        pathology = batch["pathology"].to(device)
        cystoscopy = batch["cystoscopy"].to(device)
        molecular = batch["molecular"].to(device)
        recurrence = batch["recurrence"].to(device)
        progression = batch["progression"].to(device)
        output = model(pathology, cystoscopy, molecular)
        loss = risk_loss(
            output,
            molecular,
            recurrence,
            progression,
            config.lambda_reconstruction,
            config.lambda_conformal,
            config.conformal_target,
        )
        torch.autograd.backward(loss.total)
        torch.nn.utils.clip_grad_norm_(model.parameters(), config.clip_grad_norm)
        opt.step()
        opt.zero_grad(set_to_none=True)
        losses.append(float(loss.total.detach().cpu()))
    checkpoint_path = config.checkpoint_dir / "last.pt"
    save_checkpoint(
        checkpoint_path,
        {
            "model": model.state_dict(),
            "seed": config.seed,
            "losses": losses,
            "config": config.__dict__,
        },
    )
    return TrainSummary(losses=losses, checkpoint=str(checkpoint_path))


def train_synthetic(config: RuntimeConfig) -> TrainSummary:
    dataset = SyntheticNMIBCDataset(
        n=max(config.batch_size * 4, 32), dim=config.embedding_dim, seed=config.seed
    )
    loader = DataLoader(
        dataset, batch_size=config.batch_size, shuffle=True, collate_fn=collate_nmibc
    )
    model = make_model(config, input_dim=config.embedding_dim)
    return train_steps(model, loader, config)
