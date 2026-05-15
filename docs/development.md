# Development Notes

## Local Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -e ".[dev]"
```

## Run Tests

```bash
pytest
```

## Add a New Tool

1. Add core logic in a focused module under `src/automation_toolkit/`.
2. Add a CLI command in `src/automation_toolkit/cli.py`.
3. Add tests for the core logic.
4. Update the README and usage examples.
5. Document any limitations.

## Commit Style

Use small commits that represent one logical change.

Examples:

```text
chore(project): add base package structure
feat(files): add extension-based organizer
feat(csv): add csv to excel conversion
test(files): add organizer tests
docs(readme): add installation and usage steps
```
