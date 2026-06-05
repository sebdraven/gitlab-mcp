"""
CI/CD Variables tools for GitLab MCP server.

This module provides MCP tools for managing project-level CI/CD variables:
- Listing project variables
- Getting a single variable
- Creating a variable
- Updating a variable
- Deleting a variable

Variables with the same key but different `environment_scope` are disambiguated
via the `filter_environment_scope` parameter on get/update/delete operations.

All tools are async functions that accept a GitLabClient and return formatted data.
"""

import asyncio
from typing import Any

from gitlab_mcp.client.gitlab_client import GitLabClient


async def list_project_variables(
    client: GitLabClient,
    project_id: str | int,
    page: int = 1,
    per_page: int = 20,
) -> list[dict[str, Any]]:
    """
    List CI/CD variables defined at the project level.

    Args:
        client: Authenticated GitLabClient instance
        project_id: Project ID (int) or path (str)
        page: Page number for pagination
        per_page: Results per page (max 100)

    Returns:
        List of variable dictionaries
    """
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.list_project_variables(
        project_id=project_id,
        page=page,
        per_page=per_page,
    )


async def get_project_variable(
    client: GitLabClient,
    project_id: str | int,
    key: str,
    filter_environment_scope: str | None = None,
) -> dict[str, Any]:
    """
    Get a single CI/CD variable by key.

    Args:
        client: Authenticated GitLabClient instance
        project_id: Project ID (int) or path (str)
        key: Variable key (e.g., 'DEPLOY_TOKEN')
        filter_environment_scope: Restrict lookup to a given environment scope
            (required when multiple variables share the same key across scopes)

    Returns:
        Variable dictionary
    """
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.get_project_variable(
        project_id=project_id,
        key=key,
        filter_environment_scope=filter_environment_scope,
    )


async def create_project_variable(
    client: GitLabClient,
    project_id: str | int,
    key: str,
    value: str,
    variable_type: str | None = None,
    protected: bool | None = None,
    masked: bool | None = None,
    raw: bool | None = None,
    environment_scope: str | None = None,
    description: str | None = None,
) -> dict[str, Any]:
    """
    Create a new CI/CD variable at the project level.

    Args:
        client: Authenticated GitLabClient instance
        project_id: Project ID (int) or path (str)
        key: Variable key (required, A-Z 0-9 _ only)
        value: Variable value (required)
        variable_type: 'env_var' (default) or 'file' (optional)
        protected: Restrict to protected branches/tags (optional, default false)
        masked: Mask value in job logs (optional, default false)
        raw: Disable variable expansion (optional, default false)
        environment_scope: Restrict to an environment (optional, default '*')
        description: Variable description (optional, GitLab 16.2+)

    Returns:
        Created variable dictionary
    """
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.create_project_variable(
        project_id=project_id,
        key=key,
        value=value,
        variable_type=variable_type,
        protected=protected,
        masked=masked,
        raw=raw,
        environment_scope=environment_scope,
        description=description,
    )


async def update_project_variable(
    client: GitLabClient,
    project_id: str | int,
    key: str,
    value: str | None = None,
    variable_type: str | None = None,
    protected: bool | None = None,
    masked: bool | None = None,
    raw: bool | None = None,
    environment_scope: str | None = None,
    description: str | None = None,
    filter_environment_scope: str | None = None,
) -> dict[str, Any]:
    """
    Update an existing CI/CD variable. Only fields explicitly provided are sent.

    Args:
        client: Authenticated GitLabClient instance
        project_id: Project ID (int) or path (str)
        key: Variable key to update
        value: New value (optional)
        variable_type: 'env_var' or 'file' (optional)
        protected: Restrict to protected branches/tags (optional)
        masked: Mask value in job logs (optional)
        raw: Disable variable expansion (optional)
        environment_scope: Change environment scope (optional)
        description: New description (optional)
        filter_environment_scope: Restrict update to a given env scope
            (required when multiple variables share the same key across scopes)

    Returns:
        Updated variable dictionary
    """
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.update_project_variable(
        project_id=project_id,
        key=key,
        value=value,
        variable_type=variable_type,
        protected=protected,
        masked=masked,
        raw=raw,
        environment_scope=environment_scope,
        description=description,
        filter_environment_scope=filter_environment_scope,
    )


async def delete_project_variable(
    client: GitLabClient,
    project_id: str | int,
    key: str,
    filter_environment_scope: str | None = None,
) -> dict[str, str]:
    """
    Delete a CI/CD variable.

    Args:
        client: Authenticated GitLabClient instance
        project_id: Project ID (int) or path (str)
        key: Variable key to delete
        filter_environment_scope: Restrict deletion to a given env scope
            (required when multiple variables share the same key across scopes)

    Returns:
        Dictionary {"status": "deleted", "project_id": "<id>", "key": "<key>"}
    """
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.delete_project_variable(
        project_id=project_id,
        key=key,
        filter_environment_scope=filter_environment_scope,
    )
