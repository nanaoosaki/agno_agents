---
title: Streamable HTTP Transport
category: misc
source_lines: 72354-72526
line_count: 172
---

# Streamable HTTP Transport
Source: https://docs.agno.com/tools/mcp/transports/streamable_http



The new [Streamable HTTP transport](https://modelcontextprotocol.io/specification/draft/basic/transports#streamable-http) replaces the HTTP+SSE transport from protocol version 2024-11-05.

This transport enables the MCP server to handle multiple client connections, and can also use SSE for server-to-client streaming.

To use it, initialize the `MCPTools` passing the URL of the MCP server and setting the transport to `streamable-http`:

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.mcp import MCPTools

server_url = "http://localhost:8000/mcp"

async def run_mcp_agent():

    # Initialize the MCP tools
    mcp_tools = MCPTools(url=server_url, transport="streamable-http")

    # Connect to the MCP server
    await mcp_tools.connect()

    # Initialize the Agent
    agent = Agent(model=OpenAIChat(id="gpt-4o"), tools=[mcp_tools])

    # Run the agent
    await agent.aprint_response("What is the license for this project?", stream=True)

    # Close the MCP connection
    await mcp_tools.close()
```

You can also use the `server_params` argument to define the MCP connection. This way you can specify the headers to send to the MCP server with every request, and the timeout values:

```python
from agno.tools.mcp import MCPTools, StreamableHTTPClientParams

server_params = StreamableHTTPClientParams(
    url=...,
    headers=...,
    timeout=...,
    sse_read_timeout=...,
    terminate_on_close=...,

)

async def run_mcp_agent():

    # Initialize the MCP tools
    mcp_tools = MCPTools(server_params=server_params)

    # Connect to the MCP server
    await mcp_tools.connect()

    ...

```

## Complete example

Let's set up a simple local server and connect to it using the Streamable HTTP transport:

<Steps>
  <Step title="Setup the server">
    ```python streamable_http_server.py
    from mcp.server.fastmcp import FastMCP

    mcp = FastMCP("calendar_assistant")


    @mcp.tool()
    def get_events(day: str) -> str:
        return f"There are no events scheduled for {day}."


    @mcp.tool()
    def get_birthdays_this_week() -> str:
        return "It is your mom's birthday tomorrow"


    if __name__ == "__main__":
        mcp.run(transport="streamable-http")
    ```
  </Step>

  <Step title="Setup the client">
    ```python streamable_http_client.py
    import asyncio

    from agno.agent import Agent
    from agno.models.openai import OpenAIChat
    from agno.tools.mcp import MCPTools, MultiMCPTools

    # This is the URL of the MCP server we want to use.
    server_url = "http://localhost:8000/mcp"


    async def run_agent(message: str) -> None:

        # Initialize the MCP tools
        mcp_tools = MCPTools(transport="streamable-http", url=server_url)

        # Connect to the MCP server
        await mcp_tools.connect()

        # Initialize the Agent
        agent = Agent(
            model=OpenAIChat(id="gpt-4o"),
            tools=[mcp_tools],
            markdown=True,
        )

        # Run the agent
        await agent.aprint_response(message=message, stream=True, markdown=True)

        # Close the MCP connection
        await mcp_tools.close()


    # Using MultiMCPTools, we can connect to multiple MCP servers at once, even if they use different transports.
    # In this example we connect to both our example server (Streamable HTTP transport), and a different server (stdio transport).
    async def run_agent_with_multimcp(message: str) -> None:

        # Initialize the MultiMCPTools instance
        multi_mcp_tools = MultiMCPTools(
            commands=["npx -y @openbnb/mcp-server-airbnb --ignore-robots-txt"],
            urls=[server_url],
            urls_transports=["streamable-http"],
        )

        # Connect to the MCP servers
        await multi_mcp_tools.connect()

        # Initialize the Agent
        agent = Agent(
            model=OpenAIChat(id="gpt-4o"),
            tools=[mcp_tools],
            markdown=True,
        )

        # Run the agent
        await agent.aprint_response(message=message, stream=True, markdown=True)


    if __name__ == "__main__":
        asyncio.run(run_agent("Do I have any birthdays this week?"))
        asyncio.run(
            run_agent_with_multimcp(
                "Can you check when is my mom's birthday, and if there are any AirBnb listings in SF for two people for that day?"
            )
        )
    ```
  </Step>

  <Step title="Run the server">
    ```bash
    python streamable_http_server.py
    ```
  </Step>

  <Step title="Run the client">
    ```bash
    python streamable_http_client.py
    ```
  </Step>
</Steps>


