#!/usr/bin/env bash
set -euo pipefail
python -m nmibc_multimodal_risk.cli prepare --schema manifests/schema.json --sources dataset_sources.txt
