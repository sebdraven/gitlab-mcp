"""
Runners tools for GitLab MCP server.

This module provides MCP tools for managing GitLab CI/CD runners at the project level:
- Listing runners enabled for a project
- Getting runner details by ID
- Enabling/disabling runners for a project
- Updating runner configuration

Runner instance creation (POST /runners with authentication tokens) is intentionally
out of scope: it relies on the GitLab 16+ runner registration token flow which is
typically performed outside an MCP context.

All tools are async functions that accept a GitLabClient and return formatted data.
"""

import asyncio
from typing import Any

from gitlab_mcp.client.gitlab_client import GitLabClient


async def list_project_runners(
    client: GitLabClient,
    project_id: str | int,
    type: str | None = None,
    status: str | None = None,
    tag_list: list[str] | None = None,
    page: int = 1,
    per_page: int = 20,
) -> list[dict[str, Any]]:
    """
    List runners enabled for a project (project-owned + shared).

    Args:
        client: Authenticated GitLabClient instance
        project_id: Project ID (int) or path (str)
        type: Filter by type - 'instance_type', 'group_type', 'project_type' (optional)
        status: Filter by status - 'online', 'offline', 'stale', 'never_contacted',
            'active', 'paused' (optional)
        tag_list: Filter by tags (optional)
        page: Page number for pagination
        per_page: Results per page (max 100)

    Returns:
        List of runner dictionaries
    """
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.list_project_runners(
        project_id=project_id,
        type=type,
        status=status,
        tag_list=tag_list,
        page=page,
        per_page=per_page,
    )


async def get_runner(
    client: GitLabClient,
    runner_id: int,
) -> dict[str, Any]:
    """
    Get details of a single runner by ID.

    Requires admin privileges OR ownership/maintainer access on a project
    the runner is associated with.

    Args:
        client: Authenticated GitLabClient instance
        runner_id: Runner ID

    Returns:
        Runner dictionary with full details
    """
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.get_runner(runner_id=runner_id)


async def enable_project_runner(
    client: GitLabClient,
    project_id: str | int,
    runner_id: int,
) -> dict[str, Any]:
    """
    Enable an existing runner for a project.

    Args:
        client: Authenticated GitLabClient instance
        project_id: Project ID (int) or path (str)
        runner_id: ID of an existing runner to enable for this project

    Returns:
        Runner dictionary as enabled for the project
    """
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.enable_project_runner(
        project_id=project_id,
        runner_id=runner_id,
    )


async def disable_project_runner(
    client: GitLabClient,
    project_id: str | int,
    runner_id: int,
) -> dict[str, str]:
    """
    Disable (disassociate) a runner from a project. Reversible.

    Args:
        client: Authenticated GitLabClient instance
        project_id: Project ID (int) or path (str)
        runner_id: Runner ID to disable for this project

    Returns:
        Dictionary {"status": "disabled", "project_id": "<id>", "runner_id": <id>}
    """
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.disable_project_runner(
        project_id=project_id,
        runner_id=runner_id,
    )


async def update_runner(
    client: GitLabClient,
    runner_id: int,
    description: str | None = None,
    active: bool | None = None,
    paused: bool | None = None,
    tag_list: list[str] | None = None,
    run_untagged: bool | None = None,
    locked: bool | None = None,
    access_level: str | None = None,
    maximum_timeout: int | None = None,
) -> dict[str, Any]:
    """
    Update an existing runner's configuration. Only fields explicitly provided are sent.

    Args:
        client: Authenticated GitLabClient instance
        runner_id: Runner ID
        description: New description (optional)
        active: Enable/disable runner (deprecated GitLab 14+, use `paused`) (optional)
        paused: Pause/unpause runner (optional, GitLab 14+)
        tag_list: Replace runner tags (optional)
        run_untagged: Allow runner to pick up untagged jobs (optional)
        locked: Lock runner to current projects (optional)
        access_level: 'not_protected' or 'ref_protected' (optional)
        maximum_timeout: Max job timeout in seconds (optional)

    Returns:
        Updated runner dictionary
    """
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.update_runner(
        runner_id=runner_id,
        description=description,
        active=active,
        paused=paused,
        tag_list=tag_list,
        run_untagged=run_untagged,
        locked=locked,
        access_level=access_level,
        maximum_timeout=maximum_timeout,
    )
