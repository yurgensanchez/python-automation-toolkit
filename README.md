# Python Automation Toolkit

Small Python CLI toolkit for practical automation tasks involving files and text.

This repository is part of a professional portfolio focused on Python, automation, clean project structure, tests, and clear documentation. The goal is not to build a large automation platform. The goal is to show a simple, maintainable project that solves common tasks in a reproducible way.

## Problem

Small repetitive tasks often take more time than they should: grouping files, cleaning copied text, preparing inputs for reports, or creating small command-line helpers. This project collects a few focused tools that can be used from the terminal and tested independently.

## Current Features

- Organize files into folders by extension.
- Preview file organization with `--dry-run`.
- Rename files using a numbered pattern.
- Clean text by trimming extra spaces and collapsing repeated whitespace.
- Optional lowercase conversion for cleaned text.

## Technologies

- Python 3.10+
- Typer for the CLI
- Rich for terminal output
- pytest for tests
- pathlib and logging from the standard library

## Project Structure

```text
python-automation-toolkit/
├── docs/
├── examples/
├── src/
│   └── automation_toolkit/
│       ├── cli.py
│       ├── file_tools.py
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

Preview file renaming:

```bash
automation-toolkit rename-files examples/sample_files --prefix document --dry-run
```

Rename files with a custom starting number:

```bash
automation-toolkit rename-files examples/sample_files --prefix document --start 10
```

## Tests

Run the test suite:

```bash
pytest
```

## Design Decisions

- The first version only processes files directly inside the selected directory.
- Nested directory traversal is intentionally left out to avoid unexpected file moves.
- `--dry-run` exists so users can review changes before moving files.
- CLI logic is separated from business logic so tests can target the core functions.
- Renaming refuses to overwrite files that already exist.

## Limitations

- The file organizer does not process nested directories yet.
- Existing destination files are not renamed automatically.
- File renaming uses one numbered pattern at a time.
- CSV to Excel conversion and API consumption are planned but not implemented yet.
- This is a portfolio/demo project, not a production-grade automation suite.

See [docs/limitations.md](docs/limitations.md) for more detail.

## Next Steps

- Add a CSV to Excel converter.
- Add examples with sample files.
- Add GitHub Actions for automated tests.
- Improve error messages for common user mistakes.
