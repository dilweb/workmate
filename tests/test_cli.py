from workmate.cli import main


def test_cli_prints_clickbait_report(capsys) -> None:
    exit_code = main(["--files", "stats1.csv", "stats2.csv", "--report", "clickbait"])

    captured = capsys.readouterr()

    assert exit_code == 0
    assert "Секрет который скрывают тимлиды" in captured.out
    assert "ctr" in captured.out
    assert "retention_rate" in captured.out
    assert "Почему я не использую ChatGPT на собесах" not in captured.out


def test_cli_fails_for_unknown_report() -> None:
    try:
        main(["--files", "stats1.csv", "--report", "unknown"])
    except SystemExit as error:
        assert error.code == 2
    else:
        raise AssertionError("CLI should exit for unknown report")
