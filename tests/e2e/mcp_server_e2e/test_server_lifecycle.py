"""
Test MCP server lifecycle (startup, shutdown, tool listing).

These tests verify that:
1. Server can start up and authenticate with GitLab
2. Server can list all registered tools
3. Server provides correct metadata
4. Server can shut down gracefully
"""

from unittest.mock import MagicMock, patch

import pytest

from gitlab_mcp.config.settings import GitLabConfig
from gitlab_mcp.server import GitLabMCPServer


@pytest.mark.e2e
class TestServerLifecycle:
    """Test MCP server lifecycle operations."""

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

    @pytest.mark.asyncio
    async def test_server_startup_authenticates(self, server):
        """Test that server startup authenticates with GitLab."""
        # Mock the authenticate method
        with patch.object(server.gitlab_client, "authenticate") as mock_auth:
            await server.startup()
            mock_auth.assert_called_once()

    @pytest.mark.asyncio
    async def test_server_shutdown_completes(self, server):
        """Test that server shutdown completes without errors."""
        # Should complete without raising exceptions
        await server.shutdown()

    @pytest.mark.asyncio
    async def test_server_list_tools_before_registration(self, server):
        """Test that list_tools returns empty list before registration."""
        tools = await server.list_tools()
        assert tools == []

    @pytest.mark.asyncio
    async def test_server_list_tools_after_registration(self, server):
        """Test that list_tools returns all tools after registration."""
        server.register_all_tools()
        tools = await server.list_tools()

        # Should have 139 tools (132 + 7 MR discussions)
        assert len(tools) == 139

        # Each tool should have name and description
        for tool in tools:
            assert "name" in tool
            assert "description" in tool
            assert tool["name"]
            assert tool["description"]

    def test_server_get_info(self, server):
        """Test that get_info returns server metadata."""
        info = server.get_info()

        assert "name" in info
        assert "version" in info
        assert "description" in info
        assert info["name"] == "gitlab-mcp-server"
        assert info["version"] == "0.1.0"
        assert "GitLab MCP Server" in info["description"]


@pytest.mark.e2e
class TestServerToolRegistration:
    """Test tool registration functionality."""

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

    def test_register_single_tool(self, server):
        """Test registering a single tool."""

        async def dummy_tool(**kwargs):
            return {"result": "success"}

        server.register_tool("test_tool", "A test tool", dummy_tool)

        assert "test_tool" in server._tools
        assert server._tools["test_tool"]["name"] == "test_tool"
        assert server._tools["test_tool"]["description"] == "A test tool"
        assert server._tools["test_tool"]["function"] == dummy_tool

    def test_register_all_tools_creates_67_tools(self, server):
        """Test that register_all_tools creates all 139 tools."""
        server.register_all_tools()
        assert len(server._tools) == 139

    @pytest.mark.asyncio
    async def test_registered_tools_are_callable(self, server):
        """Test that registered tool functions are callable."""

        async def dummy_tool(**kwargs):
            return {"result": "success"}

        server.register_tool("test_tool", "A test tool", dummy_tool)

        # Tool function should be callable
        tool_func = server._tools["test_tool"]["function"]
        result = await tool_func()
        assert result == {"result": "success"}
