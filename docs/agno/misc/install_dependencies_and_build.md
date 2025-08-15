---
title: Install dependencies and build
category: misc
source_lines: 27409-27505
line_count: 96
---

# Install dependencies and build
npm install
npm run build
```

### 2. Install Python Dependencies

```bash
pip install agno mcp openai
```

### 3. Set Environment Variables

```bash
export BROWSERBASE_API_KEY=your_browserbase_api_key
export BROWSERBASE_PROJECT_ID=your_browserbase_project_id
export OPENAI_API_KEY=your_openai_api_key
```

## Code Example

```python
import asyncio
from os import environ
from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.mcp import MCPTools
from mcp import StdioServerParameters


async def run_agent(message: str) -> None:
    server_params = StdioServerParameters(
        command="node",
        # Update this path to the location where you cloned the repository
        args=["mcp-server-browserbase/stagehand/dist/index.js"],
        env=environ.copy(),
    )

    async with MCPTools(server_params=server_params, timeout_seconds=60) as mcp_tools:
        agent = Agent(
            model=OpenAIChat(id="gpt-4o"),
            tools=[mcp_tools],
            instructions=dedent("""\
                You are a web scraping assistant that creates concise reader's digests from Hacker News.

                CRITICAL INITIALIZATION RULES - FOLLOW EXACTLY:
                1. NEVER use screenshot tool until AFTER successful navigation
                2. ALWAYS start with stagehand_navigate first
                3. Wait for navigation success message before any other actions
                4. If you see initialization errors, restart with navigation only
                5. Use stagehand_observe and stagehand_extract to explore pages safely

                Available tools and safe usage order:
                - stagehand_navigate: Use FIRST to initialize browser
                - stagehand_extract: Use to extract structured data from pages
                - stagehand_observe: Use to find elements and understand page structure
                - stagehand_act: Use to click links and navigate to comments
                - screenshot: Use ONLY after navigation succeeds and page loads

                Your goal is to create a comprehensive but concise digest that includes:
                - Top headlines with brief summaries
                - Key themes and trends
                - Notable comments and insights
                - Overall tech news landscape overview

                Be methodical, extract structured data, and provide valuable insights.
            """),
            markdown=True,
            show_tool_calls=True,
        )
        await agent.aprint_response(message, stream=True)


if __name__ == "__main__":
    asyncio.run(
        run_agent(
            "Create a comprehensive Hacker News Reader's Digest from https://news.ycombinator.com"
        )
    )
```

## Available Tools

The Stagehand MCP server provides several tools for web automation:

| Tool                 | Purpose                                     | Usage Notes                            |
| -------------------- | ------------------------------------------- | -------------------------------------- |
| `stagehand_navigate` | Navigate to web pages                       | **Use first** for initialization       |
| `stagehand_extract`  | Extract structured data                     | Safe for content extraction            |
| `stagehand_observe`  | Find elements and understand page structure | Good for exploration                   |
| `stagehand_act`      | Interact with page elements                 | Click, type, scroll actions            |
| `screenshot`         | Take screenshots                            | **Use only after** navigation succeeds |


