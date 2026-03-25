"""
Meta-tools for lazy tool loading (slim mode).

This module provides 3 meta-tools that replace the 87 direct GitLab tools,
reducing context window usage by ~95%. Clients can:
1. Discover available tools by category
2. Get full schema for a specific tool
3. Execute any tool by name

This implements the lazy-mcp pattern for tool management.
"""

from typing import Any

from gitlab_mcp.client.gitlab_client import GitLabClient

# Tool categories with their member tools
TOOL_CATEGORIES: dict[str, dict[str, Any]] = {
    "context": {
        "description": "Server and user context information",
        "tools": ["get_current_context"],
    },
    "repositories": {
        "description": "File, branch, commit, and tag operations",
        "tools": [
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
        ],
    },
    "issues": {
        "description": "Issue creation, updates, and comments",
        "tools": [
            "list_issues",
            "get_issue",
            "create_issue",
            "update_issue",
            "close_issue",
            "reopen_issue",
            "add_issue_comment",
            "list_issue_comments",
        ],
    },
    "merge_requests": {
        "description": "Merge request operations, approvals, and reviews",
        "tools": [
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
        ],
    },
    "pipelines": {
        "description": "CI/CD pipeline and job management",
        "tools": [
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
        ],
    },
    "projects": {
        "description": "Project management and milestones",
        "tools": [
            "list_projects",
            "get_project",
            "create_project",
            "search_projects",
            "list_project_members",
            "get_project_statistics",
            "list_milestones",
            "get_milestone",
            "create_milestone",
            "update_milestone",
        ],
    },
    "labels": {
        "description": "Label management",
        "tools": [
            "list_labels",
            "create_label",
            "update_label",
            "delete_label",
        ],
    },
    "wikis": {
        "description": "Wiki page management",
        "tools": [
            "list_wiki_pages",
            "get_wiki_page",
            "create_wiki_page",
            "update_wiki_page",
            "delete_wiki_page",
        ],
    },
    "snippets": {
        "description": "Code snippet management",
        "tools": [
            "list_snippets",
            "get_snippet",
            "create_snippet",
            "update_snippet",
            "delete_snippet",
        ],
    },
    "releases": {
        "description": "Release management",
        "tools": [
            "list_releases",
            "get_release",
            "create_release",
            "update_release",
            "delete_release",
        ],
    },
    "users": {
        "description": "User information and search",
        "tools": [
            "get_user",
            "search_users",
            "list_user_projects",
        ],
    },
    "groups": {
        "description": "Group information and members",
        "tools": [
            "list_groups",
            "get_group",
            "list_group_members",
        ],
    },
}


def _get_all_tool_names() -> list[str]:
    """Get all tool names across all categories."""
    tools = []
    for category in TOOL_CATEGORIES.values():
        tools.extend(category["tools"])
    return tools


def _get_tool_definitions_map() -> dict[str, tuple[str, dict[str, Any]]]:
    """
    Get a map of tool name to (description, schema) from server's tool definitions.

    This lazily imports and caches the tool definitions from the server module.
    """
    # Import here to avoid circular dependency
    from gitlab_mcp.server import _get_tool_definitions

    tool_defs = _get_tool_definitions()
    return {name: (desc, schema) for name, desc, schema in tool_defs}


async def discover_tools(
    client: GitLabClient,
    category: str | None = None,
) -> dict[str, Any]:
    """
    Discover available GitLab tools by category.

    This meta-tool helps you find which tools are available before requesting
    their full schemas. Use this to explore the GitLab MCP capabilities.

    Args:
        client: GitLab client (unused but required for tool signature)
        category: Optional category to filter. If None, returns all categories.
                  Valid categories: context, repositories, issues, merge_requests,
                  pipelines, projects, labels, wikis, snippets, releases, users, groups

    Returns:
        Dictionary with:
        - categories: List of category info (if no category specified)
        - category: Category name (if category specified)
        - tools: List of tool names in the category
        - total_tools: Total count of tools
    """
    if category is not None:
        if category not in TOOL_CATEGORIES:
            return {
                "error": f"Unknown category: {category}",
                "valid_categories": list(TOOL_CATEGORIES.keys()),
            }

        cat_info = TOOL_CATEGORIES[category]
        tool_defs = _get_tool_definitions_map()

        # Get tool info with descriptions
        tools_info = []
        for tool_name in cat_info["tools"]:
            if tool_name in tool_defs:
                desc, _ = tool_defs[tool_name]
                tools_info.append({"name": tool_name, "description": desc})
            else:
                tools_info.append({"name": tool_name, "description": "No description"})

        return {
            "category": category,
            "description": cat_info["description"],
            "tools": tools_info,
            "tool_count": len(cat_info["tools"]),
        }

    # Return all categories
    categories = []
    total_tools = 0
    for cat_name, cat_info in TOOL_CATEGORIES.items():
        tool_count = len(cat_info["tools"])
        total_tools += tool_count
        categories.append(
            {
                "name": cat_name,
                "description": cat_info["description"],
                "tool_count": tool_count,
            }
        )

    return {
        "categories": categories,
        "total_categories": len(categories),
        "total_tools": total_tools,
    }


