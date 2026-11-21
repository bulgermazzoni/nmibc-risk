from __future__ import annotations

import torch
from torch.utils.data import Dataset

from nmibc_multimodal_risk.typing import BatchDict


class SyntheticNMIBCDataset(Dataset[BatchDict]):
    def __init__(self, n: int, dim: int, seed: int = 42) -> None:
        generator = torch.Generator().manual_seed(seed)
        self.pathology = torch.randn(n, dim, generator=generator)
        self.cystoscopy = torch.randn(n, dim, generator=generator)
        self.molecular = torch.randn(n, dim, generator=generator)
        score = self.pathology[:, 0] * 1.4 + self.cystoscopy[:, 1] - self.molecular[:, 2] * 0.7
        score_prog = self.pathology[:, 2] * 1.1 + self.molecular[:, 1] * 0.9
        self.recurrence = (score > score.median()).float()
        self.progression = (score_prog > score_prog.median()).float()
        self.groups = {
            "sex": ["M" if i % 2 == 0 else "F" for i in range(n)],
            "age": ["lt65" if i % 3 else "ge65" for i in range(n)],
            "stage": [["Ta", "T1", "CIS"][i % 3] for i in range(n)],
            "grade": ["LG" if i % 4 else "HG" for i in range(n)],
        }

    def __len__(self) -> int:
        return int(self.recurrence.numel())

    def __getitem__(self, index: int) -> BatchDict:
        return {
            "pathology": self.pathology[index],
            "cystoscopy": self.cystoscopy[index],
            "molecular": self.molecular[index],
            "recurrence": self.recurrence[index],
            "progression": self.progression[index],
            "groups": {key: [value[index]] for key, value in self.groups.items()},
        }


def collate_nmibc(items: list[BatchDict]) -> BatchDict:
    groups: dict[str, list[str]] = {}
    for item in items:
        for key, value in item["groups"].items():
            groups.setdefault(key, []).extend(value)
    return {
        "pathology": torch.stack([item["pathology"] for item in items]),
        "cystoscopy": torch.stack([item["cystoscopy"] for item in items]),
        "molecular": torch.stack([item["molecular"] for item in items]),
        "recurrence": torch.stack([item["recurrence"] for item in items]),
        "progression": torch.stack([item["progression"] for item in items]),
        "groups": groups,
    }
