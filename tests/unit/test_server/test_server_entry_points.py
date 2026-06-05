"""
Unit tests for MCP server entry points and tool definitions.

Tests the async_main(), main(), and _get_tool_definitions() functions.
Following TDD: These tests are written FIRST (RED phase).
"""

from unittest.mock import AsyncMock, Mock, patch

import pytest

from gitlab_mcp.server import _build_tool_schema, _get_tool_definitions, main


class TestToolDefinitions:
    """Test _get_tool_definitions function."""

    def test_get_tool_definitions_returns_list(self) -> None:
        """Test that _get_tool_definitions returns a list."""
        tool_defs = _get_tool_definitions()

        assert isinstance(tool_defs, list)

    def test_get_tool_definitions_has_67_tools(self) -> None:
        """Test that _get_tool_definitions returns exactly 132 tools."""
        tool_defs = _get_tool_definitions()

        assert len(tool_defs) == 132

    def test_tool_definition_structure(self) -> None:
        """Test that each tool definition has correct structure."""
        tool_defs = _get_tool_definitions()

        for tool_def in tool_defs:
            # Each tool definition should be a tuple of (name, description, params_schema)
            assert isinstance(tool_def, tuple)
            assert len(tool_def) == 3

            name, description, params_schema = tool_def
            assert isinstance(name, str)
            assert isinstance(description, str)
            assert isinstance(params_schema, dict)

    def test_tool_names_are_unique(self) -> None:
        """Test that all tool names are unique."""
        tool_defs = _get_tool_definitions()
        tool_names = [name for name, _, _ in tool_defs]

        assert len(tool_names) == len(set(tool_names)), "Tool names must be unique"

    def test_context_tools(self) -> None:
        """Test that context tools are defined."""
        tool_defs = _get_tool_definitions()
        tool_names = {name for name, _, _ in tool_defs}

        expected_context_tools = {"get_current_context"}
        assert expected_context_tools.issubset(tool_names)

    def test_repository_tools(self) -> None:
        """Test that repository tools are defined."""
        tool_defs = _get_tool_definitions()
        tool_names = {name for name, _, _ in tool_defs}

        expected_repo_tools = {"list_repository_tree", "get_file_contents", "search_code"}
        assert expected_repo_tools.issubset(tool_names)

    def test_issue_tools(self) -> None:
        """Test that issue tools are defined."""
        tool_defs = _get_tool_definitions()
        tool_names = {name for name, _, _ in tool_defs}

        expected_issue_tools = {"list_issues", "get_issue", "create_issue"}
        assert expected_issue_tools.issubset(tool_names)

    def test_merge_request_tools(self) -> None:
        """Test that merge request tools are defined."""
        tool_defs = _get_tool_definitions()
        tool_names = {name for name, _, _ in tool_defs}

        expected_mr_tools = {
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
        }
        assert expected_mr_tools.issubset(tool_names)

    def test_pipeline_tools(self) -> None:
        """Test that pipeline tools are defined."""
        tool_defs = _get_tool_definitions()
        tool_names = {name for name, _, _ in tool_defs}

        expected_pipeline_tools = {
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
        }
        assert expected_pipeline_tools.issubset(tool_names)

    def test_project_tools(self) -> None:
        """Test that project tools are defined."""
        tool_defs = _get_tool_definitions()
        tool_names = {name for name, _, _ in tool_defs}

        expected_project_tools = {
            "list_projects",
            "get_project",
            "search_projects",
            "list_project_members",
            "get_project_statistics",
            "list_milestones",
            "get_milestone",
            "create_milestone",
            "update_milestone",
        }
        assert expected_project_tools.issubset(tool_names)

    def test_label_tools(self) -> None:
        """Test that label tools are defined."""
        tool_defs = _get_tool_definitions()
        tool_names = {name for name, _, _ in tool_defs}

        expected_label_tools = {"list_labels", "create_label", "update_label", "delete_label"}
        assert expected_label_tools.issubset(tool_names)

    def test_wiki_tools(self) -> None:
        """Test that wiki tools are defined."""
        tool_defs = _get_tool_definitions()
        tool_names = {name for name, _, _ in tool_defs}

        expected_wiki_tools = {
            "list_wiki_pages",
            "get_wiki_page",
            "create_wiki_page",
            "update_wiki_page",
            "delete_wiki_page",
        }
        assert expected_wiki_tools.issubset(tool_names)

    def test_snippet_tools(self) -> None:
        """Test that snippet tools are defined."""
        tool_defs = _get_tool_definitions()
        tool_names = {name for name, _, _ in tool_defs}

        expected_snippet_tools = {
            "list_snippets",
            "get_snippet",
            "create_snippet",
            "update_snippet",
            "delete_snippet",
        }
        assert expected_snippet_tools.issubset(tool_names)

    def test_release_tools(self) -> None:
        """Test that release tools are defined."""
        tool_defs = _get_tool_definitions()
        tool_names = {name for name, _, _ in tool_defs}

        expected_release_tools = {
            "list_releases",
            "get_release",
            "create_release",
            "update_release",
            "delete_release",
        }
        assert expected_release_tools.issubset(tool_names)

    def test_user_tools(self) -> None:
        """Test that user tools are defined."""
        tool_defs = _get_tool_definitions()
        tool_names = {name for name, _, _ in tool_defs}

        expected_user_tools = {"get_user", "search_users", "list_user_projects"}
        assert expected_user_tools.issubset(tool_names)

    def test_group_tools(self) -> None:
        """Test that group tools are defined."""
        tool_defs = _get_tool_definitions()
        tool_names = {name for name, _, _ in tool_defs}

        expected_group_tools = {"list_groups", "get_group", "list_group_members"}
        assert expected_group_tools.issubset(tool_names)

    def test_tool_parameter_schemas_valid(self) -> None:
        """Test that tool parameter schemas are valid JSON schema objects."""
        tool_defs = _get_tool_definitions()

        for name, _description, params_schema in tool_defs:
            # Each parameter should have type and description
            for param_name, param_def in params_schema.items():
                assert "type" in param_def, f"Parameter {param_name} in {name} missing 'type'"
                assert (
                    "description" in param_def
                ), f"Parameter {param_name} in {name} missing 'description'"

                # Type should be a valid JSON schema type
                valid_types = ["string", "integer", "boolean", "array", "object", "number"]
                assert (
                    param_def["type"] in valid_types
                ), f"Parameter {param_name} in {name} has invalid type: {param_def['type']}"


