from __future__ import annotations

import torch
from torch import nn


class FeatureAdapter(nn.Module):
    def __init__(self, input_dim: int, embedding_dim: int, hidden_dim: int, dropout: float) -> None:
        super().__init__()
        self.net = nn.Sequential(
            nn.LayerNorm(input_dim),
            nn.Linear(input_dim, hidden_dim),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim, embedding_dim),
            nn.LayerNorm(embedding_dim),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        out: torch.Tensor = self.net(x.float())
        return out


class MolecularReconstructor(nn.Module):
    def __init__(self, embedding_dim: int, output_dim: int, hidden_dim: int) -> None:
        super().__init__()
        self.decoder = nn.Sequential(
            nn.Linear(embedding_dim, hidden_dim),
            nn.GELU(),
            nn.Linear(hidden_dim, output_dim),
        )

    def forward(self, z: torch.Tensor) -> torch.Tensor:
        out: torch.Tensor = self.decoder(z)
        return out


class ModalityStem(nn.Module):
    def __init__(self, input_dim: int, embedding_dim: int, hidden_dim: int, dropout: float) -> None:
        super().__init__()
        self.pathology = FeatureAdapter(input_dim, embedding_dim, hidden_dim, dropout)
        self.cystoscopy = FeatureAdapter(input_dim, embedding_dim, hidden_dim, dropout)
        self.molecular = FeatureAdapter(input_dim, embedding_dim, hidden_dim, dropout)

    def forward(
        self,
        pathology: torch.Tensor,
        cystoscopy: torch.Tensor,
        molecular: torch.Tensor,
    ) -> dict[str, torch.Tensor]:
        return {
            "pathology": self.pathology(pathology),
            "cystoscopy": self.cystoscopy(cystoscopy),
            "molecular": self.molecular(molecular),
        }
