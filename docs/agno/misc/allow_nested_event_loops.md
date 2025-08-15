---
title: Allow nested event loops
category: misc
source_lines: 9069-9125
line_count: 56
---

# Allow nested event loops
nest_asyncio.apply()

agent_storage_file: str = "tmp/agents.db"


async def run_server() -> None:
    """Run the GitHub agent server."""
    github_token = getenv("GITHUB_TOKEN") or getenv("GITHUB_ACCESS_TOKEN")
    if not github_token:
        raise ValueError("GITHUB_TOKEN environment variable is required")

    # Initialize the MCP server
    server_params = StdioServerParameters(
        command="npx",
        args=["-y", "@modelcontextprotocol/server-github"],
    )

    # Create a client session to connect to the MCP server
    async with MCPTools(server_params=server_params) as mcp_tools:
        agent = Agent(
            name="MCP GitHub Agent",
            tools=[mcp_tools],
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

        playground = Playground(
            agents=[agent],
            name="MCP Demo",
            description="A playground for MCP",
            app_id="mcp-demo",
        )
        playground.get_app()

        # Serve the app while keeping the MCPTools context manager alive
        playground.serve(app="mcp_demo:app", reload=True)


if __name__ == "__main__":
    asyncio.run(run_server())