class TestMainEntryPoint:
    """Test main() CLI entry point."""

    @patch("gitlab_mcp.server.asyncio.run")
    @patch("gitlab_mcp.server.parse_args")
    def test_main_calls_asyncio_run(self, mock_parse_args: Mock, mock_asyncio_run: Mock) -> None:
        """Test that main() calls asyncio.run with async_main."""
        # Mock parse_args to return default arguments
        mock_args = Mock()
        mock_args.transport = "stdio"
        mock_args.host = "127.0.0.1"
        mock_args.port = 8000
        mock_args.mode = "full"
        mock_parse_args.return_value = mock_args

        main()

        # Verify parse_args was called
        mock_parse_args.assert_called_once()

        # Verify asyncio.run was called with async_main coroutine
        mock_asyncio_run.assert_called_once()
        # The argument should be the async_main coroutine
        call_args = mock_asyncio_run.call_args[0]
        assert len(call_args) == 1
        # Check it's a coroutine by checking if it has a cr_code attribute
        assert hasattr(call_args[0], "cr_code") or hasattr(call_args[0], "__await__")

    @patch("gitlab_mcp.server.asyncio.run")
    @patch("gitlab_mcp.server.parse_args")
    def test_main_passes_transport_args(
        self, mock_parse_args: Mock, mock_asyncio_run: Mock
    ) -> None:
        """Test that main() passes transport arguments to async_main."""
        # Mock parse_args to return HTTP transport arguments
        mock_args = Mock()
        mock_args.transport = "http"
        mock_args.host = "0.0.0.0"
        mock_args.port = 9000
        mock_args.mode = "slim"
        mock_parse_args.return_value = mock_args

        main()

        # Verify asyncio.run was called
        mock_asyncio_run.assert_called_once()
        # The coroutine should be created with the specified arguments
        call_args = mock_asyncio_run.call_args[0]
        assert len(call_args) == 1


