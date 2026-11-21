FROM pytorch/pytorch:2.4.0-cuda12.4-cudnn9-runtime
WORKDIR /workspace
COPY requirements.txt pyproject.toml ./
COPY src ./src
RUN pip install --no-cache-dir -r requirements.txt && pip install --no-cache-dir -e .
COPY configs ./configs
COPY scripts ./scripts
COPY manifests ./manifests
CMD ["python", "-m", "nmibc_multimodal_risk.cli", "train", "--config", "configs/smoke.yaml"]
