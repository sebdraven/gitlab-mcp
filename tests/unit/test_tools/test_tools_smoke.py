"""
Smoke tests for MCP tools layer.

These tests verify that:
1. All tools can be imported successfully
2. Tools have correct signatures (async functions)
3. Server can register and list all tools
"""

import inspect
from unittest.mock import MagicMock

import pytest

from gitlab_mcp import tools
from gitlab_mcp.config.settings import GitLabConfig
from gitlab_mcp.server import GitLabMCPServer


class TestToolsImports:
    """Test that all tools can be imported."""

    def test_context_tools_import(self):
        """Test context tools can be imported."""
        assert hasattr(tools, "get_current_context")
        assert callable(tools.get_current_context)

    def test_repository_tools_import(self):
        """Test repository tools can be imported."""
        assert hasattr(tools, "list_repository_tree")
        assert hasattr(tools, "get_file_contents")
        assert hasattr(tools, "search_code")

    def test_issue_tools_import(self):
        """Test issue tools can be imported."""
        assert hasattr(tools, "list_issues")
        assert hasattr(tools, "get_issue")
        assert hasattr(tools, "create_issue")

    def test_merge_request_tools_import(self):
        """Test merge request tools can be imported."""
        assert hasattr(tools, "list_merge_requests")
        assert hasattr(tools, "get_merge_request")
        assert hasattr(tools, "create_merge_request")
        assert hasattr(tools, "update_merge_request")
        assert hasattr(tools, "merge_merge_request")
        assert hasattr(tools, "close_merge_request")
        assert hasattr(tools, "reopen_merge_request")
        assert hasattr(tools, "approve_merge_request")
        assert hasattr(tools, "unapprove_merge_request")
        assert hasattr(tools, "get_merge_request_changes")
        assert hasattr(tools, "get_merge_request_commits")
        assert hasattr(tools, "get_merge_request_pipelines")

    def test_pipeline_tools_import(self):
        """Test pipeline tools can be imported."""
        assert hasattr(tools, "list_pipelines")
        assert hasattr(tools, "get_pipeline")
        assert hasattr(tools, "create_pipeline")
        assert hasattr(tools, "retry_pipeline")
        assert hasattr(tools, "cancel_pipeline")
        assert hasattr(tools, "delete_pipeline")
        assert hasattr(tools, "list_pipeline_jobs")
        assert hasattr(tools, "get_job")
        assert hasattr(tools, "get_job_trace")
        assert hasattr(tools, "retry_job")
        assert hasattr(tools, "cancel_job")
        assert hasattr(tools, "play_job")
        assert hasattr(tools, "download_job_artifacts")
        assert hasattr(tools, "list_pipeline_variables")

    def test_project_tools_import(self):
        """Test project tools can be imported."""
        assert hasattr(tools, "list_projects")
        assert hasattr(tools, "get_project")
        assert hasattr(tools, "search_projects")
        assert hasattr(tools, "list_project_members")
        assert hasattr(tools, "get_project_statistics")
        assert hasattr(tools, "list_milestones")
        assert hasattr(tools, "get_milestone")
        assert hasattr(tools, "create_milestone")
        assert hasattr(tools, "update_milestone")

    def test_label_tools_import(self):
        """Test label tools can be imported."""
        assert hasattr(tools, "list_labels")
        assert hasattr(tools, "create_label")
        assert hasattr(tools, "update_label")
        assert hasattr(tools, "delete_label")

    def test_wiki_tools_import(self):
        """Test wiki tools can be imported."""
        assert hasattr(tools, "list_wiki_pages")
        assert hasattr(tools, "get_wiki_page")
        assert hasattr(tools, "create_wiki_page")
        assert hasattr(tools, "update_wiki_page")
        assert hasattr(tools, "delete_wiki_page")

    def test_snippet_tools_import(self):
        """Test snippet tools can be imported."""
        assert hasattr(tools, "list_snippets")
        assert hasattr(tools, "get_snippet")
        assert hasattr(tools, "create_snippet")
        assert hasattr(tools, "update_snippet")
        assert hasattr(tools, "delete_snippet")

    def test_release_tools_import(self):
        """Test release tools can be imported."""
        assert hasattr(tools, "list_releases")
        assert hasattr(tools, "get_release")
        assert hasattr(tools, "create_release")
        assert hasattr(tools, "update_release")
        assert hasattr(tools, "delete_release")

    def test_user_tools_import(self):
        """Test user tools can be imported."""
        assert hasattr(tools, "get_user")
        assert hasattr(tools, "search_users")
        assert hasattr(tools, "list_user_projects")

    def test_group_tools_import(self):
        """Test group tools can be imported."""
        assert hasattr(tools, "list_groups")
        assert hasattr(tools, "get_group")
        assert hasattr(tools, "list_group_members")