class TestAsyncMainEntryPoint:
    """Test async_main() entry point."""

    @pytest.mark.asyncio
    @patch("gitlab_mcp.server.load_config")
    @patch("gitlab_mcp.server.stdio_server")
    @patch("gitlab_mcp.server.Server")
    @patch("gitlab_mcp.server.GitLabClient")
    async def test_async_main_loads_config(
        self,
        mock_gitlab_client: Mock,
        mock_server: Mock,
        mock_stdio_server: Mock,
        mock_load_config: Mock,
    ) -> None:
        """Test that async_main loads configuration."""
        from gitlab_mcp.config.settings import GitLabConfig

        # Setup mocks
        mock_config = GitLabConfig(
            gitlab_url="https://gitlab.example.com",
            gitlab_token="test-token",
        )
        mock_load_config.return_value = mock_config

        # Mock client authentication
        mock_client_instance = Mock()
        mock_client_instance.authenticate = Mock()
        mock_gitlab_client.return_value = mock_client_instance

        # Mock server and stdio_server context manager
        mock_server_instance = Mock()
        mock_server.return_value = mock_server_instance
        mock_server_instance.run = AsyncMock()
        mock_server_instance.create_initialization_options = Mock(return_value={})

        # Mock stdio_server as async context manager
        mock_stdio_instance = AsyncMock()
        mock_stdio_instance.__aenter__ = AsyncMock(return_value=(Mock(), Mock()))
        mock_stdio_instance.__aexit__ = AsyncMock(return_value=None)
        mock_stdio_server.return_value = mock_stdio_instance

        # Call async_main
        from gitlab_mcp.server import async_main

        await async_main()

        # Verify config was loaded
        mock_load_config.assert_called_once()

    @pytest.mark.asyncio
    @patch("gitlab_mcp.server.load_config")
    @patch("gitlab_mcp.server.stdio_server")
    @patch("gitlab_mcp.server.Server")
    @patch("gitlab_mcp.server.GitLabClient")
    async def test_async_main_creates_client(
        self,
        mock_gitlab_client: Mock,
        mock_server: Mock,
        mock_stdio_server: Mock,
        mock_load_config: Mock,
    ) -> None:
        """Test that async_main creates GitLab client."""
        from gitlab_mcp.config.settings import GitLabConfig

        # Setup mocks
        mock_config = GitLabConfig(
            gitlab_url="https://gitlab.example.com",
            gitlab_token="test-token",
        )
        mock_load_config.return_value = mock_config

        # Mock client authentication
        mock_client_instance = Mock()
        mock_client_instance.authenticate = Mock()
        mock_gitlab_client.return_value = mock_client_instance

        # Mock server and stdio_server
        mock_server_instance = Mock()
        mock_server.return_value = mock_server_instance
        mock_server_instance.run = AsyncMock()
        mock_server_instance.create_initialization_options = Mock(return_value={})

        mock_stdio_instance = AsyncMock()
        mock_stdio_instance.__aenter__ = AsyncMock(return_value=(Mock(), Mock()))
        mock_stdio_instance.__aexit__ = AsyncMock(return_value=None)
        mock_stdio_server.return_value = mock_stdio_instance

        # Call async_main
        from gitlab_mcp.server import async_main

        await async_main()

        # Verify client was created with config
        mock_gitlab_client.assert_called_once_with(mock_config)
        # Verify client was authenticated
        mock_client_instance.authenticate.assert_called_once()

    @pytest.mark.asyncio
    @patch("gitlab_mcp.server.load_config")
    @patch("builtins.print")  # Mock print to avoid stderr output
    @patch("gitlab_mcp.server.GitLabClient")
    async def test_async_main_exits_on_auth_failure(
        self,
        mock_gitlab_client: Mock,
        mock_print: Mock,
        mock_load_config: Mock,
    ) -> None:
        """Test that async_main handles authentication failure gracefully."""
        from gitlab_mcp.config.settings import GitLabConfig

        # Setup mocks
        mock_config = GitLabConfig(
            gitlab_url="https://gitlab.example.com",
            gitlab_token="invalid-token",
        )
        mock_load_config.return_value = mock_config

        # Mock client authentication failure
        mock_client_instance = Mock()
        mock_client_instance.authenticate = Mock(side_effect=Exception("Authentication failed"))
        mock_gitlab_client.return_value = mock_client_instance

        # Call async_main - it will call sys.exit(1) which will raise SystemExit
        from gitlab_mcp.server import async_main

        with pytest.raises(SystemExit) as exc_info:
            await async_main()

        # Verify sys.exit was called with error code 1
        assert exc_info.value.code == 1


