from __future__ import annotations

import logging
from pathlib import Path

import typer
from rich.console import Console
from rich.table import Table

from automation_toolkit.file_tools import organize_by_extension
from automation_toolkit.rename_tools import rename_files_by_pattern
from automation_toolkit.text_tools import clean_text

app = typer.Typer(help="Practical Python automation tools for files and text.")
console = Console()


def configure_logging(verbose: bool) -> None:
    level = logging.INFO if verbose else logging.WARNING
    logging.basicConfig(level=level, format="%(levelname)s: %(message)s")


@app.command("organize-files")
def organize_files(
    source: Path = typer.Argument(..., help="Directory containing files to organize."),
    output: Path | None = typer.Option(None, "--output", "-o", help="Optional output directory."),
    dry_run: bool = typer.Option(False, "--dry-run", help="Preview changes without moving files."),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Show detailed logs."),
) -> None:
    """Group files into folders by extension."""
    configure_logging(verbose)
    moves = organize_by_extension(source, output, dry_run=dry_run)

    if not moves:
        console.print("No files to organize.")
        raise typer.Exit()

    table = Table(title="Planned moves" if dry_run else "Moved files")
    table.add_column("Source")
    table.add_column("Destination")

    for original, destination in moves:
        table.add_row(str(original), str(destination))

    console.print(table)


@app.command("rename-files")
def rename_files(
    source: Path = typer.Argument(..., help="Directory containing files to rename."),
    prefix: str = typer.Option(..., "--prefix", "-p", help="Prefix for generated filenames."),
    start: int = typer.Option(1, "--start", "-s", help="Starting number for renamed files."),
    dry_run: bool = typer.Option(False, "--dry-run", help="Preview changes without renaming files."),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Show detailed logs."),
) -> None:
    """Rename files using a numbered pattern."""
    configure_logging(verbose)
    renames = rename_files_by_pattern(source, prefix=prefix, start=start, dry_run=dry_run)

    if not renames:
        console.print("No files to rename.")
        raise typer.Exit()

    table = Table(title="Planned renames" if dry_run else "Renamed files")
    table.add_column("Original")
    table.add_column("New name")

    for original, destination in renames:
        table.add_row(str(original), str(destination))

    console.print(table)


@app.command("clean-text")
def clean_text_command(
    text: str = typer.Argument(..., help="Text to clean."),
    lowercase: bool = typer.Option(False, "--lowercase", "-l", help="Convert text to lowercase."),
) -> None:
    """Trim text and collapse repeated whitespace."""
    console.print(clean_text(text, lowercase=lowercase))


if __name__ == "__main__":
    app()
