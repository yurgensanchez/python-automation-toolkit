# Limitations

This project is intentionally small in its first version. The current goal is to show clean Python structure, a usable CLI, and basic tests.

## Current Limits

- The file organizer only reads files directly inside the selected folder.
- It does not recursively organize nested directories.
- It does not handle duplicate destination filenames with automatic renaming.
- CSV to Excel conversion supports custom delimiter and encoding options, but does not auto-detect them.
- CSV to Excel conversion expects a single-character delimiter.
- The rename command uses a simple numbered pattern only.
- The rename command does not recursively rename files in nested directories.
- Directory reports only summarize files directly inside one folder.
- GitHub repository summaries use the public GitHub API without authentication.
- GitHub API requests may fail because of network issues, unavailable repositories, or rate limits.
- It has basic tests, but not full CLI integration tests yet.

## Why These Limits Exist

The first version avoids broad file-system behavior because automation tools can create real user damage if they move files unexpectedly. Recursive operations and overwrite handling should be added only after the behavior is documented and tested.

## Future Improvements

- Add safer duplicate filename handling.
- Add recursive mode as an explicit option.
- Add more rename patterns, such as date-based names.
- Add recursive directory reports as an explicit option.
- Add CLI integration tests.
- Add CSV delimiter and encoding auto-detection if it becomes useful.
- Add optional authenticated GitHub API requests only if the project needs higher rate limits.
- Add sample input and output folders for documentation.
- Add GitHub Actions to run tests automatically.
