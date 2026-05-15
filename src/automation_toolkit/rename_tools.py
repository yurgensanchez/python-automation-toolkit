from __future__ import annotations

import logging
from pathlib import Path

logger = logging.getLogger(__name__)


def build_numbered_name(prefix: str, index: int, original: Path, padding: int = 3) -> str:
    """Build a numbered filename while preserving the original extension."""
    return f"{prefix}_{index:0{padding}d}{original.suffix.lower()}"


def rename_files_by_pattern(
    source_dir: Path,
    prefix: str,
    start: int = 1,
    dry_run: bool = False,
) -> list[tuple[Path, Path]]:
    """Rename files in a directory using a numbered pattern."""
    source_dir = source_dir.expanduser().resolve()

    if not source_dir.exists():
        raise FileNotFoundError(f"Source directory does not exist: {source_dir}")
    if not source_dir.is_dir():
        raise NotADirectoryError(f"Source path is not a directory: {source_dir}")
    if not prefix.strip():
        raise ValueError("Prefix cannot be empty")

    files = [item for item in sorted(source_dir.iterdir()) if item.is_file()]
    planned_renames: list[tuple[Path, Path]] = []

    for offset, file_path in enumerate(files):
        new_name = build_numbered_name(prefix.strip(), start + offset, file_path)
        destination = file_path.with_name(new_name)

        if destination.exists() and destination.resolve() != file_path.resolve():
            raise FileExistsError(f"Destination already exists: {destination}")

        if file_path.resolve() == destination.resolve():
            continue

        planned_renames.append((file_path, destination))

        if dry_run:
            logger.info("Would rename %s -> %s", file_path, destination)
            continue

        file_path.rename(destination)
        logger.info("Renamed %s -> %s", file_path, destination)

    return planned_renames