class TestBuildToolSchema:
    """Test _build_tool_schema helper function."""

    def test_empty_params_schema(self) -> None:
        """Test that empty params schema returns basic object schema."""
        result = _build_tool_schema({})

        assert result == {"type": "object", "properties": {}}
        assert "required" not in result

    def test_single_required_param(self) -> None:
        """Test that parameter without 'optional' is marked as required."""
        params_schema = {
            "project_id": {
                "type": "string",
                "description": "Project ID or path",
            }
        }

        result = _build_tool_schema(params_schema)

        assert result["type"] == "object"
        assert "project_id" in result["properties"]
        assert result["properties"]["project_id"]["type"] == "string"
        assert result["required"] == ["project_id"]

    def test_single_optional_param(self) -> None:
        """Test that parameter with 'optional' in description is not required."""
        params_schema = {
            "page": {
                "type": "integer",
                "description": "Page number (optional, default: 1)",
            }
        }

        result = _build_tool_schema(params_schema)

        assert result["type"] == "object"
        assert "page" in result["properties"]
        assert "required" not in result

    def test_mixed_required_and_optional_params(self) -> None:
        """Test schema with both required and optional parameters."""
        params_schema = {
            "project_id": {
                "type": "string",
                "description": "Project ID or path",
            },
            "page": {
                "type": "integer",
                "description": "Page number (optional, default: 1)",
            },
            "branch": {
                "type": "string",
                "description": "Branch name",
            },
            "per_page": {
                "type": "integer",
                "description": "Results per page (optional, default: 20)",
            },
        }

        result = _build_tool_schema(params_schema)

        assert result["type"] == "object"
        assert len(result["properties"]) == 4
        # Only project_id and branch should be required
        assert set(result["required"]) == {"project_id", "branch"}

    def test_optional_case_insensitive(self) -> None:
        """Test that 'Optional' (capital O) in description marks param as optional."""
        params_schema = {
            "filter": {
                "type": "string",
                "description": "Filter string (Optional)",
            }
        }

        result = _build_tool_schema(params_schema)

        assert "required" not in result

    def test_param_definitions_are_copied(self) -> None:
        """Test that original param definitions are copied, not referenced."""
        params_schema = {
            "test_param": {
                "type": "string",
                "description": "Test parameter",
            }
        }

        result = _build_tool_schema(params_schema)

        # Modify the result and verify original is unchanged
        result["properties"]["test_param"]["modified"] = True
        assert "modified" not in params_schema["test_param"]

    def test_param_without_description(self) -> None:
        """Test parameter without description is treated as required."""
        params_schema = {
            "id": {
                "type": "integer",
            }
        }

        result = _build_tool_schema(params_schema)

        # Param without description defaults to required (no "optional" found)
        assert result["required"] == ["id"]


