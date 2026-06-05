"""GitLab MCP tools package.

This package contains all MCP tool implementations for interacting with GitLab.
Tools are organized by category:
- context: Server and user context
- repositories: Repository operations
- issues: Issue management
- merge_requests: Merge request operations
- pipelines: CI/CD pipeline and job management
- projects: Project management
- labels: Label operations
- wikis: Wiki management
- snippets: Snippet operations
- releases: Release management
- users: User operations
- groups: Group operations

Additionally, provides meta-tools for lazy loading (slim mode):
- discover_tools: List tools by category
- get_tool_schema: Get full schema for a tool
- execute_tool: Execute any tool by name
"""

# Context tools
from gitlab_mcp.tools.context import get_current_context

# CI Lint tools
from gitlab_mcp.tools.ci_lint import (
    lint_ci_yaml,
    validate_project_ci_config,
)

# Environments tools (project-level deployment environments)
from gitlab_mcp.tools.environments import (
    create_environment,
    delete_environment,
    get_environment,
    list_environments,
    stop_environment,
    update_environment,
)

# Group tools
from gitlab_mcp.tools.groups import (
    get_group,
    list_group_members,
    list_groups,
)

# Webhook tools (project + group)
from gitlab_mcp.tools.hooks import (
    create_group_hook,
    create_project_hook,
    delete_group_hook,
    delete_project_hook,
    get_group_hook,
    get_project_hook,
    list_group_hooks,
    list_project_hooks,
    test_project_hook,
    update_group_hook,
    update_project_hook,
)

# Issue tools
from gitlab_mcp.tools.issues import (
    add_issue_comment,
    close_issue,
    create_issue,
    get_issue,
    list_issue_comments,
    list_issues,
    reopen_issue,
    update_issue,
)

# Label tools
from gitlab_mcp.tools.labels import (
    create_label,
    delete_label,
    list_labels,
    update_label,
)

# Merge Request tools
from gitlab_mcp.tools.merge_requests import (
    add_mr_comment,
    approve_merge_request,
    close_merge_request,
    create_merge_request,
    get_merge_request,
    get_merge_request_changes,
    get_merge_request_commits,
    get_merge_request_pipelines,
    list_merge_requests,
    list_mr_comments,
    merge_merge_request,
    reopen_merge_request,
    unapprove_merge_request,
    update_merge_request,
)

# Meta-tools for lazy loading (slim mode)
from gitlab_mcp.tools.meta import (
    TOOL_CATEGORIES,
    discover_tools,
    execute_tool,
    get_tool_schema,
)

# Pipeline tools
from gitlab_mcp.tools.pipelines import (
    cancel_job,
    cancel_pipeline,
    create_pipeline,
    delete_pipeline,
    download_job_artifacts,
    get_job,
    get_job_trace,
    get_pipeline,
    list_pipeline_jobs,
    list_pipeline_variables,
    list_pipelines,
    play_job,
    retry_job,
    retry_pipeline,
)

# Project tools
from gitlab_mcp.tools.projects import (
    create_milestone,
    create_project,
    delete_project,
    fork_project,
    get_milestone,
    get_project,
    get_project_statistics,
    list_milestones,
    list_project_members,
    list_projects,
    search_projects,
    update_milestone,
    update_project,
)

# Protected refs tools (branches + tags)
from gitlab_mcp.tools.protected_refs import (
    get_protected_branch,
    get_protected_tag,
    list_protected_branches,
    list_protected_tags,
    protect_branch,
    protect_tag,
    unprotect_branch,
    unprotect_tag,
    update_protected_branch,
)

# Release tools
from gitlab_mcp.tools.releases import (
    create_release,
    delete_release,
    get_release,
    list_releases,
    update_release,
)

# Repository tools
from gitlab_mcp.tools.repositories import (
    compare_branches,
    create_branch,
    create_file,
    create_tag,
    delete_branch,
    delete_file,
    get_branch,
    get_commit,
    get_file_contents,
    get_tag,
    list_branches,
    list_commits,
    list_repository_tree,
    list_tags,
    search_code,
    update_file,
)

# Runner tools (project-level)
from gitlab_mcp.tools.runners import (
    disable_project_runner,
    enable_project_runner,
    get_runner,
    list_project_runners,
    update_runner,
)

# Search tools (cross-projects, group-scoped, project-scoped)
from gitlab_mcp.tools.search import (
    search_globally,
    search_in_group,
    search_in_project,
)

