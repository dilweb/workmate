from __future__ import annotations

import argparse

from workmate.csv_reader import read_video_metrics
from workmate.output import render_table
from workmate.report_registry import build_report


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Generate reports for YouTube video metrics from CSV files."
    )
    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="One or more paths to CSV files with YouTube metrics.",
    )
    parser.add_argument(
        "--report",
        required=True,
        help="Report name to generate, for example: clickbait.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = create_parser()
    args = parser.parse_args(argv)

    try:
        report = build_report(args.report)
    except ValueError as error:
        parser.error(str(error))

    metrics = read_video_metrics(args.files)
    report_rows = report.generate(metrics)
    print(render_table(report_rows))
    return 0
