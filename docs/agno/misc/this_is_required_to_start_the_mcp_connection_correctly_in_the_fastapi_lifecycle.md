---
title: This is required to start the MCP connection correctly in the FastAPI lifecycle
category: misc
source_lines: 72029-72068
line_count: 39
---

# This is required to start the MCP connection correctly in the FastAPI lifecycle
@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage MCP connection lifecycle inside a FastAPI app"""
    global mcp_tools

    # Startuplogic: connect to our MCP server
    mcp_tools = MCPTools(server_params=server_params)
    await mcp_tools.connect()

    # Add the MCP tools to our Agent
    agent.tools = [mcp_tools]

    yield

    # Shutdown: Close MCP connection
    await mcp_tools.close()


agent = Agent(
    name="MCP GitHub Agent",
    instructions=dedent("""\
        You are a GitHub assistant. Help users explore repositories and their activity.

        - Use headings to organize your responses
        - Be concise and focus on relevant information\
    """),
    model=OpenAIChat(id="gpt-4o"),
    storage=SqliteAgentStorage(
        table_name="basic_agent",
        db_file=agent_storage_file,
        auto_upgrade_schema=True,
    ),
    add_history_to_messages=True,
    num_history_responses=3,
    add_datetime_to_instructions=True,
    markdown=True,
)

