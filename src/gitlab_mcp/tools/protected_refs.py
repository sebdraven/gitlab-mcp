"""
Protected refs tools for GitLab MCP server.

This module provides MCP tools for managing protected branches and tags:
- Listing, getting, protecting, updating, and unprotecting branches
- Listing, getting, protecting, and unprotecting tags

Access levels follow the standard GitLab convention:
    0  = No access
    30 = Developer
    40 = Maintainer
    60 = Admin

Branch/tag names support wildcard patterns (e.g. 'release/*', 'v*').

Granular `allowed_to_push` / `allowed_to_merge` / `allowed_to_unprotect` lists
(per-user / per-group) are NOT exposed here — only the simple `*_access_level`
integer fields. Extend if needed.

All tools are async functions that accept a GitLabClient and return formatted data.
"""

import asyncio
from typing import Any

from gitlab_mcp.client.gitlab_client import GitLabClient


# ---- Protected branches ----


async def list_protected_branches(
    client: GitLabClient,
    project_id: str | int,
    search: str | None = None,
    page: int = 1,
    per_page: int = 20,
) -> list[dict[str, Any]]:
    """
    List protected branches of a project.

    Args:
        client: Authenticated GitLabClient instance
        project_id: Project ID (int) or path (str)
        search: Filter by name substring (optional)
        page: Page number for pagination
        per_page: Results per page (max 100)

    Returns:
        List of protected branch dictionaries
    """
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.list_protected_branches(
        project_id=project_id,
        search=search,
        page=page,
        per_page=per_page,
    )


async def get_protected_branch(
    client: GitLabClient,
    project_id: str | int,
    name: str,
) -> dict[str, Any]:
    """
    Get a single protected branch by name.

    Args:
        client: Authenticated GitLabClient instance
        project_id: Project ID (int) or path (str)
        name: Protected branch name (wildcards supported)

    Returns:
        Protected branch dictionary
    """
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.get_protected_branch(project_id=project_id, name=name)


async def protect_branch(
    client: GitLabClient,
    project_id: str | int,
    name: str,
    push_access_level: int | None = None,
    merge_access_level: int | None = None,
    unprotect_access_level: int | None = None,
    allow_force_push: bool | None = None,
) -> dict[str, Any]:
    """
    Protect a branch (or wildcard pattern).

    Access levels: 0 (no one), 30 (developer), 40 (maintainer), 60 (admin).
    `unprotect_access_level` accepts only 40 or 60.

    Args:
        client: Authenticated GitLabClient instance
        project_id: Project ID (int) or path (str)
        name: Branch name or wildcard (e.g. 'main', 'release/*')
        push_access_level: Minimum role allowed to push (optional)
        merge_access_level: Minimum role allowed to merge (optional)
        unprotect_access_level: Minimum role allowed to unprotect (optional)
        allow_force_push: Allow force push (optional, default false)

    Returns:
        Created protected branch dictionary
    """
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.protect_branch(
        project_id=project_id,
        name=name,
        push_access_level=push_access_level,
        merge_access_level=merge_access_level,
        unprotect_access_level=unprotect_access_level,
        allow_force_push=allow_force_push,
    )


async def update_protected_branch(
    client: GitLabClient,
    project_id: str | int,
    name: str,
    push_access_level: int | None = None,
    merge_access_level: int | None = None,
    unprotect_access_level: int | None = None,
    allow_force_push: bool | None = None,
) -> dict[str, Any]:
    """
    Update an existing protected branch (GitLab 15.6+).

    Only fields explicitly provided are sent.

    Args:
        client: Authenticated GitLabClient instance
        project_id: Project ID (int) or path (str)
        name: Protected branch name
        push_access_level: New minimum role to push (optional)
        merge_access_level: New minimum role to merge (optional)
        unprotect_access_level: New minimum role to unprotect (optional)
        allow_force_push: Allow force push (optional)

    Returns:
        Updated protected branch dictionary
    """
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.update_protected_branch(
        project_id=project_id,
        name=name,
        push_access_level=push_access_level,
        merge_access_level=merge_access_level,
        unprotect_access_level=unprotect_access_level,
        allow_force_push=allow_force_push,
    )


async def unprotect_branch(
    client: GitLabClient,
    project_id: str | int,
    name: str,
) -> dict[str, str]:
    """
    Remove protection from a branch (or wildcard pattern).

    Args:
        client: Authenticated GitLabClient instance
        project_id: Project ID (int) or path (str)
        name: Protected branch name

    Returns:
        Dictionary {"status": "unprotected", "project_id": "<id>", "name": "<name>"}
    """
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.unprotect_branch(project_id=project_id, name=name)


# ---- Protected tags ----


async def list_protected_tags(
    client: GitLabClient,
    project_id: str | int,
    page: int = 1,
    per_page: int = 20,
) -> list[dict[str, Any]]:
    """
    List protected tags of a project.

    Args:
        client: Authenticated GitLabClient instance
        project_id: Project ID (int) or path (str)
        page: Page number for pagination
        per_page: Results per page (max 100)

    Returns:
        List of protected tag dictionaries
    """
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.list_protected_tags(
        project_id=project_id,
        page=page,
        per_page=per_page,
    )


async def get_protected_tag(
    client: GitLabClient,
    project_id: str | int,
    name: str,
) -> dict[str, Any]:
    """
    Get a single protected tag by name.

    Args:
        client: Authenticated GitLabClient instance
        project_id: Project ID (int) or path (str)
        name: Protected tag name (wildcards supported)

    Returns:
        Protected tag dictionary
    """
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.get_protected_tag(project_id=project_id, name=name)


async def protect_tag(
    client: GitLabClient,
    project_id: str | int,
    name: str,
    create_access_level: int | None = None,
) -> dict[str, Any]:
    """
    Protect a tag (or wildcard pattern).

    Access levels: 0 (no one), 30 (developer), 40 (maintainer), 60 (admin).

    Args:
        client: Authenticated GitLabClient instance
        project_id: Project ID (int) or path (str)
        name: Tag name or wildcard (e.g. 'v*')
        create_access_level: Minimum role allowed to create the tag
            (optional, default 40 = maintainer)

    Returns:
        Created protected tag dictionary
    """
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.protect_tag(
        project_id=project_id,
        name=name,
        create_access_level=create_access_level,
    )


async def unprotect_tag(
    client: GitLabClient,
    project_id: str | int,
    name: str,
) -> dict[str, str]:
    """
    Remove protection from a tag (or wildcard pattern).

    Args:
        client: Authenticated GitLabClient instance
        project_id: Project ID (int) or path (str)
        name: Protected tag name

    Returns:
        Dictionary {"status": "unprotected", "project_id": "<id>", "name": "<name>"}
    """
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.unprotect_tag(project_id=project_id, name=name)
