from __future__ import annotations

import logging
import shutil
from pathlib import Path

logger = logging.getLogger(__name__)


def extension_folder_name(path: Path) -> str:
    """Return the destination folder name for a file extension."""
    suffix = path.suffix.lower().lstrip(".")
    return suffix if suffix else "no_extension"


def organize_by_extension(source_dir: Path, output_dir: Path | None = None, dry_run: bool = False) -> list[tuple[Path, Path]]:
    """Organize files from a directory into folders grouped by extension.

    The function only processes files directly inside ``source_dir``. It does
    not walk nested directories, which keeps the first version predictable.
    """
    source_dir = source_dir.expanduser().resolve()
    destination_root = (output_dir or source_dir).expanduser().resolve()

    if not source_dir.exists():
        raise FileNotFoundError(f"Source directory does not exist: {source_dir}")
    if not source_dir.is_dir():
        raise NotADirectoryError(f"Source path is not a directory: {source_dir}")

    planned_moves: list[tuple[Path, Path]] = []

    for item in sorted(source_dir.iterdir()):
        if not item.is_file():
            continue

        folder = destination_root / extension_folder_name(item)
        destination = folder / item.name

        if item.resolve() == destination.resolve():
            continue

        planned_moves.append((item, destination))

        if dry_run:
            logger.info("Would move %s -> %s", item, destination)
            continue

        folder.mkdir(parents=True, exist_ok=True)
        shutil.move(str(item), str(destination))
        logger.info("Moved %s -> %s", item, destination)

    return planned_moves
