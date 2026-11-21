from __future__ import annotations

import torch

from nmibc_multimodal_risk.architecture import NMIBCRiskModel
from nmibc_multimodal_risk.bridge import present_from_missing


def predict_with_missing(
    model: NMIBCRiskModel,
    pathology: torch.Tensor,
    cystoscopy: torch.Tensor,
    molecular: torch.Tensor,
    missing: set[str],
) -> tuple[torch.Tensor, torch.Tensor]:
    present = present_from_missing(pathology.shape[0], missing, pathology.device)
    return model.probabilities(pathology, cystoscopy, molecular, present)


def retention(clean_auc: float, missing_auc: float) -> float:
    if clean_auc == 0.0:
        return 0.0
    return float(missing_auc / clean_auc)
