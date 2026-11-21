from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import numpy as np
import torch
from torch.utils.data import DataLoader

from nmibc_multimodal_risk.architecture import NMIBCRiskModel
from nmibc_multimodal_risk.measures import (
    BinaryMetrics,
    binary_metrics,
    bootstrap_interval,
    decision_curve,
)
from nmibc_multimodal_risk.typing import PredictionFrame


@dataclass(frozen=True)
class EvaluationBundle:
    recurrence: BinaryMetrics
    progression: BinaryMetrics
    recurrence_ci: tuple[float, float, float]
    progression_ci: tuple[float, float, float]
    decision_curve: dict[float, float]


def collect_predictions(
    model: NMIBCRiskModel,
    loader: DataLoader[Any],
    device: str = "cpu",
) -> PredictionFrame:
    actual_device = torch.device(
        device if device == "cuda" and torch.cuda.is_available() else "cpu"
    )
    model.to(actual_device)
    model.eval()
    rec_scores: list[float] = []
    prog_scores: list[float] = []
    rec_labels: list[int] = []
    prog_labels: list[int] = []
    strata: dict[str, list[str]] = {}
    with torch.no_grad():
        for batch in loader:
            rec, prog = model.probabilities(
                batch["pathology"].to(actual_device),
                batch["cystoscopy"].to(actual_device),
                batch["molecular"].to(actual_device),
            )
            rec_scores.extend(float(x) for x in rec.cpu())
            prog_scores.extend(float(x) for x in prog.cpu())
            rec_labels.extend(int(x) for x in batch["recurrence"].cpu())
            prog_labels.extend(int(x) for x in batch["progression"].cpu())
            for key, values in batch["groups"].items():
                strata.setdefault(key, []).extend(values)
    return PredictionFrame(rec_scores, prog_scores, rec_labels, prog_labels, strata)


def evaluate_predictions(frame: PredictionFrame, bootstrap: int = 1000) -> EvaluationBundle:
    recurrence = binary_metrics(frame.recurrence_label, frame.recurrence_probability)
    progression = binary_metrics(frame.progression_label, frame.progression_probability)
    rec_ci = bootstrap_interval(
        frame.recurrence_label,
        frame.recurrence_probability,
        lambda y, s: binary_metrics(y, s).auroc,
        iterations=bootstrap,
    )
    prog_ci = bootstrap_interval(
        frame.progression_label,
        frame.progression_probability,
        lambda y, s: binary_metrics(y, s).auroc,
        iterations=bootstrap,
    )
    dca = decision_curve(
        frame.recurrence_label, frame.recurrence_probability, [0.05, 0.15, 0.30, 0.40]
    )
    return EvaluationBundle(recurrence, progression, rec_ci, prog_ci, dca)


def table_ready(bundle: EvaluationBundle) -> dict[str, float]:
    return {
        "recurrence_auroc": bundle.recurrence.auroc,
        "recurrence_auprc": bundle.recurrence.auprc,
        "recurrence_brier": bundle.recurrence.brier,
        "recurrence_ece": bundle.recurrence.ece,
        "progression_auroc": bundle.progression.auroc,
        "progression_auprc": bundle.progression.auprc,
        "progression_brier": bundle.progression.brier,
        "progression_ece": bundle.progression.ece,
        "dca_15": bundle.decision_curve[0.15],
        "dca_30": bundle.decision_curve[0.30],
    }


def load_prediction_csv(path: str) -> PredictionFrame:
    data = np.genfromtxt(path, delimiter=",", names=True, dtype=None, encoding="utf-8")
    return PredictionFrame(
        recurrence_probability=[float(x) for x in data["recurrence_probability"]],
        progression_probability=[float(x) for x in data["progression_probability"]],
        recurrence_label=[int(x) for x in data["recurrence_label"]],
        progression_label=[int(x) for x in data["progression_label"]],
        strata={},
    )
