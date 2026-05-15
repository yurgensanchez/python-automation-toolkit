from pathlib import Path

from automation_toolkit.file_tools import extension_folder_name, organize_by_extension


def test_extension_folder_name_uses_extension() -> None:
    assert extension_folder_name(Path("report.PDF")) == "pdf"


def test_extension_folder_name_handles_missing_extension() -> None:
    assert extension_folder_name(Path("README")) == "no_extension"


def test_organize_by_extension_dry_run_plans_moves_without_moving_files(tmp_path: Path) -> None:
    source_file = tmp_path / "report.txt"
    source_file.write_text("example", encoding="utf-8")

    moves = organize_by_extension(tmp_path, dry_run=True)

    assert moves == [(source_file.resolve(), tmp_path.resolve() / "txt" / "report.txt")]
    assert source_file.exists()


def test_organize_by_extension_moves_files(tmp_path: Path) -> None:
    source_file = tmp_path / "report.txt"
    source_file.write_text("example", encoding="utf-8")

    moves = organize_by_extension(tmp_path)

    destination = tmp_path / "txt" / "report.txt"
    assert moves == [(source_file.resolve(), destination.resolve())]
    assert destination.exists()
    assert not source_file.exists()
