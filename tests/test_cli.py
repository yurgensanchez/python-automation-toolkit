from pathlib import Path

import pandas as pd
from typer.testing import CliRunner

from automation_toolkit.cli import app

runner = CliRunner()


def test_clean_text_command_outputs_normalized_text() -> None:
    result = runner.invoke(app, ["clean-text", "  HELLO     From   Python  ", "--lowercase"])

    assert result.exit_code == 0
    assert "hello from python" in result.output


def test_github_repo_summary_command_outputs_summary(monkeypatch) -> None:
    def fake_fetch(owner: str, repo: str):
        from automation_toolkit.api_tools import GitHubRepoSummary

        assert owner == "python"
        assert repo == "cpython"
        return GitHubRepoSummary(
            full_name="python/cpython",
            description="The Python programming language",
            stars=70000,
            forks=30000,
            open_issues=9000,
            language="Python",
            url="https://github.com/python/cpython",
        )

    monkeypatch.setattr("automation_toolkit.cli.fetch_github_repo_summary", fake_fetch)

    result = runner.invoke(app, ["github-repo-summary", "python", "cpython"])

    assert result.exit_code == 0
    assert "Repository: python/cpython" in result.output
    assert "Stars: 70000" in result.output


def test_organize_files_dry_run_does_not_move_files(tmp_path: Path) -> None:
    source_file = tmp_path / "notes.txt"
    source_file.write_text("hello", encoding="utf-8")

    result = runner.invoke(app, ["organize-files", str(tmp_path), "--dry-run"])

    assert result.exit_code == 0
    assert "Planned moves" in result.output
    assert source_file.exists()
    assert not (tmp_path / "txt" / "notes.txt").exists()


def test_rename_files_dry_run_does_not_rename_files(tmp_path: Path) -> None:
    source_file = tmp_path / "notes.txt"
    source_file.write_text("hello", encoding="utf-8")

    result = runner.invoke(app, ["rename-files", str(tmp_path), "--prefix", "document", "--dry-run"])

    assert result.exit_code == 0
    assert "Planned renames" in result.output
    assert source_file.exists()
    assert not (tmp_path / "document_001.txt").exists()


def test_csv_to_excel_command_creates_workbook(tmp_path: Path) -> None:
    csv_file = tmp_path / "sales.csv"
    output_file = tmp_path / "sales.xlsx"
    csv_file.write_text("product,total\ncoffee,25\n", encoding="utf-8")

    result = runner.invoke(app, ["csv-to-excel", str(csv_file), "--output", str(output_file)])

    assert result.exit_code == 0
    assert "Excel file created" in result.output
    assert output_file.exists()
    dataframe = pd.read_excel(output_file)
    assert dataframe.to_dict(orient="records") == [{"product": "coffee", "total": 25}]


def test_csv_to_excel_command_accepts_delimiter_and_encoding(tmp_path: Path) -> None:
    csv_file = tmp_path / "sales.csv"
    output_file = tmp_path / "sales.xlsx"
    csv_file.write_text("product;total\ncoffee;25\n", encoding="latin-1")

    result = runner.invoke(
        app,
        [
            "csv-to-excel",
            str(csv_file),
            "--output",
            str(output_file),
            "--delimiter",
            ";",
            "--encoding",
            "latin-1",
        ],
    )

    assert result.exit_code == 0
    dataframe = pd.read_excel(output_file)
    assert dataframe.to_dict(orient="records") == [{"product": "coffee", "total": 25}]


def test_file_report_command_writes_markdown_report(tmp_path: Path) -> None:
    report_file = tmp_path / "report.md"
    (tmp_path / "notes.txt").write_text("hello", encoding="utf-8")
    (tmp_path / "sales.csv").write_text("product,total\ncoffee,25\n", encoding="utf-8")

    result = runner.invoke(app, ["file-report", str(tmp_path), "--output", str(report_file)])

    assert result.exit_code == 0
    assert "Report created" in result.output
    assert report_file.exists()

    report_text = report_file.read_text(encoding="utf-8")
    assert "# Directory Report" in report_text
    assert "| csv | 1 |" in report_text
    assert "| txt | 1 |" in report_text
