from workmate.models import VideoMetric
from workmate.reports.clickbait import ClickbaitReport


def test_clickbait_report_filters_and_sorts_metrics() -> None:
    metrics = [
        VideoMetric(title="A", ctr=16.0, retention_rate=39.0),
        VideoMetric(title="B", ctr=25.0, retention_rate=22.0),
        VideoMetric(title="C", ctr=30.0, retention_rate=45.0),
        VideoMetric(title="D", ctr=10.0, retention_rate=10.0),
    ]

    report = ClickbaitReport()

    result = report.generate(metrics)

    assert [metric.title for metric in result] == ["B", "A"]
