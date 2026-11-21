from __future__ import annotations

import argparse
import json
from pathlib import Path

from nmibc_multimodal_risk.config import runtime_config
from nmibc_multimodal_risk.evaluation import (
    evaluate_predictions,
    load_prediction_csv,
    table_ready,
)
from nmibc_multimodal_risk.tgbrd import bootstrap_tgbrd, manuscript_axes
from nmibc_multimodal_risk.training import train_synthetic


def train_command(args: argparse.Namespace) -> None:
    config = runtime_config(args.config)
    summary = train_synthetic(config)
    payload = {"losses": summary.losses, "checkpoint": summary.checkpoint}
    config.output_dir.mkdir(parents=True, exist_ok=True)
    (config.output_dir / "train_summary.json").write_text(
        json.dumps(payload, indent=2), encoding="utf-8"
    )


def evaluate_command(args: argparse.Namespace) -> None:
    frame = load_prediction_csv(args.predictions)
    bundle = evaluate_predictions(frame, bootstrap=200)
    Path(args.output).write_text(json.dumps(table_ready(bundle), indent=2), encoding="utf-8")


def prepare_command(args: argparse.Namespace) -> None:
    schema = Path(args.schema).read_text(encoding="utf-8")
    sources = Path(args.sources).read_text(encoding="utf-8")
    count = len([line for line in sources.splitlines() if line.strip()])
    Path(args.output).write_text(
        json.dumps({"schema_bytes": len(schema), "sources": count}, indent=2),
        encoding="utf-8",
    )


def tgbrd_command(args: argparse.Namespace) -> None:
    axes, drops, deployment = manuscript_axes()
    result = bootstrap_tgbrd(axes, drops, deployment, iterations=args.iterations)
    payload = {
        "weights": result.weights,
        "bound": result.bound,
        "lower": result.lower,
        "upper": result.upper,
    }
    Path(args.output).write_text(json.dumps(payload, indent=2), encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="nmibc_multimodal_risk")
    sub = parser.add_subparsers(dest="command", required=True)
    train = sub.add_parser("train")
    train.add_argument("--config", required=True)
    train.set_defaults(func=train_command)
    evalp = sub.add_parser("evaluate")
    evalp.add_argument("--config", required=True)
    evalp.add_argument("--predictions", required=True)
    evalp.add_argument("--output", default="outputs/evaluation.json")
    evalp.set_defaults(func=evaluate_command)
    prep = sub.add_parser("prepare")
    prep.add_argument("--schema", required=True)
    prep.add_argument("--sources", required=True)
    prep.add_argument("--output", default="outputs/prepare_summary.json")
    prep.set_defaults(func=prepare_command)
    gap = sub.add_parser("tgbrd")
    gap.add_argument("--iterations", type=int, default=200)
    gap.add_argument("--output", default="outputs/tgbrd.json")
    gap.set_defaults(func=tgbrd_command)
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