class TestToolSignatures:
    """Test that tools have correct async signatures."""

    def test_all_tools_are_coroutine_functions(self):
        """Test that all exported tools are async functions."""
        tool_names = [
            "get_current_context",
            "list_repository_tree",
            "get_file_contents",
            "search_code",
            "list_issues",
            "get_issue",
            "create_issue",
            "list_merge_requests",
            "get_merge_request",
            "create_merge_request",
            "list_pipelines",
            "get_pipeline",
            "list_projects",
            "get_project",
            "list_labels",
            "create_label",
            "list_wiki_pages",
            "get_wiki_page",
            "list_snippets",
            "get_snippet",
            "list_releases",
            "get_release",
            "get_user",
            "search_users",
            "list_groups",
            "get_group",
        ]

        for tool_name in tool_names:
            tool_func = getattr(tools, tool_name)
            assert inspect.iscoroutinefunction(tool_func), f"{tool_name} should be async"

    def test_tools_accept_client_parameter(self):
        """Test that all tools accept a client parameter as first arg."""
        tool_names = [
            "list_issues",
            "get_issue",
            "list_projects",
            "list_labels",
        ]

        for tool_name in tool_names:
            tool_func = getattr(tools, tool_name)
            sig = inspect.signature(tool_func)
            params = list(sig.parameters.keys())
            assert params[0] == "client", f"{tool_name} should have 'client' as first parameter"


class TestServerToolRegistration:
    """Test server tool registration functionality."""

    @pytest.fixture
    def mock_config(self):
        """Create a mock GitLab config."""
        config = MagicMock(spec=GitLabConfig)
        config.gitlab_url = "https://gitlab.example.com"
        config.personal_access_token = "fake-token"
        return config

    @pytest.fixture
    def server(self, mock_config):
        """Create a GitLabMCPServer instance."""
        return GitLabMCPServer(config=mock_config)

    def test_server_has_register_all_tools_method(self, server):
        """Test that server has register_all_tools method."""
        assert hasattr(server, "register_all_tools")
        assert callable(server.register_all_tools)

    def test_register_all_tools_adds_67_tools(self, server):
        """Test that register_all_tools registers all 107 tools."""
        # Initially no tools
        assert len(server._tools) == 0

        # Register all tools
        server.register_all_tools()

        # Should have 107 tools registered
        assert len(server._tools) == 107

    def test_all_registered_tools_have_descriptions(self, server):
        """Test that all registered tools have descriptions."""
        server.register_all_tools()

        for tool_name, tool_info in server._tools.items():
            assert "description" in tool_info
            assert tool_info["description"], f"{tool_name} should have non-empty description"

    def test_all_registered_tools_have_functions(self, server):
        """Test that all registered tools have callable functions."""
        server.register_all_tools()

        for tool_name, tool_info in server._tools.items():
            assert "function" in tool_info
            assert callable(tool_info["function"]), f"{tool_name} function should be callable"

    def test_tool_categories_registered(self, server):
        """Test that tools from all categories are registered."""
        server.register_all_tools()

        # Check for tools from each category
        expected_tools = {
            # Context
            "get_current_context",
            # Repositories
            "list_repository_tree",
            "get_file_contents",
            "search_code",
            # Issues
            "list_issues",
            "get_issue",
            "create_issue",
            # Merge Requests
            "list_merge_requests",
            "create_merge_request",
            # Pipelines
            "list_pipelines",
            "get_pipeline",
            # Projects
            "list_projects",
            "get_project",
            # Labels
            "list_labels",
            "create_label",
            # Wikis
            "list_wiki_pages",
            "get_wiki_page",
            # Snippets
            "list_snippets",
            "get_snippet",
            # Releases
            "list_releases",
            "get_release",
            # Users
            "get_user",
            "search_users",
            # Groups
            "list_groups",
            "get_group",
        }

        registered_tools = set(server._tools.keys())
        assert expected_tools.issubset(registered_tools), "All expected tools should be registered"


class TestToolCounts:
    """Test that we have the expected number of tools in each category."""

    def test_total_tool_count(self):
        """Test that __all__ has 111 total exports."""
        # Total MCP tools: 107
        # Context: 1 (get_current_context)
        # Repos: 3 (list_repository_tree, get_file_contents, search_code)
        # Issues: 3 (list_issues, get_issue, create_issue)
        # MRs: 12 (list, get, create, update, merge, close, reopen, approve, unapprove, changes, commits, pipelines)
        # Pipelines: 14 (6 pipeline ops + 7 job ops + 1 variables)
        # Projects: 13 (7 project ops [list, get, create, update, delete, fork, search] + 1 members + 1 stats + 4 milestone ops)
        # Labels: 4 (list, create, update, delete)
        # Wikis: 5 (list, get, create, update, delete)
        # Snippets: 5 (list, get, create, update, delete)
        # Releases: 5 (list, get, create, update, delete)
        # Users: 3 (get, search, list_projects)
        # Groups: 3 (list, get, list_members)
        # Variables (CI/CD project): 5 (list, get, create, update, delete)
        # Environments: 6 (list, get, create, update, delete, stop)
        # Runners (project-level): 5 (list, get, enable, disable, update)
        # Meta-tools (slim mode): 4 (discover_tools, get_tool_schema, execute_tool, TOOL_CATEGORIES)
        # Total: 111 tools (107 regular + 4 meta-tools)
        assert len(tools.__all__) == 111
