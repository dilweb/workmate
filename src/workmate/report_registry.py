from workmate.reports.base import Report
from workmate.reports.clickbait import ClickbaitReport


REPORTS: dict[str, type[Report]] = {
    "clickbait": ClickbaitReport,
}


def build_report(report_name: str) -> Report:
    try:
        report_class = REPORTS[report_name]
    except KeyError as error:
        supported_reports = ", ".join(sorted(REPORTS))
        raise ValueError(
            f"Unknown report '{report_name}'. Supported reports: {supported_reports}"
        ) from error

    return report_class()