async def get_tool_schema(
    client: GitLabClient,
    tool_name: str,
) -> dict[str, Any]:
    """
    Get the full JSON schema for a specific GitLab tool.

    Use this after discovering tools to get the complete input schema
    before calling execute_tool.

    Args:
        client: GitLab client (unused but required for tool signature)
        tool_name: Name of the tool to get schema for (e.g., "list_merge_requests")

    Returns:
        Dictionary with:
        - name: Tool name
        - description: Tool description
        - inputSchema: Complete JSON schema for the tool's parameters
        - category: Which category this tool belongs to
    """
    # Find which category this tool belongs to
    tool_category = None
    for cat_name, cat_info in TOOL_CATEGORIES.items():
        if tool_name in cat_info["tools"]:
            tool_category = cat_name
            break

    if tool_category is None:
        all_tools = _get_all_tool_names()
        return {
            "error": f"Unknown tool: {tool_name}",
            "hint": "Use discover_tools() to see available tools",
            "available_tools_count": len(all_tools),
        }

    # Get the tool definition
    tool_defs = _get_tool_definitions_map()
    if tool_name not in tool_defs:
        return {
            "error": f"Tool definition not found: {tool_name}",
            "category": tool_category,
        }

    description, params_schema = tool_defs[tool_name]

    # Build the full input schema (same logic as server._build_tool_schema)
    input_schema: dict[str, Any] = {
        "type": "object",
        "properties": {},
    }

    required = []
    for param_name, param_def in params_schema.items():
        input_schema["properties"][param_name] = param_def
        # Parameters without "optional" in description are required
        if "optional" not in param_def.get("description", "").lower():
            required.append(param_name)

    if required:
        input_schema["required"] = required

    return {
        "name": tool_name,
        "description": description,
        "category": tool_category,
        "inputSchema": input_schema,
    }


async def execute_tool(
    client: GitLabClient,
    tool_name: str,
    arguments: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """
    Execute any GitLab tool by name.

    Use this after getting the schema to actually run a tool.
    This routes to the actual tool implementation.

    Args:
        client: GitLab client for API operations
        tool_name: Name of the tool to execute (e.g., "list_merge_requests")
        arguments: Tool-specific arguments matching the inputSchema

    Returns:
        The result from the executed tool
    """
    # Validate tool exists
    all_tools = _get_all_tool_names()
    if tool_name not in all_tools:
        return {
            "error": f"Unknown tool: {tool_name}",
            "hint": "Use discover_tools() to see available tools",
        }

    # Import tools module and get the function
    from gitlab_mcp import tools

    tool_func = getattr(tools, tool_name, None)
    if tool_func is None:
        return {
            "error": f"Tool function not found: {tool_name}",
            "hint": "Tool may not be properly exported",
        }

    # Execute the tool
    args = arguments or {}
    try:
        result: dict[str, Any] = await tool_func(client, **args)
        return result
    except TypeError as e:
        return {
            "error": f"Invalid arguments for {tool_name}",
            "hint": "Use get_tool_schema() to see required parameters",
        }
    except Exception:
        return {
            "error": f"Error executing {tool_name}: operation failed",
            "tool": tool_name,
        }


# Export the meta-tools
__all__ = [
    "discover_tools",
    "get_tool_schema",
    "execute_tool",
    "TOOL_CATEGORIES",
]
