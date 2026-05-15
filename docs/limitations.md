# Limitations

This project is intentionally small in its first version. The current goal is to show clean Python structure, a usable CLI, and basic tests.

## Current Limits

- The file organizer only reads files directly inside the selected folder.
- It does not recursively organize nested directories.
- It does not handle duplicate destination filenames with automatic renaming.
- The rename command uses a simple numbered pattern only.
- The rename command does not recursively rename files in nested directories.
- It does not currently include CSV to Excel conversion.
- It does not currently consume external APIs.
- It has basic tests, but not full CLI integration tests yet.

## Why These Limits Exist

The first version avoids broad file-system behavior because automation tools can create real user damage if they move files unexpectedly. Recursive operations and overwrite handling should be added only after the behavior is documented and tested.

## Future Improvements

- Add safer duplicate filename handling.
- Add recursive mode as an explicit option.
- Add more rename patterns, such as date-based names.
- Add CLI integration tests.
- Add CSV to Excel conversion.
- Add sample input and output folders for documentation.
- Add GitHub Actions to run tests automatically.
