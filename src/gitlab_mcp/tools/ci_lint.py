"""
CI Lint tools for GitLab MCP server.

This module provides MCP tools for validating GitLab CI/CD YAML configurations:
- Linting an arbitrary YAML (globally or in a project context)
- Validating a project's current `.gitlab-ci.yml`

All tools are async functions that accept a GitLabClient and return formatted data.
"""

import asyncio
from typing import Any

from gitlab_mcp.client.gitlab_client import GitLabClient


async def lint_ci_yaml(
    client: GitLabClient,
    content: str,
    project_id: str | int | None = None,
    dry_run: bool | None = None,
    ref: str | None = None,
    include_jobs: bool | None = None,
    include_merged_yaml: bool | None = None,
) -> dict[str, Any]:
    """
    Validate a GitLab CI/CD YAML configuration.

    When `project_id` is provided, the lint runs in the context of that project,
    which resolves `include:` directives and CI/CD variables. Without it, the
    global lint endpoint is used and only the syntax is validated.

    Args:
        client: Authenticated GitLabClient instance
        content: Raw YAML content to validate (required)
        project_id: Project ID (int) or path (str) to use as lint context (optional)
        dry_run: Simulate creating a pipeline without persisting it (optional,
            project-scoped only)
        ref: Branch/tag/SHA to resolve includes against (optional,
            project-scoped only)
        include_jobs: Include resolved jobs in the response (optional)
        include_merged_yaml: Include the merged YAML in the response (optional)

    Returns:
        Lint result dictionary (valid, errors, warnings, optionally jobs/merged_yaml)
    """
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.lint_ci_yaml(
        content=content,
        project_id=project_id,
        dry_run=dry_run,
        ref=ref,
        include_jobs=include_jobs,
        include_merged_yaml=include_merged_yaml,
    )


async def validate_project_ci_config(
    client: GitLabClient,
    project_id: str | int,
    dry_run: bool | None = None,
    ref: str | None = None,
    include_jobs: bool | None = None,
) -> dict[str, Any]:
    """
    Validate the current `.gitlab-ci.yml` of a project (no content to provide).

    Args:
        client: Authenticated GitLabClient instance
        project_id: Project ID (int) or path (str)
        dry_run: Simulate creating a pipeline without persisting it (optional)
        ref: Branch/tag/SHA to validate (optional, defaults to default branch)
        include_jobs: Include resolved jobs in the response (optional)

    Returns:
        Lint result dictionary
    """
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.validate_project_ci_config(
        project_id=project_id,
        dry_run=dry_run,
        ref=ref,
        include_jobs=include_jobs,
    )
