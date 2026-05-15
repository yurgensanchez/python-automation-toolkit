from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from pathlib import Path

from automation_toolkit.file_tools import extension_folder_name


@dataclass(frozen=True)
class DirectoryReport:
    source: Path
    total_files: int
    total_size_bytes: int
    files_by_extension: dict[str, int]


def build_directory_report(source_dir: Path) -> DirectoryReport:
    """Build a simple report for files directly inside a directory."""
    source_dir = source_dir.expanduser().resolve()

    if not source_dir.exists():
        raise FileNotFoundError(f"Source directory does not exist: {source_dir}")
    if not source_dir.is_dir():
        raise NotADirectoryError(f"Source path is not a directory: {source_dir}")

    files = [item for item in sorted(source_dir.iterdir()) if item.is_file()]
    counts = Counter(extension_folder_name(file_path) for file_path in files)
    total_size = sum(file_path.stat().st_size for file_path in files)

    return DirectoryReport(
        source=source_dir,
        total_files=len(files),
        total_size_bytes=total_size,
        files_by_extension=dict(sorted(counts.items())),
    )


def format_directory_report(report: DirectoryReport) -> str:
    """Format a directory report as Markdown."""
    lines = [
        "# Directory Report",
        "",
        f"Source: `{report.source}`",
        f"Total files: {report.total_files}",
        f"Total size: {report.total_size_bytes} bytes",
        "",
        "## Files by Extension",
        "",
        "| Extension | Files |",
        "| --- | ---: |",
    ]

    if not report.files_by_extension:
        lines.append("| none | 0 |")
    else:
        for extension, count in report.files_by_extension.items():
            lines.append(f"| {extension} | {count} |")

    return "\n".join(lines) + "\n"
