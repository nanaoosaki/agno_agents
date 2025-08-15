---
title: Streaming User Confirmation
category: advanced
source_lines: 31644-31768
line_count: 124
---

# Streaming User Confirmation
Source: https://docs.agno.com/examples/concepts/user-control-flows/03-confirmation-required-stream

This example demonstrates how to implement streaming user confirmation flows, allowing for real-time interaction and response streaming.

## Code

```python cookbook/agent_concepts/user_control_flows/confirmation_required_stream.py
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

for run_response in agent.run("Fetch the top 2 hackernews stories", stream=True):
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
                # We update the tools in place
                tool.confirmed = True
        run_response = agent.continue_run(
            run_id=agent.run_response.run_id,
            updated_tools=agent.run_response.tools,
            stream=True,
        )
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
      python cookbook/agent_concepts/user_control_flows/confirmation_required_stream.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/user_control_flows/confirmation_required_stream.py
      ```
    </CodeGroup>
  </Step>
</Steps>

## Key Features

* Uses `agent.run(stream=True)` for streaming responses
* Implements streaming continuation with `agent.continue_run(stream=True)`
* Maintains real-time interaction with user confirmation
* Demonstrates how to handle streaming responses with user input

## Use Cases

* Real-time user interaction
* Streaming applications requiring user input
* Interactive chat interfaces
* Progressive response generation


