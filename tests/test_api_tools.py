from typing import Any

import pytest
import requests

from automation_toolkit.api_tools import (
    GitHubRepoSummary,
    fetch_github_repo_summary,
    format_github_repo_summary,
    parse_github_repo_summary,
)


def test_parse_github_repo_summary_maps_expected_fields() -> None:
    payload: dict[str, Any] = {
        "full_name": "python/cpython",
        "description": "The Python programming language",
        "stargazers_count": 70000,
        "forks_count": 30000,
        "open_issues_count": 9000,
        "language": "Python",
        "html_url": "https://github.com/python/cpython",
    }

    summary = parse_github_repo_summary(payload)

    assert summary == GitHubRepoSummary(
        full_name="python/cpython",
        description="The Python programming language",
        stars=70000,
        forks=30000,
        open_issues=9000,
        language="Python",
        url="https://github.com/python/cpython",
    )


def test_format_github_repo_summary_outputs_terminal_text() -> None:
    summary = GitHubRepoSummary(
        full_name="python/cpython",
        description="The Python programming language",
        stars=70000,
        forks=30000,
        open_issues=9000,
        language="Python",
        url="https://github.com/python/cpython",
    )

    formatted = format_github_repo_summary(summary)

    assert "Repository: python/cpython" in formatted
    assert "Stars: 70000" in formatted
    assert "URL: https://github.com/python/cpython" in formatted


def test_fetch_github_repo_summary_rejects_empty_owner() -> None:
    with pytest.raises(ValueError, match="Owner cannot be empty"):
        fetch_github_repo_summary(" ", "repo")


def test_fetch_github_repo_summary_handles_timeout(monkeypatch: pytest.MonkeyPatch) -> None:
    def fake_get(*args: object, **kwargs: object) -> None:
        raise requests.Timeout()

    monkeypatch.setattr("automation_toolkit.api_tools.requests.get", fake_get)

    with pytest.raises(RuntimeError, match="timed out"):
        fetch_github_repo_summary("python", "cpython")
