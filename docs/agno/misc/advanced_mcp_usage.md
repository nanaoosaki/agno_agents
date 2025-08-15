---
title: Advanced MCP Usage
category: misc
source_lines: 71720-71767
line_count: 47
---

# Advanced MCP Usage
Source: https://docs.agno.com/tools/mcp/advanced_usage



Agno's MCP integration also supports handling connections to multiple servers, specifying server parameters and using your own MCP servers:

## Connecting to Multiple MCP Servers

You can use multiple MCP servers in a single agent by using the `MultiMCPTools` class.

```python multiple_mcp_servers.py
import asyncio
from os import getenv

from agno.agent import Agent
from agno.tools.mcp import MultiMCPTools


async def run_agent(message: str) -> None:
    # Initialize the MCP tools
    mcp_tools = MultiMCPTools(
        [
            "npx -y @openbnb/mcp-server-airbnb --ignore-robots-txt",
            "npx -y @modelcontextprotocol/server-brave-search",
        ],
        env={
            "BRAVE_API_KEY": getenv("BRAVE_API_KEY"),
        },
        timeout_seconds=30,
    )

    # Connect to the MCP servers
    await mcp_tools.connect()

    # Use the MCP tools with an Agent
    agent = Agent(
        tools=[mcp_tools],
        markdown=True,
        show_tool_calls=True,
    )
    await agent.aprint_response(message)

    # Close the MCP connection
    await mcp_tools.close()


