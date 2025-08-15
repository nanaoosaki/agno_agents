---
title: Stdio Transport
category: misc
source_lines: 72260-72343
line_count: 83
---

# Stdio Transport
Source: https://docs.agno.com/tools/mcp/transports/stdio



Transports in the Model Context Protocol (MCP) define how messages are sent and received. The Agno integration supports the three existing types:
[stdio](https://modelcontextprotocol.io/docs/concepts/transports#standard-input%2Foutput-stdio),
[SSE](https://modelcontextprotocol.io/docs/concepts/transports#server-sent-events-sse) and
[Streamable HTTP](https://modelcontextprotocol.io/specification/draft/basic/transports#streamable-http).

The stdio (standard input/output) transport is the default one in Agno's integration. It works best for local integrations.

To use it, simply initialize the `MCPTools` class with its `command` argument.
The command you want to pass is the one used to run the MCP server the agent will have access to.

For example `uvx mcp-server-git`, which runs a [git MCP server](https://github.com/modelcontextprotocol/servers/tree/main/src/git):

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.mcp import MCPTools

async def run_mcp_agent():
    # Initialize the MCP tools
    mcp_tools = MCPTools(command=f"uvx mcp-server-git")

    # Connect to the MCP server
    await mcp_tools.connect()

    # Initialize the Agent
    agent = Agent(model=OpenAIChat(id="gpt-4o"), tools=[mcp_tools])

    # Run the agent
    await agent.aprint_response("What is the license for this project?", stream=True)

    # Close the MCP connection
    await mcp_tools.close()
```

You can also use multiple MCP servers at once, with the `MultiMCPTools` class. For example:

```python
import asyncio
import os

from agno.agent import Agent
from agno.tools.mcp import MultiMCPTools


async def run_agent(message: str) -> None:
    """Run the Airbnb and Google Maps agent with the given message."""

    env = {
        **os.environ,
        "GOOGLE_MAPS_API_KEY": os.getenv("GOOGLE_MAPS_API_KEY"),
    }

    # Initialize the MultiMCPTools instance
    multi_mcp_tools = MultiMCPTools(
        [
            "npx -y @openbnb/mcp-server-airbnb --ignore-robots-txt",
            "npx -y @modelcontextprotocol/server-google-maps",
        ],
        env=env,
    )

    # Connect to the MCP servers
    await multi_mcp_tools.connect()

    # Initialize the Agent
    agent = Agent(
        tools=[mcp_tools],
        markdown=True,
        show_tool_calls=True,
    )

    # Run the agent
    await agent.aprint_response(message, stream=True)

    # Close the MCP connections
    await multi_mcp_tools.close()


