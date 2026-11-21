from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from nmibc_multimodal_risk.typing import RuntimeConfig


def read_yaml(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"configuration must be a mapping: {path}")
    if "extends" in data:
        parent = path.parent / str(data["extends"])
        merged = read_yaml(parent)
        merged.update({k: v for k, v in data.items() if k != "extends"})
        return merged
    return data


def runtime_config(path: str | Path) -> RuntimeConfig:
    data = read_yaml(Path(path))
    return RuntimeConfig(
        seed=int(data.get("seed", 42)),
        batch_size=int(data.get("batch_size", 32)),
        learning_rate=float(data.get("learning_rate", 5e-5)),
        weight_decay=float(data.get("weight_decay", 0.01)),
        max_steps=int(data.get("max_steps", 40000)),
        embedding_dim=int(data.get("embedding_dim", 64)),
        hidden_dim=int(data.get("hidden_dim", 128)),
        heads=int(data.get("heads", 4)),
        dropout=float(data.get("dropout", 0.1)),
        lambda_reconstruction=float(data.get("lambda_reconstruction", 0.1)),
        lambda_conformal=float(data.get("lambda_conformal", 0.02)),
        conformal_target=float(data.get("conformal_target", 0.9)),
        grad_accum=int(data.get("grad_accum", 1)),
        clip_grad_norm=float(data.get("clip_grad_norm", 1.0)),
        device=str(data.get("device", "cpu")),
        precision=str(data.get("precision", "fp32")),
        output_dir=Path(str(data.get("output_dir", "outputs"))),
        checkpoint_dir=Path(str(data.get("checkpoint_dir", "checkpoints"))),
        seeds=tuple(int(x) for x in data.get("seeds", [int(data.get("seed", 42))])),
        folds=int(data.get("folds", 1)),
    )


def write_yaml(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(payload, sort_keys=False), encoding="utf-8")
