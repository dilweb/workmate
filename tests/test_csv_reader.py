from pathlib import Path

from workmate.csv_reader import read_video_metrics


def test_read_video_metrics_from_multiple_files() -> None:
    metrics = read_video_metrics(
        [str(Path("stats1.csv")), str(Path("stats2.csv"))]
    )

    assert len(metrics) == 20
    assert metrics[0].title == "Я бросил IT и стал фермером"
    assert metrics[-1].title == "Я попросил повышения и мне дали чай"
