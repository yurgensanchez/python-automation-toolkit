from pathlib import Path

import pandas as pd
import pytest

from automation_toolkit.csv_tools import convert_csv_to_excel, default_excel_path


def test_default_excel_path_replaces_csv_suffix() -> None:
    assert default_excel_path(Path("report.csv")) == Path("report.xlsx")


def test_convert_csv_to_excel_creates_workbook(tmp_path: Path) -> None:
    csv_file = tmp_path / "sales.csv"
    csv_file.write_text("product,total\ncoffee,25\ntea,15\n", encoding="utf-8")

    output = convert_csv_to_excel(csv_file)

    assert output == tmp_path / "sales.xlsx"
    assert output.exists()

    dataframe = pd.read_excel(output)
    assert list(dataframe.columns) == ["product", "total"]
    assert dataframe.to_dict(orient="records") == [
        {"product": "coffee", "total": 25},
        {"product": "tea", "total": 15},
    ]


def test_convert_csv_to_excel_accepts_custom_output(tmp_path: Path) -> None:
    csv_file = tmp_path / "sales.csv"
    output_file = tmp_path / "exports" / "sales_report.xlsx"
    csv_file.write_text("product,total\ncoffee,25\n", encoding="utf-8")

    output = convert_csv_to_excel(csv_file, output_file)

    assert output == output_file
    assert output.exists()


def test_convert_csv_to_excel_accepts_custom_delimiter(tmp_path: Path) -> None:
    csv_file = tmp_path / "sales.csv"
    csv_file.write_text("product;total\ncoffee;25\ntea;15\n", encoding="utf-8")

    output = convert_csv_to_excel(csv_file, delimiter=";")

    dataframe = pd.read_excel(output)
    assert list(dataframe.columns) == ["product", "total"]
    assert dataframe.to_dict(orient="records") == [
        {"product": "coffee", "total": 25},
        {"product": "tea", "total": 15},
    ]


def test_convert_csv_to_excel_accepts_custom_encoding(tmp_path: Path) -> None:
    csv_file = tmp_path / "customers.csv"
    csv_file.write_text("name,city\nJose,San Jose\n", encoding="latin-1")

    output = convert_csv_to_excel(csv_file, encoding="latin-1")

    dataframe = pd.read_excel(output)
    assert dataframe.to_dict(orient="records") == [{"name": "Jose", "city": "San Jose"}]


def test_convert_csv_to_excel_rejects_non_csv_file(tmp_path: Path) -> None:
    text_file = tmp_path / "notes.txt"
    text_file.write_text("not csv", encoding="utf-8")

    with pytest.raises(ValueError, match="Expected a .csv file"):
        convert_csv_to_excel(text_file)


def test_convert_csv_to_excel_rejects_empty_delimiter(tmp_path: Path) -> None:
    csv_file = tmp_path / "sales.csv"
    csv_file.write_text("product,total\ncoffee,25\n", encoding="utf-8")

    with pytest.raises(ValueError, match="Delimiter cannot be empty"):
        convert_csv_to_excel(csv_file, delimiter="")


def test_convert_csv_to_excel_rejects_multi_character_delimiter(tmp_path: Path) -> None:
    csv_file = tmp_path / "sales.csv"
    csv_file.write_text("product,total\ncoffee,25\n", encoding="utf-8")

    with pytest.raises(ValueError, match="Delimiter must be a single character"):
        convert_csv_to_excel(csv_file, delimiter="::")
