from pathlib import Path

from automation_toolkit.report_tools import build_directory_report, format_directory_report


def test_build_directory_report_counts_files_by_extension(tmp_path: Path) -> None:
    (tmp_path / "notes.txt").write_text("hello", encoding="utf-8")
    (tmp_path / "sales.csv").write_text("name,total\ncoffee,10\n", encoding="utf-8")
    (tmp_path / "README").write_text("docs", encoding="utf-8")
    (tmp_path / "nested").mkdir()

    report = build_directory_report(tmp_path)

    assert report.total_files == 3
    assert report.total_size_bytes > 0
    assert report.files_by_extension == {
        "csv": 1,
        "no_extension": 1,
        "txt": 1,
    }


def test_format_directory_report_outputs_markdown(tmp_path: Path) -> None:
    (tmp_path / "notes.txt").write_text("hello", encoding="utf-8")
    report = build_directory_report(tmp_path)

    formatted = format_directory_report(report)

    assert "# Directory Report" in formatted
    assert "| txt | 1 |" in formatted
    assert "Total files: 1" in formatted


def test_format_directory_report_handles_empty_directory(tmp_path: Path) -> None:
    report = build_directory_report(tmp_path)

    formatted = format_directory_report(report)

    assert "Total files: 0" in formatted
    assert "| none | 0 |" in formatted