class TestSchemaDescriptionConstants:
    """Test schema description constants for SonarQube S1192 compliance."""

    def test_desc_project_id_constant(self) -> None:
        """Test DESC_PROJECT_ID constant has expected value."""
        from gitlab_mcp.server import DESC_PROJECT_ID

        assert DESC_PROJECT_ID == "Project ID or path (e.g., 'group/project')"
        assert isinstance(DESC_PROJECT_ID, str)

    def test_desc_page_constant(self) -> None:
        """Test DESC_PAGE constant has expected value."""
        from gitlab_mcp.server import DESC_PAGE

        assert DESC_PAGE == "Page number (optional, default: 1)"
        assert "optional" in DESC_PAGE.lower()

    def test_desc_per_page_constant(self) -> None:
        """Test DESC_PER_PAGE constant has expected value."""
        from gitlab_mcp.server import DESC_PER_PAGE

        assert DESC_PER_PAGE == "Results per page (optional, default: 20)"
        assert "optional" in DESC_PER_PAGE.lower()

    def test_desc_mr_iid_constant(self) -> None:
        """Test DESC_MR_IID constant has expected value."""
        from gitlab_mcp.server import DESC_MR_IID

        assert DESC_MR_IID == "Merge request IID (internal ID)"
        assert "IID" in DESC_MR_IID

    def test_desc_issue_iid_constant(self) -> None:
        """Test DESC_ISSUE_IID constant has expected value."""
        from gitlab_mcp.server import DESC_ISSUE_IID

        assert DESC_ISSUE_IID == "Issue IID (internal ID)"
        assert "IID" in DESC_ISSUE_IID

    def test_desc_pipeline_id_constant(self) -> None:
        """Test DESC_PIPELINE_ID constant has expected value."""
        from gitlab_mcp.server import DESC_PIPELINE_ID

        assert DESC_PIPELINE_ID == "Pipeline ID"

    def test_desc_job_id_constant(self) -> None:
        """Test DESC_JOB_ID constant has expected value."""
        from gitlab_mcp.server import DESC_JOB_ID

        assert DESC_JOB_ID == "Job ID"

    def test_desc_new_title_constant(self) -> None:
        """Test DESC_NEW_TITLE constant has expected value."""
        from gitlab_mcp.server import DESC_NEW_TITLE

        assert DESC_NEW_TITLE == "New title (optional)"
        assert "optional" in DESC_NEW_TITLE.lower()

    def test_desc_new_desc_constant(self) -> None:
        """Test DESC_NEW_DESC constant has expected value."""
        from gitlab_mcp.server import DESC_NEW_DESC

        assert DESC_NEW_DESC == "New description (optional)"
        assert "optional" in DESC_NEW_DESC.lower()

    def test_desc_wiki_slug_constant(self) -> None:
        """Test DESC_WIKI_SLUG constant has expected value."""
        from gitlab_mcp.server import DESC_WIKI_SLUG

        assert DESC_WIKI_SLUG == "Wiki page slug (URL-friendly identifier)"

    def test_desc_snippet_id_constant(self) -> None:
        """Test DESC_SNIPPET_ID constant has expected value."""
        from gitlab_mcp.server import DESC_SNIPPET_ID

        assert DESC_SNIPPET_ID == "Snippet ID"

    def test_desc_tag_name_constant(self) -> None:
        """Test DESC_TAG_NAME constant has expected value."""
        from gitlab_mcp.server import DESC_TAG_NAME

        assert DESC_TAG_NAME == "Git tag name"

    def test_desc_tag_release_constant(self) -> None:
        """Test DESC_TAG_RELEASE constant has expected value."""
        from gitlab_mcp.server import DESC_TAG_RELEASE

        assert DESC_TAG_RELEASE == "Git tag name associated with release"

    def test_desc_search_query_constant(self) -> None:
        """Test DESC_SEARCH_QUERY constant has expected value."""
        from gitlab_mcp.server import DESC_SEARCH_QUERY

        assert DESC_SEARCH_QUERY == "Search query string"

    def test_desc_author_email_constant(self) -> None:
        """Test DESC_AUTHOR_EMAIL constant has expected value."""
        from gitlab_mcp.server import DESC_AUTHOR_EMAIL

        assert DESC_AUTHOR_EMAIL == "Email of commit author (optional)"
        assert "optional" in DESC_AUTHOR_EMAIL.lower()

    def test_desc_author_name_constant(self) -> None:
        """Test DESC_AUTHOR_NAME constant has expected value."""
        from gitlab_mcp.server import DESC_AUTHOR_NAME

        assert DESC_AUTHOR_NAME == "Name of commit author (optional)"
        assert "optional" in DESC_AUTHOR_NAME.lower()

    def test_desc_source_ref_constant(self) -> None:
        """Test DESC_SOURCE_REF constant has expected value."""
        from gitlab_mcp.server import DESC_SOURCE_REF

        assert DESC_SOURCE_REF == "Source branch, tag, or commit SHA"

    def test_all_constants_are_strings(self) -> None:
        """Test that all schema description constants are strings."""
        from gitlab_mcp.server import (
            DESC_AUTHOR_EMAIL,
            DESC_AUTHOR_NAME,
            DESC_ISSUE_IID,
            DESC_JOB_ID,
            DESC_MR_IID,
            DESC_NEW_DESC,
            DESC_NEW_TITLE,
            DESC_PAGE,
            DESC_PER_PAGE,
            DESC_PIPELINE_ID,
            DESC_PROJECT_ID,
            DESC_SEARCH_QUERY,
            DESC_SNIPPET_ID,
            DESC_SOURCE_REF,
            DESC_TAG_NAME,
            DESC_TAG_RELEASE,
            DESC_WIKI_SLUG,
        )

        constants = [
            DESC_PROJECT_ID,
            DESC_PAGE,
            DESC_PER_PAGE,
            DESC_MR_IID,
            DESC_ISSUE_IID,
            DESC_PIPELINE_ID,
            DESC_JOB_ID,
            DESC_NEW_TITLE,
            DESC_NEW_DESC,
            DESC_WIKI_SLUG,
            DESC_SNIPPET_ID,
            DESC_TAG_NAME,
            DESC_TAG_RELEASE,
            DESC_SEARCH_QUERY,
            DESC_AUTHOR_EMAIL,
            DESC_AUTHOR_NAME,
            DESC_SOURCE_REF,
        ]

        for const in constants:
            assert isinstance(const, str)
            assert len(const) > 0
