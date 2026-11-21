from __future__ import annotations

import torch
from torch import nn

from nmibc_multimodal_risk.bridge import ModalityBridge
from nmibc_multimodal_risk.encoders import ModalityStem, MolecularReconstructor
from nmibc_multimodal_risk.typing import RiskOutput


class RiskHead(nn.Module):
    def __init__(self, input_dim: int, hidden_dim: int, dropout: float) -> None:
        super().__init__()
        self.net = nn.Sequential(
            nn.LayerNorm(input_dim),
            nn.Linear(input_dim, hidden_dim),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim, hidden_dim // 2),
            nn.GELU(),
        )
        self.recurrence = nn.Linear(hidden_dim // 2, 1)
        self.progression = nn.Linear(hidden_dim // 2, 1)

    def forward(self, x: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
        h = self.net(x)
        return self.recurrence(h).squeeze(-1), self.progression(h).squeeze(-1)


class NMIBCRiskModel(nn.Module):
    def __init__(
        self, input_dim: int, embedding_dim: int, hidden_dim: int, heads: int, dropout: float
    ) -> None:
        super().__init__()
        self.stem = ModalityStem(input_dim, embedding_dim, hidden_dim, dropout)
        self.bridge = ModalityBridge(embedding_dim, heads, dropout)
        self.reconstructor = MolecularReconstructor(embedding_dim, input_dim, hidden_dim)
        self.head = RiskHead(embedding_dim * 9, hidden_dim, dropout)

    def forward(
        self,
        pathology: torch.Tensor,
        cystoscopy: torch.Tensor,
        molecular: torch.Tensor,
        present: dict[str, torch.Tensor] | None = None,
    ) -> RiskOutput:
        embeddings = self.stem(pathology, cystoscopy, molecular)
        fused, attr = self.bridge(embeddings, present)
        rec, prog = self.head(fused)
        recon = self.reconstructor(embeddings["molecular"])
        return RiskOutput(
            recurrence=rec, progression=prog, reconstruction=recon, fused=fused, attribution=attr
        )

    def probabilities(
        self,
        pathology: torch.Tensor,
        cystoscopy: torch.Tensor,
        molecular: torch.Tensor,
        present: dict[str, torch.Tensor] | None = None,
    ) -> tuple[torch.Tensor, torch.Tensor]:
        out = self.forward(pathology, cystoscopy, molecular, present)
        return torch.sigmoid(out.recurrence), torch.sigmoid(out.progression)
