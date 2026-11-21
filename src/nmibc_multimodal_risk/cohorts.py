from __future__ import annotations

import csv
import hashlib
from collections import Counter, defaultdict
from pathlib import Path
from typing import Iterable

from nmibc_multimodal_risk.typing import CohortRecord

REQUIRED_COLUMNS = {
    "patient_id",
    "cohort",
    "split",
    "recurrence_1y",
    "progression_1y",
    "cystoscopy_path",
    "pathology_path",
    "molecular_path",
}


def file_sha256(path: Path, block_size: int = 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while True:
            block = handle.read(block_size)
            if not block:
                break
            digest.update(block)
    return digest.hexdigest()


def read_manifest(path: Path) -> list[CohortRecord]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        names = set(reader.fieldnames or [])
        missing = REQUIRED_COLUMNS - names
        if missing:
            raise ValueError(f"manifest missing columns: {sorted(missing)}")
        records = []
        for row in reader:
            records.append(
                CohortRecord(
                    patient_id=str(row["patient_id"]),
                    cohort=str(row["cohort"]),
                    split=str(row["split"]),
                    recurrence_1y=int(row["recurrence_1y"]),
                    progression_1y=int(row["progression_1y"]),
                    cystoscopy_path=str(row["cystoscopy_path"]),
                    pathology_path=str(row["pathology_path"]),
                    molecular_path=str(row["molecular_path"]),
                    sex=str(row.get("sex", "unknown")),
                    age_group=str(row.get("age_group", "unknown")),
                    stage=str(row.get("stage", "unknown")),
                    grade=str(row.get("grade", "unknown")),
                    site=str(row.get("site", "unknown")),
                    equipment=str(row.get("equipment", "unknown")),
                    ethnicity_proxy=str(row.get("ethnicity_proxy", "unknown")),
                )
            )
        return records


def validate_unique_patients(records: Iterable[CohortRecord]) -> None:
    seen: set[str] = set()
    for record in records:
        if record.patient_id in seen:
            raise ValueError(f"duplicate patient id: {record.patient_id}")
        seen.add(record.patient_id)


def count_by(records: Iterable[CohortRecord], field: str) -> dict[str, int]:
    values = Counter(str(getattr(record, field)) for record in records)
    return dict(values)


def stratified_folds(records: list[CohortRecord], folds: int) -> list[list[CohortRecord]]:
    if folds < 1:
        raise ValueError("folds must be positive")
    buckets: dict[tuple[str, str, str], list[CohortRecord]] = defaultdict(list)
    for record in records:
        buckets[(record.cohort, record.grade, record.equipment)].append(record)
    output: list[list[CohortRecord]] = [[] for _ in range(folds)]
    for bucket in buckets.values():
        for index, record in enumerate(bucket):
            output[index % folds].append(record)
    return output


def manifest_summary(records: Iterable[CohortRecord]) -> dict[str, dict[str, int]]:
    rows = list(records)
    return {
        "cohort": count_by(rows, "cohort"),
        "split": count_by(rows, "split"),
        "stage": count_by(rows, "stage"),
        "grade": count_by(rows, "grade"),
        "equipment": count_by(rows, "equipment"),
    }
