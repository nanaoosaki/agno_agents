---
title: SSE Transport
category: misc
source_lines: 72115-72260
line_count: 145
---

# SSE Transport
Source: https://docs.agno.com/tools/mcp/transports/sse



Agno's MCP integration supports the [SSE transport](https://modelcontextprotocol.io/docs/concepts/transports#server-sent-events-sse). This transport enables server-to-client streaming, and can prove more useful than [stdio](https://modelcontextprotocol.io/docs/concepts/transports#standard-input%2Foutput-stdio) when working with restricted networks.

To use it, initialize the `MCPTools` passing the URL of the MCP server and setting the transport to `sse`:

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.mcp import MCPTools

server_url = "http://localhost:8000/sse"

async with MCPTools(url=server_url, transport="sse") as mcp_tools:
    agent = Agent(model=OpenAIChat(id="gpt-4o"), tools=[mcp_tools])
    await agent.aprint_response("What is the license for this project?", stream=True)
```

You can also use the `server_params` argument to define the MCP connection. This way you can specify the headers to send to the MCP server with every request, and the timeout values:

```python
from agno.tools.mcp import MCPTools, SSEClientParams

server_params = SSEClientParams(
    url=...,
    headers=...,
    timeout=...,
    sse_read_timeout=...,
)

async def run_mcp_agent():

    # Initialize the MCP tools with the server parameters
    mcp_tools = MCPTools(server_params=server_params)

    ...
```

## Complete example

Let's set up a simple local server and connect to it using the SSE transport:

<Steps>
  <Step title="Setup the server">
    ```python sse_server.py
    from mcp.server.fastmcp import FastMCP

    mcp = FastMCP("calendar_assistant")


    @mcp.tool()
    def get_events(day: str) -> str:
        return f"There are no events scheduled for {day}."


    @mcp.tool()
    def get_birthdays_this_week() -> str:
        return "It is your mom's birthday tomorrow"


    if __name__ == "__main__":
        mcp.run(transport="sse")
    ```
  </Step>

  <Step title="Setup the client">
    ```python sse_client.py
    import asyncio

    from agno.agent import Agent
    from agno.models.openai import OpenAIChat
    from agno.tools.mcp import MCPTools, MultiMCPTools

    # This is the URL of the MCP server we want to use.
    server_url = "http://localhost:8000/sse"


    async def run_agent(message: str) -> None:
        mcp_tools = MCPTools(transport="sse", url=server_url)
        await mcp_tools.connect()

        agent = Agent(
            model=OpenAIChat(id="gpt-4o"),
            tools=[mcp_tools],
            markdown=True,
        )
        await agent.aprint_response(message=message, stream=True, markdown=True)

        await mcp_tools.close()


    # Using MultiMCPTools, we can connect to multiple MCP servers at once, even if they use different transports.
    # In this example we connect to both our example server (SSE transport), and a different server (stdio transport).
    async def run_agent_with_multimcp(message: str) -> None:

        # Initialize the MultiMCPTools instance
        multi_mcp_tools =MultiMCPTools(
            commands=["npx -y @openbnb/mcp-server-airbnb --ignore-robots-txt"],
            urls=[server_url],
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

        # Close the MCP connections
        await multi_mcp_tools.close()


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
    python sse_server.py
    ```
  </Step>

  <Step title="Run the client">
    ```bash
    python sse_client.py
    ```
  </Step>
</Steps>


