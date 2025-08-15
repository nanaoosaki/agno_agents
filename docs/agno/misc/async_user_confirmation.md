---
title: Async User Confirmation
category: misc
source_lines: 31524-31644
line_count: 120
---

# Async User Confirmation
Source: https://docs.agno.com/examples/concepts/user-control-flows/02-confirmation-required-async

This example demonstrates how to implement asynchronous user confirmation flows, allowing for non-blocking execution while waiting for user input.

## Code

```python cookbook/agent_concepts/user_control_flows/confirmation_required_async.py
import asyncio
import json

import httpx
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools import tool
from agno.utils import pprint
from rich.console import Console
from rich.prompt import Prompt

console = Console()

@tool(requires_confirmation=True)
async def get_top_hackernews_stories(num_stories: int) -> str:
    """Fetch top stories from Hacker News.

    Args:
        num_stories (int): Number of stories to retrieve

    Returns:
        str: JSON string containing story details
    """
    # Fetch top story IDs
    response = httpx.get("https://hacker-news.firebaseio.com/v0/topstories.json")
    story_ids = response.json()

    # Yield story details
    all_stories = []
    for story_id in story_ids[:num_stories]:
        story_response = httpx.get(
            f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
        )
        story = story_response.json()
        if "text" in story:
            story.pop("text", None)
        all_stories.append(story)
    return json.dumps(all_stories)

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[get_top_hackernews_stories],
    markdown=True,
)

run_response = asyncio.run(agent.arun("Fetch the top 2 hackernews stories"))
if run_response.is_paused:
    for tool in run_response.tools_requiring_confirmation:
        # Ask for confirmation
        console.print(
            f"Tool name [bold blue]{tool.tool_name}({tool.tool_args})[/] requires confirmation."
        )
        message = (
            Prompt.ask("Do you want to continue?", choices=["y", "n"], default="y")
            .strip()
            .lower()
        )

        if message == "n":
            tool.confirmed = False
        else:
            tool.confirmed = True

run_response = asyncio.run(agent.acontinue_run(run_response=run_response))
pprint.pprint_run_response(run_response)
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export OPENAI_API_KEY=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U agno httpx rich openai
    ```
  </Step>

  <Step title="Run Example">
    <CodeGroup>
      ```bash Mac
      python cookbook/agent_concepts/user_control_flows/confirmation_required_async.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/user_control_flows/confirmation_required_async.py
      ```
    </CodeGroup>
  </Step>
</Steps>

## Key Features

* Uses `agent.arun()` for asynchronous agent execution
* Implements `agent.acontinue_run()` for async continuation
* Maintains the same confirmation flow as synchronous version
* Demonstrates how to handle async execution with user input

## Use Cases

* Non-blocking user confirmation flows
* High-performance applications requiring async execution
* Web applications with user interaction
* Long-running operations with user input


