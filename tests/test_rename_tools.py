from pathlib import Path

import pytest

from automation_toolkit.rename_tools import build_numbered_name, rename_files_by_pattern


def test_build_numbered_name_preserves_extension_in_lowercase() -> None:
    assert build_numbered_name("invoice", 7, Path("Report.PDF")) == "invoice_007.pdf"


def test_rename_files_by_pattern_dry_run_does_not_rename(tmp_path: Path) -> None:
    first = tmp_path / "a.txt"
    second = tmp_path / "b.csv"
    first.write_text("a", encoding="utf-8")
    second.write_text("b", encoding="utf-8")

    renames = rename_files_by_pattern(tmp_path, prefix="file", dry_run=True)

    assert renames == [
        (first.resolve(), tmp_path.resolve() / "file_001.txt"),
        (second.resolve(), tmp_path.resolve() / "file_002.csv"),
    ]
    assert first.exists()
    assert second.exists()


def test_rename_files_by_pattern_renames_files(tmp_path: Path) -> None:
    first = tmp_path / "a.txt"
    first.write_text("a", encoding="utf-8")

    renames = rename_files_by_pattern(tmp_path, prefix="note", start=5)

    destination = tmp_path / "note_005.txt"
    assert renames == [(first.resolve(), destination.resolve())]
    assert destination.exists()
    assert not first.exists()


def test_rename_files_by_pattern_rejects_empty_prefix(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="Prefix cannot be empty"):
        rename_files_by_pattern(tmp_path, prefix=" ")


def test_rename_files_by_pattern_rejects_existing_destination(tmp_path: Path) -> None:
    source = tmp_path / "a.txt"
    existing = tmp_path / "file_001.txt"
    source.write_text("a", encoding="utf-8")
    existing.write_text("existing", encoding="utf-8")

    with pytest.raises(FileExistsError, match="Destination already exists"):
        rename_files_by_pattern(tmp_path, prefix="file")
