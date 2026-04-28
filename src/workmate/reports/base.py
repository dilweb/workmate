from __future__ import annotations

from abc import ABC, abstractmethod

from workmate.models import VideoMetric


class Report(ABC):
    @abstractmethod
    def generate(self, metrics: list[VideoMetric]) -> list[VideoMetric]:
        raise NotImplementedError
