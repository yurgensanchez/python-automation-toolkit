# Python Automation Toolkit

[![Tests](https://github.com/yurgensanchez/python-automation-toolkit/actions/workflows/tests.yml/badge.svg)](https://github.com/yurgensanchez/python-automation-toolkit/actions/workflows/tests.yml)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

Small Python CLI toolkit for practical automation tasks involving files and text.

This repository is part of a professional portfolio focused on Python, automation, clean project structure, tests, and clear documentation. The goal is not to build a large automation platform. The goal is to show a simple, maintainable project that solves common tasks in a reproducible way.

## Portfolio Context

This is the first project in a broader portfolio focused on Python development and applied automation. I kept the scope intentionally small so the repository can show the basics well: a package structure, a usable CLI, tests, documentation, GitHub Actions, and a realistic commit/PR history.

The project is not meant to be a full production automation suite. It is a practical foundation that demonstrates how I organize code, handle errors, document behavior, and add features incrementally.

## Problem

Small repetitive tasks often take more time than they should: grouping files, cleaning copied text, preparing inputs for reports, or creating small command-line helpers. This project collects a few focused tools that can be used from the terminal and tested independently.

## Current Features

- Organize files into folders by extension.
- Preview file organization with `--dry-run`.
- Convert CSV files to Excel workbooks.
- Rename files using a numbered pattern.
- Generate a simple Markdown report for files in a directory.
- Fetch a short summary for a public GitHub repository.
- Clean text by trimming extra spaces and collapsing repeated whitespace.
- Optional lowercase conversion for cleaned text.

## Technologies

- Python 3.10+
- Typer for the CLI
- Rich for terminal output
- pandas and openpyxl for CSV to Excel conversion
- requests for public API calls
- pytest for tests
- pathlib and logging from the standard library

## Status

Version `v0.1.0` is the first portfolio-ready version of this project. It includes the core CLI commands, unit tests, CLI integration tests, documentation, and a passing GitHub Actions workflow.

## Project Structure

```text
python-automation-toolkit/
├── docs/
├── examples/
├── src/
│   └── automation_toolkit/
│       ├── api_tools.py
│       ├── csv_tools.py
│       ├── cli.py
│       ├── file_tools.py
│       ├── rename_tools.py
│       ├── report_tools.py
│       └── text_tools.py
├── tests/
├── pyproject.toml
└── README.md
```

## Installation

Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install the project in editable mode with development dependencies:

```bash
pip install -e ".[dev]"
```

## Usage

Show available commands:

```bash
automation-toolkit --help
```

Fetch a public GitHub repository summary:

```bash
automation-toolkit github-repo-summary python cpython
```

Organize files by extension:

```bash
automation-toolkit organize-files examples/sample_files
```

Preview the operation without moving files:

```bash
automation-toolkit organize-files examples/sample_files --dry-run
```

Write organized files to another directory:

```bash
automation-toolkit organize-files examples/sample_files --output organized_output
```

Clean text:

```bash
automation-toolkit clean-text "  Hello     from   Python  "
```

Clean and lowercase text:

```bash
automation-toolkit clean-text "  HELLO     From   Python  " --lowercase
```

Convert a CSV file to Excel:

```bash
automation-toolkit csv-to-excel examples/sample_files/report.csv
```

Write the Excel file to a custom path:

```bash
automation-toolkit csv-to-excel examples/sample_files/report.csv --output organized_output/report.xlsx
```

Convert a semicolon-delimited CSV:

```bash
automation-toolkit csv-to-excel examples/sample_files/report.csv --delimiter ";"
```

Read a CSV with a specific encoding:

```bash
automation-toolkit csv-to-excel examples/sample_files/report.csv --encoding latin-1
```

Preview file renaming:

```bash
automation-toolkit rename-files examples/sample_files --prefix document --dry-run
```

Rename files with a custom starting number:

```bash
automation-toolkit rename-files examples/sample_files --prefix document --start 10
```

Generate a file report in the terminal:

```bash
automation-toolkit file-report examples/sample_files
```

Write a report to a Markdown file:

```bash
automation-toolkit file-report examples/sample_files --output organized_output/report.md
```

## Tests

Run the test suite:

```bash
pytest
```

The repository also includes a GitHub Actions workflow that runs the test suite on pushes and pull requests targeting `main`.

## Design Decisions

- The first version only processes files directly inside the selected directory.
- Nested directory traversal is intentionally left out to avoid unexpected file moves.
- `--dry-run` exists so users can review changes before moving files.
- CLI logic is separated from business logic so tests can target the core functions.
- CSV conversion is implemented as a focused command instead of being mixed into the file organizer.
- Renaming refuses to overwrite files that already exist.
- Reports are generated as Markdown so they can be reviewed or committed easily.

## Limitations

- The file organizer does not process nested directories yet.
- Existing destination files are not renamed automatically.
- CSV conversion supports custom delimiter and encoding options, but does not auto-detect them.
- File renaming uses one numbered pattern at a time.
- File reports only summarize files directly inside one folder.
- GitHub repository summaries use the public GitHub API and may be rate-limited.
- This is a portfolio/demo project, not a production-grade automation suite.

See [docs/limitations.md](docs/limitations.md) for more detail.

## Next Steps

These are intentionally left as possible future improvements, not requirements for the first portfolio version.

- Add examples with sample files.
- Add date-based rename patterns.
- Add optional recursive reports.
- Improve error messages for common user mistakes.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
