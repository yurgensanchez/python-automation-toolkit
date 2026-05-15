from __future__ import annotations

import re


def clean_text(value: str, lowercase: bool = False, collapse_spaces: bool = True) -> str:
    """Normalize simple text input for reports, filenames, or copied content."""
    cleaned = value.strip()

    if collapse_spaces:
        cleaned = re.sub(r"\s+", " ", cleaned)

    if lowercase:
        cleaned = cleaned.lower()

    return cleaned
