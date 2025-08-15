---
title: Model Context Protocol (MCP)
category: advanced
source_lines: 71881-71992
line_count: 111
---

# Model Context Protocol (MCP)
Source: https://docs.agno.com/tools/mcp/mcp

Learn how to use MCP with Agno to enable your agents to interact with external systems through a standardized interface.

The [Model Context Protocol (MCP)](https://modelcontextprotocol.io) enables Agents to interact with external systems through a standardized interface.
You can connect your Agents to any MCP server, using Agno's MCP integration.

## Usage

<Steps>
  <Step title="Find the MCP server you want to use">
    You can use any working MCP server. To see some examples, you can check [this GitHub repository](https://github.com/modelcontextprotocol/servers), by the maintainers of the MCP themselves.
  </Step>

  <Step title="Initialize the MCP integration">
    Intialize the `MCPTools` class and connect to the MCP server. This needs to be done inside an async function.

    The recommended way to define the MCP server, is to use the `command` or `url` parameters. With `command`, you can pass the command used to run the MCP server you want. With `url`, you can pass the URL of the running MCP server you want to use.

    For example, to use the "[mcp-server-git](https://github.com/modelcontextprotocol/servers/tree/main/src/git)" server, you can do the following:

    ```python
    from agno.tools.mcp import MCPTools

    async def run_mcp_agent():

        # Initialize the MCP tools
        mcp_tools = MCPTools(command=f"uvx mcp-server-git")

        # Connect to the MCP server
        await mcp_tools.connect()
        ...
    ```
  </Step>

  <Step title="Provide the MCPTools to the Agent">
    When initializing the Agent, pass the `MCPTools` class in the `tools` parameter.

    The agent will now be ready to use the MCP server:

    ```python
    from agno.agent import Agent
    from agno.models.openai import OpenAIChat
    from agno.tools.mcp import MCPTools

    async def run_mcp_agent():

        # Initialize the MCP tools
        mcp_tools = MCPTools(command=f"uvx mcp-server-git")

        # Connect to the MCP server
        await mcp_tools.connect()

        # Setup and run the agent
        agent = Agent(model=OpenAIChat(id="gpt-4o"), tools=[mcp_tools])
        await agent.aprint_response("What is the license for this project?", stream=True)
    ```
  </Step>
</Steps>

### Basic example: Filesystem Agent

Here's a filesystem agent that uses the [Filesystem MCP server](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) to explore and analyze files:

```python filesystem_agent.py
import asyncio
from pathlib import Path
from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.mcp import MCPTools
from mcp import StdioServerParameters


async def run_mcp_agent(message: str) -> None:
    """Run the filesystem agent with the given message."""

    file_path = str(Path(__file__).parent.parent.parent.parent)

    # Initialize the MCP tools
    mcp_tools = MCPTools(f"npx -y @modelcontextprotocol/server-filesystem {file_path}")

    # Connect to the MCP server
    await mcp_tools.connect()

    # Use the MCP tools with an Agent
    agent = Agent(
        model=OpenAIChat(id="gpt-4o"),
        tools=[mcp_tools],
        instructions=dedent("""\
            You are a filesystem assistant. Help users explore files and directories.

            - Navigate the filesystem to answer questions
            - Use the list_allowed_directories tool to find directories that you can access
            - Provide clear context about files you examine
            - Use headings to organize your responses
            - Be concise and focus on relevant information\
        """),
        markdown=True,
        show_tool_calls=True,
    )

    # Run the agent
    await agent.aprint_response(message, stream=True)

    # Close the MCP connection
    await mcp_tools.close()


