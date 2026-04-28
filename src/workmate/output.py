from __future__ import annotations

from tabulate import tabulate

from workmate.models import VideoMetric


def render_table(metrics: list[VideoMetric]) -> str:
    rows = [
        (
            metric.title,
            _format_number(metric.ctr),
            _format_number(metric.retention_rate),
        )
        for metric in metrics
    ]
    return tabulate(
        rows,
        headers=["title", "ctr", "retention_rate"],
        tablefmt="grid",
    )


def _format_number(value: float) -> str:
    if value.is_integer():
        return str(int(value))
    return f"{value:.1f}"
