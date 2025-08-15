---
title: Writing your own tools
category: tools
source_lines: 72910-73046
line_count: 136
---

# Writing your own tools
Source: https://docs.agno.com/tools/tool-decorator

Learn how to write your own tools and how to use the `@tool` decorator to modify the behavior of a tool.

In most production cases, you will need to write your own tools. Which is why we're focused on provide the best tool-use experience in Agno.

The rule is simple:

* Any python function can be used as a tool by an Agent.
* Use the `@tool` decorator to modify what happens before and after this tool is called.

## Any python function can be used as a tool

For example, here's how to use a `get_top_hackernews_stories` function as a tool:

```python hn_agent.py
import json
import httpx

from agno.agent import Agent

def get_top_hackernews_stories(num_stories: int = 10) -> str:
    """
    Use this function to get top stories from Hacker News.

    Args:
        num_stories (int): Number of stories to return. Defaults to 10.

    Returns:
        str: JSON string of top stories.
    """

    # Fetch top story IDs
    response = httpx.get('https://hacker-news.firebaseio.com/v0/topstories.json')
    story_ids = response.json()

    # Fetch story details
    stories = []
    for story_id in story_ids[:num_stories]:
        story_response = httpx.get(f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json')
        story = story_response.json()
        if "text" in story:
            story.pop("text", None)
        stories.append(story)
    return json.dumps(stories)

agent = Agent(tools=[get_top_hackernews_stories], show_tool_calls=True, markdown=True)
agent.print_response("Summarize the top 5 stories on hackernews?", stream=True)
```

## Magic of the @tool decorator

To modify the behavior of a tool, use the `@tool` decorator. Some notable features:

* `requires_confirmation=True`: Requires user confirmation before execution.
* `requires_user_input=True`: Requires user input before execution. Use `user_input_fields` to specify which fields require user input.
* `external_execution=True`: The tool will be executed outside of the agent's control.
* `show_result=True`: Show the output of the tool call in the Agent's response. Without this flag, the result of the tool call is sent to the model for further processing.
* `stop_after_tool_call=True`: Stop the agent run after the tool call.
* `tool_hooks`: Run custom logic before and after this tool call.
* `cache_results=True`: Cache the tool result to avoid repeating the same call. Use `cache_dir` and `cache_ttl` to configure the cache.

Here's an example that uses many possible parameters on the `@tool` decorator.

```python advanced_tool.py
import httpx
from agno.agent import Agent
from agno.tools import tool
from typing import Any, Callable, Dict

def logger_hook(function_name: str, function_call: Callable, arguments: Dict[str, Any]):
    """Hook function that wraps the tool execution"""
    print(f"About to call {function_name} with arguments: {arguments}")
    result = function_call(**arguments)
    print(f"Function call completed with result: {result}")
    return result

@tool(
    name="fetch_hackernews_stories",                # Custom name for the tool (otherwise the function name is used)
    description="Get top stories from Hacker News",  # Custom description (otherwise the function docstring is used)
    show_result=True,                               # Show result after function call
    stop_after_tool_call=True,                      # Return the result immediately after the tool call and stop the agent
    tool_hooks=[logger_hook],                       # Hook to run before and after execution
    requires_confirmation=True,                     # Requires user confirmation before execution
    cache_results=True,                             # Enable caching of results
    cache_dir="/tmp/agno_cache",                    # Custom cache directory
    cache_ttl=3600                                  # Cache TTL in seconds (1 hour)
)
def get_top_hackernews_stories(num_stories: int = 5) -> str:
    """
    Fetch the top stories from Hacker News.

    Args:
        num_stories: Number of stories to fetch (default: 5)

    Returns:
        str: The top stories in text format
    """
    # Fetch top story IDs
    response = httpx.get("https://hacker-news.firebaseio.com/v0/topstories.json")
    story_ids = response.json()

    # Get story details
    stories = []
    for story_id in story_ids[:num_stories]:
        story_response = httpx.get(f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json")
        story = story_response.json()
        stories.append(f"{story.get('title')} - {story.get('url', 'No URL')}")

    return "\n".join(stories)

agent = Agent(tools=[get_top_hackernews_stories])
agent.print_response("Show me the top news from Hacker News")
```

### @tool Parameters Reference

| Parameter               | Type             | Description                                                       |
| ----------------------- | ---------------- | ----------------------------------------------------------------- |
| `name`                  | `str`            | Override for the function name                                    |
| `description`           | `str`            | Override for the function description                             |
| `show_result`           | `bool`           | If True, shows the result after function call                     |
| `stop_after_tool_call`  | `bool`           | If True, the agent will stop after the function call              |
| `tool_hooks`            | `list[Callable]` | List of hooks that wrap the function execution                    |
| `pre_hook`              | `Callable`       | Hook to run before the function is executed                       |
| `post_hook`             | `Callable`       | Hook to run after the function is executed                        |
| `requires_confirmation` | `bool`           | If True, requires user confirmation before execution              |
| `requires_user_input`   | `bool`           | If True, requires user input before execution                     |
| `user_input_fields`     | `list[str]`      | List of fields that require user input                            |
| `external_execution`    | `bool`           | If True, the tool will be executed outside of the agent's control |
| `cache_results`         | `bool`           | If True, enable caching of function results                       |
| `cache_dir`             | `str`            | Directory to store cache files                                    |
| `cache_ttl`             | `int`            | Time-to-live for cached results in seconds (default: 3600)        |


