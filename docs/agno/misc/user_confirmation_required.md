---
title: User Confirmation Required
category: misc
source_lines: 31410-31524
line_count: 114
---

# User Confirmation Required
Source: https://docs.agno.com/examples/concepts/user-control-flows/01-confirmation-required

This example demonstrates how to implement human-in-the-loop functionality by requiring user confirmation before executing tool calls.

## Code

```python cookbook/agent_concepts/user_control_flows/confirmation_required.py
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
def get_top_hackernews_stories(num_stories: int) -> str:
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

agent.run("Fetch the top 2 hackernews stories.")
if agent.is_paused:
    for tool in agent.run_response.tools_requiring_confirmation:
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

run_response = agent.continue_run()
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
      python cookbook/agent_concepts/user_control_flows/confirmation_required.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/user_control_flows/confirmation_required.py
      ```
    </CodeGroup>
  </Step>
</Steps>

## Key Features

* Uses `@tool(requires_confirmation=True)` to mark tools that need user confirmation
* Demonstrates how to continue agent execution after user input

## Use Cases

* Confirming sensitive operations before execution


