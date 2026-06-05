"""
Environments tools for GitLab MCP server.

This module provides MCP tools for managing project-level deployment environments:
- Listing environments
- Getting an environment
- Creating an environment
- Updating an environment
- Deleting an environment
- Stopping an environment (reversible state transition)

All tools are async functions that accept a GitLabClient and return formatted data.
"""

import asyncio
from typing import Any

from gitlab_mcp.client.gitlab_client import GitLabClient


async def list_environments(
    client: GitLabClient,
    project_id: str | int,
    name: str | None = None,
    search: str | None = None,
    states: str | None = None,
    page: int = 1,
    per_page: int = 20,
) -> list[dict[str, Any]]:
    """
    List deployment environments of a project.

    Args:
        client: Authenticated GitLabClient instance
        project_id: Project ID (int) or path (str)
        name: Filter by exact environment name (optional)
        search: Filter by name substring, minimum 3 chars (optional)
        states: Filter by state - 'available', 'stopping', or 'stopped' (optional)
        page: Page number for pagination
        per_page: Results per page (max 100)

    Returns:
        List of environment dictionaries
    """
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.list_environments(
        project_id=project_id,
        name=name,
        search=search,
        states=states,
        page=page,
        per_page=per_page,
    )


async def get_environment(
    client: GitLabClient,
    project_id: str | int,
    environment_id: int,
) -> dict[str, Any]:
    """
    Get a single environment by ID.

    Args:
        client: Authenticated GitLabClient instance
        project_id: Project ID (int) or path (str)
        environment_id: Environment ID

    Returns:
        Environment dictionary
    """
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.get_environment(
        project_id=project_id,
        environment_id=environment_id,
    )


async def create_environment(
    client: GitLabClient,
    project_id: str | int,
    name: str,
    external_url: str | None = None,
    tier: str | None = None,
) -> dict[str, Any]:
    """
    Create a new environment.

    Args:
        client: Authenticated GitLabClient instance
        project_id: Project ID (int) or path (str)
        name: Environment name (required)
        external_url: External URL of the environment (optional)
        tier: Environment tier - 'production', 'staging', 'testing',
            'development', or 'other' (optional, GitLab 16.0+)

    Returns:
        Created environment dictionary
    """
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.create_environment(
        project_id=project_id,
        name=name,
        external_url=external_url,
        tier=tier,
    )


async def update_environment(
    client: GitLabClient,
    project_id: str | int,
    environment_id: int,
    external_url: str | None = None,
    tier: str | None = None,
) -> dict[str, Any]:
    """
    Update an existing environment. Only fields explicitly provided are sent.

    Note: the `name` of an environment is immutable via the API.

    Args:
        client: Authenticated GitLabClient instance
        project_id: Project ID (int) or path (str)
        environment_id: Environment ID
        external_url: New external URL (optional)
        tier: New tier - 'production', 'staging', 'testing',
            'development', or 'other' (optional)

    Returns:
        Updated environment dictionary
    """
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.update_environment(
        project_id=project_id,
        environment_id=environment_id,
        external_url=external_url,
        tier=tier,
    )


async def delete_environment(
    client: GitLabClient,
    project_id: str | int,
    environment_id: int,
) -> dict[str, str]:
    """
    Delete an environment.

    Note: an environment must be stopped before it can be deleted.
    Use stop_environment first if the environment is in 'available' state.

    Args:
        client: Authenticated GitLabClient instance
        project_id: Project ID (int) or path (str)
        environment_id: Environment ID

    Returns:
        Dictionary {"status": "deleted", "project_id": "<id>", "environment_id": <id>}
    """
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.delete_environment(
        project_id=project_id,
        environment_id=environment_id,
    )


async def stop_environment(
    client: GitLabClient,
    project_id: str | int,
    environment_id: int,
) -> dict[str, Any]:
    """
    Stop an environment (transition state to 'stopped'). Reversible.

    Args:
        client: Authenticated GitLabClient instance
        project_id: Project ID (int) or path (str)
        environment_id: Environment ID

    Returns:
        Updated environment dictionary (state will be 'stopping' or 'stopped')
    """
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.stop_environment(
        project_id=project_id,
        environment_id=environment_id,
    )
