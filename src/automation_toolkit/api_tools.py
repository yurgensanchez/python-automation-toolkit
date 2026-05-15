from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import requests

GITHUB_API_BASE_URL = "https://api.github.com"


@dataclass(frozen=True)
class GitHubRepoSummary:
    full_name: str
    description: str | None
    stars: int
    forks: int
    open_issues: int
    language: str | None
    url: str


def parse_github_repo_summary(payload: dict[str, Any]) -> GitHubRepoSummary:
    """Parse the GitHub repository API response into a small summary."""
    return GitHubRepoSummary(
        full_name=payload["full_name"],
        description=payload.get("description"),
        stars=int(payload.get("stargazers_count", 0)),
        forks=int(payload.get("forks_count", 0)),
        open_issues=int(payload.get("open_issues_count", 0)),
        language=payload.get("language"),
        url=payload["html_url"],
    )


def fetch_github_repo_summary(owner: str, repo: str, timeout: float = 10.0) -> GitHubRepoSummary:
    """Fetch a public GitHub repository summary without requiring an API key."""
    if not owner.strip():
        raise ValueError("Owner cannot be empty")
    if not repo.strip():
        raise ValueError("Repository name cannot be empty")

    url = f"{GITHUB_API_BASE_URL}/repos/{owner.strip()}/{repo.strip()}"

    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
    except requests.Timeout as exc:
        raise RuntimeError("GitHub API request timed out") from exc
    except requests.HTTPError as exc:
        status_code = exc.response.status_code if exc.response is not None else "unknown"
        raise RuntimeError(f"GitHub API request failed with status {status_code}") from exc
    except requests.RequestException as exc:
        raise RuntimeError("GitHub API request failed") from exc

    return parse_github_repo_summary(response.json())


def format_github_repo_summary(summary: GitHubRepoSummary) -> str:
    """Format a GitHub repository summary for terminal output."""
    description = summary.description or "No description"
    language = summary.language or "Not specified"

    return "\n".join(
        [
            f"Repository: {summary.full_name}",
            f"Description: {description}",
            f"Language: {language}",
            f"Stars: {summary.stars}",
            f"Forks: {summary.forks}",
            f"Open issues: {summary.open_issues}",
            f"URL: {summary.url}",
        ]
    )
