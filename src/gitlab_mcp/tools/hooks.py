"""
Webhook tools for GitLab MCP server.

This module provides MCP tools for managing webhooks at two scopes:
- Project-level (CRUD + test)
- Group-level (CRUD only; test endpoint is not available at the group level)

Webhooks notify external systems via HTTP POST when events occur (push, MR,
issue, pipeline, comment, deployment, release, etc.). Common use cases:
- Trigger external CI/CD or custom workflows
- Notify chat platforms (Slack, Discord, Mattermost, etc.)
- Stream events into SIEM / audit pipelines
- Integrate with ticketing or threat-intelligence systems

All tools are async functions that accept a GitLabClient and return formatted data.
"""

import asyncio
from typing import Any

from gitlab_mcp.client.gitlab_client import GitLabClient


# ---- Project hooks ----


async def list_project_hooks(
    client: GitLabClient,
    project_id: str | int,
    page: int = 1,
    per_page: int = 20,
) -> list[dict[str, Any]]:
    """List webhooks of a project."""
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.list_project_hooks(
        project_id=project_id, page=page, per_page=per_page
    )


async def get_project_hook(
    client: GitLabClient,
    project_id: str | int,
    hook_id: int,
) -> dict[str, Any]:
    """Get a single project webhook by ID."""
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.get_project_hook(project_id=project_id, hook_id=hook_id)


async def create_project_hook(
    client: GitLabClient,
    project_id: str | int,
    url: str,
    name: str | None = None,
    description: str | None = None,
    token: str | None = None,
    enable_ssl_verification: bool | None = None,
    push_events: bool | None = None,
    push_events_branch_filter: str | None = None,
    issues_events: bool | None = None,
    confidential_issues_events: bool | None = None,
    merge_requests_events: bool | None = None,
    tag_push_events: bool | None = None,
    note_events: bool | None = None,
    confidential_note_events: bool | None = None,
    job_events: bool | None = None,
    pipeline_events: bool | None = None,
    wiki_page_events: bool | None = None,
    deployment_events: bool | None = None,
    releases_events: bool | None = None,
    feature_flag_events: bool | None = None,
) -> dict[str, Any]:
    """Create a webhook on a project."""
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.create_project_hook(
        project_id=project_id,
        url=url,
        name=name,
        description=description,
        token=token,
        enable_ssl_verification=enable_ssl_verification,
        push_events=push_events,
        push_events_branch_filter=push_events_branch_filter,
        issues_events=issues_events,
        confidential_issues_events=confidential_issues_events,
        merge_requests_events=merge_requests_events,
        tag_push_events=tag_push_events,
        note_events=note_events,
        confidential_note_events=confidential_note_events,
        job_events=job_events,
        pipeline_events=pipeline_events,
        wiki_page_events=wiki_page_events,
        deployment_events=deployment_events,
        releases_events=releases_events,
        feature_flag_events=feature_flag_events,
    )


async def update_project_hook(
    client: GitLabClient,
    project_id: str | int,
    hook_id: int,
    url: str | None = None,
    name: str | None = None,
    description: str | None = None,
    token: str | None = None,
    enable_ssl_verification: bool | None = None,
    push_events: bool | None = None,
    push_events_branch_filter: str | None = None,
    issues_events: bool | None = None,
    confidential_issues_events: bool | None = None,
    merge_requests_events: bool | None = None,
    tag_push_events: bool | None = None,
    note_events: bool | None = None,
    confidential_note_events: bool | None = None,
    job_events: bool | None = None,
    pipeline_events: bool | None = None,
    wiki_page_events: bool | None = None,
    deployment_events: bool | None = None,
    releases_events: bool | None = None,
    feature_flag_events: bool | None = None,
) -> dict[str, Any]:
    """Update an existing project webhook (only provided fields are sent)."""
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.update_project_hook(
        project_id=project_id,
        hook_id=hook_id,
        url=url,
        name=name,
        description=description,
        token=token,
        enable_ssl_verification=enable_ssl_verification,
        push_events=push_events,
        push_events_branch_filter=push_events_branch_filter,
        issues_events=issues_events,
        confidential_issues_events=confidential_issues_events,
        merge_requests_events=merge_requests_events,
        tag_push_events=tag_push_events,
        note_events=note_events,
        confidential_note_events=confidential_note_events,
        job_events=job_events,
        pipeline_events=pipeline_events,
        wiki_page_events=wiki_page_events,
        deployment_events=deployment_events,
        releases_events=releases_events,
        feature_flag_events=feature_flag_events,
    )


async def delete_project_hook(
    client: GitLabClient,
    project_id: str | int,
    hook_id: int,
) -> dict[str, Any]:
    """Delete a project webhook."""
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.delete_project_hook(project_id=project_id, hook_id=hook_id)


