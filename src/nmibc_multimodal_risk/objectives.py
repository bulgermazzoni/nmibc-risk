from __future__ import annotations

from dataclasses import dataclass

import torch
from torch.nn import functional as F

from nmibc_multimodal_risk.typing import RiskOutput


@dataclass(frozen=True)
class LossBreakdown:
    total: torch.Tensor
    recurrence: torch.Tensor
    progression: torch.Tensor
    reconstruction: torch.Tensor
    conformal: torch.Tensor


def conformal_margin_loss(
    logits: torch.Tensor, labels: torch.Tensor, target: float
) -> torch.Tensor:
    probs = torch.sigmoid(logits)
    score = torch.where(labels > 0.5, 1.0 - probs, probs)
    excess = score - (1.0 - target)
    return torch.relu(excess).mean()


def risk_loss(
    output: RiskOutput,
    molecular_input: torch.Tensor,
    recurrence: torch.Tensor,
    progression: torch.Tensor,
    lambda_reconstruction: float,
    lambda_conformal: float,
    conformal_target: float,
) -> LossBreakdown:
    rec = F.binary_cross_entropy_with_logits(output.recurrence, recurrence.float())
    prog = F.binary_cross_entropy_with_logits(output.progression, progression.float())
    recon = F.mse_loss(output.reconstruction, molecular_input.float())
    conf = conformal_margin_loss(output.recurrence, recurrence.float(), conformal_target)
    total = rec + prog + lambda_reconstruction * recon + lambda_conformal * conf
    return LossBreakdown(
        total=total, recurrence=rec, progression=prog, reconstruction=recon, conformal=conf
    )


def class_weighted_bce(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    positives = labels.sum().clamp_min(1.0)
    negatives = (1.0 - labels).sum().clamp_min(1.0)
    pos_weight = negatives / positives
    return F.binary_cross_entropy_with_logits(logits, labels.float(), pos_weight=pos_weight)
