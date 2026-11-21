from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal, TypedDict

import torch

ModalityName = Literal["pathology", "cystoscopy", "molecular"]
EndpointName = Literal["recurrence", "progression"]


class BatchDict(TypedDict):
    pathology: torch.Tensor
    cystoscopy: torch.Tensor
    molecular: torch.Tensor
    recurrence: torch.Tensor
    progression: torch.Tensor
    groups: dict[str, list[str]]


@dataclass(frozen=True)
class RuntimeConfig:
    seed: int
    batch_size: int
    learning_rate: float
    weight_decay: float
    max_steps: int
    embedding_dim: int
    hidden_dim: int
    heads: int
    dropout: float
    lambda_reconstruction: float
    lambda_conformal: float
    conformal_target: float
    grad_accum: int = 1
    clip_grad_norm: float = 1.0
    device: str = "cpu"
    precision: str = "fp32"
    output_dir: Path = Path("outputs")
    checkpoint_dir: Path = Path("checkpoints")
    seeds: tuple[int, ...] = (42,)
    folds: int = 1


@dataclass(frozen=True)
class CohortRecord:
    patient_id: str
    cohort: str
    split: str
    recurrence_1y: int
    progression_1y: int
    cystoscopy_path: str
    pathology_path: str
    molecular_path: str
    sex: str = "unknown"
    age_group: str = "unknown"
    stage: str = "unknown"
    grade: str = "unknown"
    site: str = "unknown"
    equipment: str = "unknown"
    ethnicity_proxy: str = "unknown"


@dataclass(frozen=True)
class MetricResult:
    name: str
    value: float
    lower: float | None = None
    upper: float | None = None
    n: int | None = None


@dataclass(frozen=True)
class PredictionFrame:
    recurrence_probability: list[float]
    progression_probability: list[float]
    recurrence_label: list[int]
    progression_label: list[int]
    strata: dict[str, list[str]] = field(default_factory=dict)


@dataclass(frozen=True)
class RiskOutput:
    recurrence: torch.Tensor
    progression: torch.Tensor
    reconstruction: torch.Tensor
    fused: torch.Tensor
    attribution: dict[str, torch.Tensor]
