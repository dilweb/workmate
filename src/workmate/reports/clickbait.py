from workmate.models import VideoMetric
from workmate.reports.base import Report


class ClickbaitReport(Report):
    def generate(self, metrics: list[VideoMetric]) -> list[VideoMetric]:
        filtered_metrics = [
            metric
            for metric in metrics
            if metric.ctr > 15 and metric.retention_rate < 40
        ]
        return sorted(filtered_metrics, key=lambda metric: metric.ctr, reverse=True)
