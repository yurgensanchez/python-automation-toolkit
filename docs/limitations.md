# Limitations

This project is intentionally small in its first version. The current goal is to show clean Python structure, a usable CLI, and basic tests.

## Current Limits

- The file organizer only reads files directly inside the selected folder.
- It does not recursively organize nested directories.
- It does not handle duplicate destination filenames with automatic renaming.
- CSV to Excel conversion uses pandas defaults.
- CSV to Excel conversion does not expose custom delimiter or encoding options yet.
- It does not currently consume external APIs.
- It has basic tests, but not full CLI integration tests yet.

## Why These Limits Exist

The first version avoids broad file-system behavior because automation tools can create real user damage if they move files unexpectedly. Recursive operations and overwrite handling should be added only after the behavior is documented and tested.

## Future Improvements

- Add safer duplicate filename handling.
- Add recursive mode as an explicit option.
- Add CLI integration tests.
- Add CSV delimiter and encoding options.
- Add sample input and output folders for documentation.
- Add GitHub Actions to run tests automatically.