async def test_project_hook(
    client: GitLabClient,
    project_id: str | int,
    hook_id: int,
    trigger: str,
) -> dict[str, Any]:
    """
    Trigger a project webhook test for a given event type.

    Valid triggers: push_events, tag_push_events, note_events, issues_events,
    confidential_issues_events, merge_requests_events, job_events,
    pipeline_events, wiki_page_events, releases_events, emoji_events,
    resource_access_token_events.
    """
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.test_project_hook(
        project_id=project_id, hook_id=hook_id, trigger=trigger
    )


# ---- Group hooks ----


async def list_group_hooks(
    client: GitLabClient,
    group_id: str | int,
    page: int = 1,
    per_page: int = 20,
) -> list[dict[str, Any]]:
    """List webhooks of a group."""
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.list_group_hooks(group_id=group_id, page=page, per_page=per_page)


async def get_group_hook(
    client: GitLabClient,
    group_id: str | int,
    hook_id: int,
) -> dict[str, Any]:
    """Get a single group webhook by ID."""
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.get_group_hook(group_id=group_id, hook_id=hook_id)


async def create_group_hook(
    client: GitLabClient,
    group_id: str | int,
    url: str,
    name: str | None = None,
    description: str | None = None,
    token: str | None = None,
    enable_ssl_verification: bool | None = None,
    push_events: bool | None = None,
    push_events_branch_filter: str | None = None,
    issues_events: bool | None = None,
    confidential_issues_events: bool | None = None,
    merge_requests_events: bool | None = None,
    tag_push_events: bool | None = None,
    note_events: bool | None = None,
    confidential_note_events: bool | None = None,
    job_events: bool | None = None,
    pipeline_events: bool | None = None,
    wiki_page_events: bool | None = None,
    deployment_events: bool | None = None,
    releases_events: bool | None = None,
    feature_flag_events: bool | None = None,
    subgroup_events: bool | None = None,
) -> dict[str, Any]:
    """Create a webhook at the group level."""
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.create_group_hook(
        group_id=group_id,
        url=url,
        name=name,
        description=description,
        token=token,
        enable_ssl_verification=enable_ssl_verification,
        push_events=push_events,
        push_events_branch_filter=push_events_branch_filter,
        issues_events=issues_events,
        confidential_issues_events=confidential_issues_events,
        merge_requests_events=merge_requests_events,
        tag_push_events=tag_push_events,
        note_events=note_events,
        confidential_note_events=confidential_note_events,
        job_events=job_events,
        pipeline_events=pipeline_events,
        wiki_page_events=wiki_page_events,
        deployment_events=deployment_events,
        releases_events=releases_events,
        feature_flag_events=feature_flag_events,
        subgroup_events=subgroup_events,
    )


async def update_group_hook(
    client: GitLabClient,
    group_id: str | int,
    hook_id: int,
    url: str | None = None,
    name: str | None = None,
    description: str | None = None,
    token: str | None = None,
    enable_ssl_verification: bool | None = None,
    push_events: bool | None = None,
    push_events_branch_filter: str | None = None,
    issues_events: bool | None = None,
    confidential_issues_events: bool | None = None,
    merge_requests_events: bool | None = None,
    tag_push_events: bool | None = None,
    note_events: bool | None = None,
    confidential_note_events: bool | None = None,
    job_events: bool | None = None,
    pipeline_events: bool | None = None,
    wiki_page_events: bool | None = None,
    deployment_events: bool | None = None,
    releases_events: bool | None = None,
    feature_flag_events: bool | None = None,
    subgroup_events: bool | None = None,
) -> dict[str, Any]:
    """Update an existing group webhook (only provided fields are sent)."""
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.update_group_hook(
        group_id=group_id,
        hook_id=hook_id,
        url=url,
        name=name,
        description=description,
        token=token,
        enable_ssl_verification=enable_ssl_verification,
        push_events=push_events,
        push_events_branch_filter=push_events_branch_filter,
        issues_events=issues_events,
        confidential_issues_events=confidential_issues_events,
        merge_requests_events=merge_requests_events,
        tag_push_events=tag_push_events,
        note_events=note_events,
        confidential_note_events=confidential_note_events,
        job_events=job_events,
        pipeline_events=pipeline_events,
        wiki_page_events=wiki_page_events,
        deployment_events=deployment_events,
        releases_events=releases_events,
        feature_flag_events=feature_flag_events,
        subgroup_events=subgroup_events,
    )


async def delete_group_hook(
    client: GitLabClient,
    group_id: str | int,
    hook_id: int,
) -> dict[str, Any]:
    """Delete a group webhook."""
    await asyncio.sleep(0)  # Allow event loop to process other tasks
    return client.delete_group_hook(group_id=group_id, hook_id=hook_id)
