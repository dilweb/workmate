from __future__ import annotations

import csv
from pathlib import Path
from typing import Iterable

from workmate.models import VideoMetric


def read_video_metrics(file_paths: Iterable[str]) -> list[VideoMetric]:
    metrics: list[VideoMetric] = []

    for file_path in file_paths:
        metrics.extend(_read_single_file(Path(file_path)))

    return metrics


def _read_single_file(file_path: Path) -> list[VideoMetric]:
    with file_path.open(newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        return [
            VideoMetric(
                title=row["title"],
                ctr=float(row["ctr"]),
                retention_rate=float(row["retention_rate"]),
            )
            for row in reader
        ]
