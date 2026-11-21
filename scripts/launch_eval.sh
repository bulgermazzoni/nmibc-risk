#!/usr/bin/env bash
set -euo pipefail
python -m nmibc_multimodal_risk.cli evaluate --config configs/primary.yaml --predictions outputs/predictions.csv
