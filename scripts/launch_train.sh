#!/usr/bin/env bash
set -euo pipefail
torchrun --nproc_per_node=4 -m nmibc_multimodal_risk.cli train --config configs/primary.yaml