# Snippet tools
from gitlab_mcp.tools.snippets import (
    create_snippet,
    delete_snippet,
    get_snippet,
    list_snippets,
    update_snippet,
)

# User tools
from gitlab_mcp.tools.users import (
    get_user,
    list_user_projects,
    search_users,
)

# Variables tools (CI/CD project variables)
from gitlab_mcp.tools.variables import (
    create_project_variable,
    delete_project_variable,
    get_project_variable,
    list_project_variables,
    update_project_variable,
)

# Wiki tools
from gitlab_mcp.tools.wikis import (
    create_wiki_page,
    delete_wiki_page,
    get_wiki_page,
    list_wiki_pages,
    update_wiki_page,
)

__all__ = [
    # Context
    "get_current_context",
    # Repositories
    "list_repository_tree",
    "get_file_contents",
    "search_code",
    "create_file",
    "update_file",
    "delete_file",
    "list_branches",
    "get_branch",
    "create_branch",
    "delete_branch",
    "get_commit",
    "list_commits",
    "compare_branches",
    "list_tags",
    "get_tag",
    "create_tag",
    # Issues
    "list_issues",
    "get_issue",
    "create_issue",
    "update_issue",
    "close_issue",
    "reopen_issue",
    "add_issue_comment",
    "list_issue_comments",
    # Merge Requests
    "list_merge_requests",
    "get_merge_request",
    "create_merge_request",
    "update_merge_request",
    "merge_merge_request",
    "close_merge_request",
    "reopen_merge_request",
    "approve_merge_request",
    "unapprove_merge_request",
    "get_merge_request_changes",
    "get_merge_request_commits",
    "get_merge_request_pipelines",
    "add_mr_comment",
    "list_mr_comments",
    # Pipelines
    "list_pipelines",
    "get_pipeline",
    "create_pipeline",
    "retry_pipeline",
    "cancel_pipeline",
    "delete_pipeline",
    "list_pipeline_jobs",
    "get_job",
    "get_job_trace",
    "retry_job",
    "cancel_job",
    "play_job",
    "download_job_artifacts",
    "list_pipeline_variables",
    # Projects
    "list_projects",
    "get_project",
    "create_project",
    "update_project",
    "delete_project",
    "fork_project",
    "search_projects",
    "list_project_members",
    "get_project_statistics",
    "list_milestones",
    "get_milestone",
    "create_milestone",
    "update_milestone",
    # Labels
    "list_labels",
    "create_label",
    "update_label",
    "delete_label",
    # Wikis
    "list_wiki_pages",
    "get_wiki_page",
    "create_wiki_page",
    "update_wiki_page",
    "delete_wiki_page",
    # Snippets
    "list_snippets",
    "get_snippet",
    "create_snippet",
    "update_snippet",
    "delete_snippet",
    # Releases
    "list_releases",
    "get_release",
    "create_release",
    "update_release",
    "delete_release",
    # Users
    "get_user",
    "search_users",
    "list_user_projects",
    # Groups
    "list_groups",
    "get_group",
    "list_group_members",
    # Variables (CI/CD project-level)
    "list_project_variables",
    "get_project_variable",
    "create_project_variable",
    "update_project_variable",
    "delete_project_variable",
    # Environments (project-level)
    "list_environments",
    "get_environment",
    "create_environment",
    "update_environment",
    "delete_environment",
    "stop_environment",
    # Runners (project-level)
    "list_project_runners",
    "get_runner",
    "enable_project_runner",
    "disable_project_runner",
    "update_runner",
    # CI Lint
    "lint_ci_yaml",
    "validate_project_ci_config",
    # Protected refs (branches + tags)
    "list_protected_branches",
    "get_protected_branch",
    "protect_branch",
    "update_protected_branch",
    "unprotect_branch",
    "list_protected_tags",
    "get_protected_tag",
    "protect_tag",
    "unprotect_tag",
    # Search (global / group / project)
    "search_globally",
    "search_in_group",
    "search_in_project",
    # Webhooks (project + group)
    "list_project_hooks",
    "get_project_hook",
    "create_project_hook",
    "update_project_hook",
    "delete_project_hook",
    "test_project_hook",
    "list_group_hooks",
    "get_group_hook",
    "create_group_hook",
    "update_group_hook",
    "delete_group_hook",
    # Meta-tools (slim mode)
    "discover_tools",
    "get_tool_schema",
    "execute_tool",
    "TOOL_CATEGORIES",
]
