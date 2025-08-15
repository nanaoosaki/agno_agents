---
title: GitHub MCP agent
category: misc
source_lines: 26963-27028
line_count: 65
---

# GitHub MCP agent
Source: https://docs.agno.com/examples/concepts/tools/mcp/github



Using the [GitHub MCP server](https://github.com/modelcontextprotocol/servers/tree/main/src/github) to create an Agent that can explore, analyze and provide insights about GitHub repositories:

```python
"""🐙 MCP GitHub Agent - Your Personal GitHub Explorer!

This example shows how to create a GitHub agent that uses MCP to explore,
analyze, and provide insights about GitHub repositories. The agent leverages the Model
Context Protocol (MCP) to interact with GitHub, allowing it to answer questions
about issues, pull requests, repository details and more.

Example prompts to try:
- "List open issues in the repository"
- "Show me recent pull requests"
- "What are the repository statistics?"
- "Find issues labeled as bugs"
- "Show me contributor activity"

Run: `pip install agno mcp openai` to install the dependencies
Environment variables needed:
- Create a GitHub personal access token following these steps:
    - https://github.com/modelcontextprotocol/servers/tree/main/src/github#setup
- export GITHUB_TOKEN: Your GitHub personal access token
"""

import asyncio
import os
from textwrap import dedent

from agno.agent import Agent
from agno.tools.mcp import MCPTools
from mcp import StdioServerParameters


async def run_agent(message: str) -> None:
    """Run the GitHub agent with the given message."""

    # Initialize the MCP server
    server_params = StdioServerParameters(
        command="npx",
        args=["-y", "@modelcontextprotocol/server-github"],
    )

    # Create a client session to connect to the MCP server
    async with MCPTools(server_params=server_params) as mcp_tools:
        agent = Agent(
            tools=[mcp_tools],
            instructions=dedent("""\
                You are a GitHub assistant. Help users explore repositories and their activity.

                - Use headings to organize your responses
                - Be concise and focus on relevant information\
            """),
            markdown=True,
            show_tool_calls=True,
        )

        # Run the agent
        await agent.aprint_response(message, stream=True)


