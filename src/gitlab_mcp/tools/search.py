"""
Search tools for GitLab MCP server.

This module provides MCP tools for searching across GitLab at three scopes:
- Instance-wide (`search_globally`)
- Group-scoped (`search_in_group`)
- Project-scoped (`search_in_project`)

These tools complement the existing narrower search tools (`search_code` for
project-scoped blob search, `search_projects` for finding projects by name).
They expose the full GitLab Search API with all available scopes.

All tools are async functions that accept a GitLabClient and return formatted data.
"""

import asyncio
from typing import Any

from gitlab_mcp.client.gitlab_client import GitLabClient


async def search_globally(
    client: GitLabClient,
    scope: str,
    search: str,
    state: str | None = None,
    confidential: bool | None = None,
    order_by: str | None = None,
    sort: str | None = None,
    page: int = 1,
    per_page: int = 20,
) -> list[dict[str, Any]]:
    """
    Search across the GitLab instance.

    Scopes (Free): projects, issues, merge_requests, milestones,
        snippet_titles, users.
    Scopes (Premium): blobs, commits, wiki_blobs, notes.

    Args:
        client: Authenticated GitLabClient instance
        scope: Search scope (required)
        search: Search query string (required)
        state: Filter by state - 'opened' or 'closed' (issues/MRs, optional)
        confidential: Filter confidential issues (optional)
        order_by: 'created_at' (optional)
        sort: 'asc' or 'desc' (optional)
        page: Page number for pagination
        per_page: Results per page (max 100)

    Returns:
        List of result dictionaries (shape depends on scope)
    """
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.search_globally(
        scope=scope,
        search=search,
        state=state,
        confidential=confidential,
        order_by=order_by,
        sort=sort,
        page=page,
        per_page=per_page,
    )


async def search_in_group(
    client: GitLabClient,
    group_id: str | int,
    scope: str,
    search: str,
    state: str | None = None,
    confidential: bool | None = None,
    order_by: str | None = None,
    sort: str | None = None,
    page: int = 1,
    per_page: int = 20,
) -> list[dict[str, Any]]:
    """
    Search inside a group.

    Scopes (Free): projects, issues, merge_requests, milestones, users.
    Scopes (Premium): blobs, commits, wiki_blobs, notes.

    Args:
        client: Authenticated GitLabClient instance
        group_id: Group ID (int) or path (str)
        scope: Search scope (required)
        search: Search query string (required)
        state: Filter by state - 'opened' or 'closed' (optional)
        confidential: Filter confidential issues (optional)
        order_by: 'created_at' (optional)
        sort: 'asc' or 'desc' (optional)
        page: Page number for pagination
        per_page: Results per page (max 100)

    Returns:
        List of result dictionaries
    """
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.search_in_group(
        group_id=group_id,
        scope=scope,
        search=search,
        state=state,
        confidential=confidential,
        order_by=order_by,
        sort=sort,
        page=page,
        per_page=per_page,
    )


async def search_in_project(
    client: GitLabClient,
    project_id: str | int,
    scope: str,
    search: str,
    state: str | None = None,
    confidential: bool | None = None,
    order_by: str | None = None,
    sort: str | None = None,
    ref: str | None = None,
    page: int = 1,
    per_page: int = 20,
) -> list[dict[str, Any]]:
    """
    Search inside a project.

    Scopes: blobs, commits, issues, merge_requests, milestones, notes,
        users, wiki_blobs.

    Args:
        client: Authenticated GitLabClient instance
        project_id: Project ID (int) or path (str)
        scope: Search scope (required)
        search: Search query string (required)
        state: Filter by state - 'opened' or 'closed' (optional)
        confidential: Filter confidential issues (optional)
        order_by: 'created_at' (optional)
        sort: 'asc' or 'desc' (optional)
        ref: Branch/tag for blob/commit scopes (optional, default: default branch)
        page: Page number for pagination
        per_page: Results per page (max 100)

    Returns:
        List of result dictionaries
    """
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.search_in_project(
        project_id=project_id,
        scope=scope,
        search=search,
        state=state,
        confidential=confidential,
        order_by=order_by,
        sort=sort,
        ref=ref,
        page=page,
        per_page=per_page,
    )
