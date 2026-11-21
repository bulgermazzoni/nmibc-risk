from __future__ import annotations

import itertools

import torch
from torch import nn

PAIR_NAMES = (("pathology", "cystoscopy"), ("pathology", "molecular"), ("cystoscopy", "molecular"))


class PairCrossAttention(nn.Module):
    def __init__(self, embedding_dim: int, heads: int, dropout: float) -> None:
        super().__init__()
        self.attn = nn.MultiheadAttention(
            embed_dim=embedding_dim,
            num_heads=heads,
            dropout=dropout,
            batch_first=True,
        )
        self.norm = nn.LayerNorm(embedding_dim)
        self.ff = nn.Sequential(
            nn.Linear(embedding_dim, embedding_dim * 2),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(embedding_dim * 2, embedding_dim),
        )

    def forward(
        self, query: torch.Tensor, key: torch.Tensor, gate: torch.Tensor
    ) -> tuple[torch.Tensor, torch.Tensor]:
        q = query.unsqueeze(1)
        k = key.unsqueeze(1)
        attended, weights = self.attn(q, k, k, need_weights=True)
        gated = attended.squeeze(1) * gate.sigmoid()
        out = self.norm(query + gated)
        out = self.norm(out + self.ff(out))
        return out, weights.squeeze(1)


class ModalityBridge(nn.Module):
    def __init__(self, embedding_dim: int, heads: int, dropout: float) -> None:
        super().__init__()
        self.layers = nn.ModuleDict()
        self.gates = nn.ParameterDict()
        for a, b in PAIR_NAMES:
            self.layers[f"{a}_to_{b}"] = PairCrossAttention(embedding_dim, heads, dropout)
            self.layers[f"{b}_to_{a}"] = PairCrossAttention(embedding_dim, heads, dropout)
            self.gates[f"{a}_{b}"] = nn.Parameter(torch.zeros(embedding_dim))

    def forward(
        self,
        embeddings: dict[str, torch.Tensor],
        present: dict[str, torch.Tensor] | None = None,
    ) -> tuple[torch.Tensor, dict[str, torch.Tensor]]:
        pieces: list[torch.Tensor] = []
        attrs: dict[str, torch.Tensor] = {}
        for a, b in PAIR_NAMES:
            gate = self.gates[f"{a}_{b}"]
            if present is not None:
                mask = present[a].float().view(-1, 1) * present[b].float().view(-1, 1)
            else:
                mask = torch.ones(embeddings[a].shape[0], 1, device=embeddings[a].device)
            ab, wa = self.layers[f"{a}_to_{b}"](embeddings[a], embeddings[b], gate)
            ba, wb = self.layers[f"{b}_to_{a}"](embeddings[b], embeddings[a], gate)
            pieces.append(ab * mask)
            pieces.append(ba * mask)
            attrs[f"{a}_{b}"] = (
                (wa.mean(dim=-1) + wb.mean(dim=-1)) * gate.sigmoid().mean() * mask.squeeze(1)
            )
        for name in ("pathology", "cystoscopy", "molecular"):
            if present is None:
                pieces.append(embeddings[name])
            else:
                pieces.append(embeddings[name] * present[name].float().view(-1, 1))
        return torch.cat(pieces, dim=-1), attrs


def present_from_missing(
    batch_size: int, missing: set[str], device: torch.device
) -> dict[str, torch.Tensor]:
    return {
        name: torch.full((batch_size,), name not in missing, device=device)
        for name in itertools.chain(["pathology"], ["cystoscopy"], ["molecular"])
    }
