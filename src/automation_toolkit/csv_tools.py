from __future__ import annotations

from pathlib import Path

import pandas as pd


def default_excel_path(csv_path: Path) -> Path:
    """Return the default Excel output path for a CSV file."""
    return csv_path.with_suffix(".xlsx")


def convert_csv_to_excel(csv_path: Path, output_path: Path | None = None) -> Path:
    """Convert a CSV file to an Excel workbook and return the output path."""
    csv_path = csv_path.expanduser().resolve()

    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file does not exist: {csv_path}")
    if not csv_path.is_file():
        raise IsADirectoryError(f"CSV path is not a file: {csv_path}")
    if csv_path.suffix.lower() != ".csv":
        raise ValueError(f"Expected a .csv file, got: {csv_path.name}")

    destination = (output_path or default_excel_path(csv_path)).expanduser().resolve()
    destination.parent.mkdir(parents=True, exist_ok=True)

    dataframe = pd.read_csv(csv_path)
    dataframe.to_excel(destination, index=False)

    return destination
