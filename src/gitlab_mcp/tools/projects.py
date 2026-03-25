"""
Projects tools for GitLab MCP server.

This module provides MCP tools for GitLab project management operations including:
- Listing projects
- Getting project details
- Searching projects
- Listing project members
- Getting project statistics
- Managing milestones

All tools are async functions that accept a GitLabClient and return formatted data.
"""

import asyncio
from typing import Any

from gitlab_mcp.client.gitlab_client import GitLabClient


async def list_projects(
    client: GitLabClient,
    visibility: str | None = None,
    owned: bool | None = None,
    membership: bool | None = None,
    page: int = 1,
    per_page: int = 20,
) -> dict[str, Any]:
    """
    List accessible projects.

    Args:
        client: Authenticated GitLabClient instance
        visibility: Filter by visibility (public, internal, private)
        owned: Limit to projects owned by the current user
        membership: Limit to projects where user is a member
        page: Page number for pagination
        per_page: Results per page (max 100)

    Returns:
        Dictionary with projects list and pagination info
    """
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.list_projects(
        visibility=visibility,
        owned=owned,
        membership=membership,
        page=page,
        per_page=per_page,
    )


async def get_project(
    client: GitLabClient,
    project_id: str | int,
) -> Any:
    """
    Get detailed information about a specific project.

    Args:
        client: Authenticated GitLabClient instance
        project_id: Project ID (int) or path (str)

    Returns:
        Project object from python-gitlab
    """
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.get_project(project_id=project_id)


async def create_project(
    client: GitLabClient,
    name: str,
    path: str | None = None,
    namespace_id: int | None = None,
    description: str | None = None,
    visibility: str = "private",
    initialize_with_readme: bool = False,
) -> dict[str, Any]:
    """
    Create a new GitLab project.

    Args:
        client: Authenticated GitLabClient instance
        name: Project name (required)
        path: Project path/slug (optional, defaults to name if not provided)
        namespace_id: ID of the namespace/group to create project in (optional)
        description: Project description (optional)
        visibility: Project visibility level - 'private', 'internal', or 'public'
                   (default: 'private')
        initialize_with_readme: Whether to initialize project with a README.md
                               (default: False)

    Returns:
        Dictionary with created project details
    """
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.create_project(
        name=name,
        path=path,
        namespace_id=namespace_id,
        description=description,
        visibility=visibility,
        initialize_with_readme=initialize_with_readme,
    )


async def search_projects(
    client: GitLabClient,
    search_term: str,
    page: int = 1,
    per_page: int = 20,
) -> list[dict[str, Any]]:
    """
    Search for projects.

    Args:
        client: Authenticated GitLabClient instance
        search_term: Search query
        page: Page number for pagination
        per_page: Results per page (max 100)

    Returns:
        List of project dictionaries
    """
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.search_projects(
        search_term=search_term,
        page=page,
        per_page=per_page,
    )


async def list_project_members(
    client: GitLabClient,
    project_id: str | int,
    page: int = 1,
    per_page: int = 20,
) -> list[dict[str, Any]]:
    """
    List project members.

    Args:
        client: Authenticated GitLabClient instance
        project_id: Project ID (int) or path (str)
        page: Page number for pagination
        per_page: Results per page (max 100)

    Returns:
        List of member dictionaries
    """
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.list_project_members(
        project_id=project_id,
        page=page,
        per_page=per_page,
    )


async def get_project_statistics(
    client: GitLabClient,
    project_id: str | int,
) -> dict[str, Any]:
    """
    Get project statistics.

    Args:
        client: Authenticated GitLabClient instance
        project_id: Project ID (int) or path (str)

    Returns:
        Dictionary with project statistics
    """
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.get_project_statistics(project_id=project_id)


async def list_milestones(
    client: GitLabClient,
    project_id: str | int,
    state: str | None = None,
    page: int = 1,
    per_page: int = 20,
) -> list[dict[str, Any]]:
    """
    List project milestones.

    Args:
        client: Authenticated GitLabClient instance
        project_id: Project ID (int) or path (str)
        state: Filter by state (active, closed)
        page: Page number for pagination
        per_page: Results per page (max 100)

    Returns:
        List of milestone dictionaries
    """
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.list_milestones(
        project_id=project_id,
        state=state,
        page=page,
        per_page=per_page,
    )


async def get_milestone(
    client: GitLabClient,
    project_id: str | int,
    milestone_id: int,
) -> dict[str, Any]:
    """
    Get milestone details.

    Args:
        client: Authenticated GitLabClient instance
        project_id: Project ID (int) or path (str)
        milestone_id: Milestone ID

    Returns:
        Dictionary with milestone details
    """
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.get_milestone(project_id=project_id, milestone_id=milestone_id)


async def create_milestone(
    client: GitLabClient,
    project_id: str | int,
    title: str,
    description: str | None = None,
    due_date: str | None = None,
    start_date: str | None = None,
) -> dict[str, Any]:
    """
    Create a new milestone.

    Args:
        client: Authenticated GitLabClient instance
        project_id: Project ID (int) or path (str)
        title: Milestone title
        description: Milestone description (optional)
        due_date: Due date in YYYY-MM-DD format (optional)
        start_date: Start date in YYYY-MM-DD format (optional)

    Returns:
        Dictionary with created milestone details
    """
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.create_milestone(
        project_id=project_id,
        title=title,
        description=description,
        due_date=due_date,
        start_date=start_date,
    )


async def update_milestone(
    client: GitLabClient,
    project_id: str | int,
    milestone_id: int,
    title: str | None = None,
    description: str | None = None,
    due_date: str | None = None,
    start_date: str | None = None,
    state: str | None = None,
) -> dict[str, Any]:
    """
    Update an existing milestone.

    Args:
        client: Authenticated GitLabClient instance
        project_id: Project ID (int) or path (str)
        milestone_id: Milestone ID
        title: New title (optional)
        description: New description (optional)
        due_date: New due date in YYYY-MM-DD format (optional)
        start_date: New start date in YYYY-MM-DD format (optional)
        state: State (optional)

    Returns:
        Dictionary with updated milestone details
    """
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.update_milestone(
        project_id=project_id,
        milestone_id=milestone_id,
        title=title,
        description=description,
        due_date=due_date,
        start_date=start_date,
        state=state,
    )
