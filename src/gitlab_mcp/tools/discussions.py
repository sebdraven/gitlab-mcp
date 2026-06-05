"""
Merge Request discussion tools for GitLab MCP server.

This module provides MCP tools for managing threaded discussions on merge
requests, including resolution workflows and individual note edition. It
complements the existing flat MR comment helpers (`add_mr_comment`,
`list_mr_comments`).

Key concepts:
- A `discussion` is a thread of one or more `notes` (comments).
- Discussions can be anchored to a specific line in the diff via `position`
  (inline review comments) or live as standalone threads on the MR.
- MR discussions can be marked resolved/unresolved (unlike issue discussions).
- Notes can be edited or deleted individually by their note_id.

All tools are async functions that accept a GitLabClient and return formatted data.
"""

import asyncio
from typing import Any

from gitlab_mcp.client.gitlab_client import GitLabClient


async def list_merge_request_discussions(
    client: GitLabClient,
    project_id: str | int,
    merge_request_iid: int,
    page: int = 1,
    per_page: int = 20,
) -> list[dict[str, Any]]:
    """List threaded discussions on a merge request."""
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.list_merge_request_discussions(
        project_id=project_id,
        merge_request_iid=merge_request_iid,
        page=page,
        per_page=per_page,
    )


async def get_merge_request_discussion(
    client: GitLabClient,
    project_id: str | int,
    merge_request_iid: int,
    discussion_id: str,
) -> dict[str, Any]:
    """Get a single MR discussion by its ID."""
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.get_merge_request_discussion(
        project_id=project_id,
        merge_request_iid=merge_request_iid,
        discussion_id=discussion_id,
    )


async def create_merge_request_discussion(
    client: GitLabClient,
    project_id: str | int,
    merge_request_iid: int,
    body: str,
    position: dict[str, Any] | None = None,
    commit_id: str | None = None,
) -> dict[str, Any]:
    """
    Create a new threaded discussion on a merge request.

    If `position` is provided, the discussion is anchored to a specific line
    in the diff (inline review comment). Otherwise it's a regular threaded
    comment.

    Position dict required keys: base_sha, start_sha, head_sha, position_type
    ('text' or 'image'), new_path, old_path.
    Position dict optional keys: new_line, old_line.
    """
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.create_merge_request_discussion(
        project_id=project_id,
        merge_request_iid=merge_request_iid,
        body=body,
        position=position,
        commit_id=commit_id,
    )


async def add_note_to_merge_request_discussion(
    client: GitLabClient,
    project_id: str | int,
    merge_request_iid: int,
    discussion_id: str,
    body: str,
) -> dict[str, Any]:
    """Reply to an existing MR discussion by adding a note to its thread."""
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.add_note_to_merge_request_discussion(
        project_id=project_id,
        merge_request_iid=merge_request_iid,
        discussion_id=discussion_id,
        body=body,
    )


async def resolve_merge_request_discussion(
    client: GitLabClient,
    project_id: str | int,
    merge_request_iid: int,
    discussion_id: str,
    resolved: bool = True,
) -> dict[str, Any]:
    """Mark an MR discussion as resolved (default) or unresolved."""
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.resolve_merge_request_discussion(
        project_id=project_id,
        merge_request_iid=merge_request_iid,
        discussion_id=discussion_id,
        resolved=resolved,
    )


async def update_merge_request_note(
    client: GitLabClient,
    project_id: str | int,
    merge_request_iid: int,
    note_id: int,
    body: str,
) -> dict[str, Any]:
    """Update the body of an existing MR note (comment)."""
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.update_merge_request_note(
        project_id=project_id,
        merge_request_iid=merge_request_iid,
        note_id=note_id,
        body=body,
    )


async def delete_merge_request_note(
    client: GitLabClient,
    project_id: str | int,
    merge_request_iid: int,
    note_id: int,
) -> dict[str, Any]:
    """Delete an MR note (comment)."""
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.delete_merge_request_note(
        project_id=project_id,
        merge_request_iid=merge_request_iid,
        note_id=note_id,
    )
