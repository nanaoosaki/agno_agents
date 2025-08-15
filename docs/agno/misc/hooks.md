---
title: Hooks
category: misc
source_lines: 71461-71648
line_count: 187
---

# Hooks
Source: https://docs.agno.com/tools/hooks

Learn how to use tool hooks to modify the behavior of a tool.

## Tool Hooks

You can use tool hooks to perform validation, logging, or any other logic before or after a tool is called.

A tool hook is a function that takes a function name, function call, and arguments. Optionally, you can access the `Agent` or `Team` object as well.  Inside the tool hook, you have to call the function call and return the result.

<Note>
  It is important to use exact parameter names when defining a tool hook. `agent`, `team`, `function_name`, `function_call`, and `arguments` are available parameters.
</Note>

For example:

```python
def logger_hook(
    function_name: str, function_call: Callable, arguments: Dict[str, Any]
):
    """Log the duration of the function call"""
    start_time = time.time()

    # Call the function
    result = function_call(**arguments)
    
    end_time = time.time()
    duration = end_time - start_time
    
    logger.info(f"Function {function_name} took {duration:.2f} seconds to execute")

    # Return the result
    return result
```

or

```python
def confirmation_hook(
    function_name: str, function_call: Callable, arguments: Dict[str, Any]
):
    """Confirm the function call"""
    if function_name != "get_top_hackernews_stories":
        raise ValueError("This tool is not allowed to be called")
    return function_call(**arguments)
```

You can assign tool hooks on agents and teams.  The tool hooks will be applied to all tool calls made by the agent or team.

For example:

```python
agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[DuckDuckGoTools()],
    tool_hooks=[logger_hook],
)
```

You can also get access to the `Agent` or `Team` object in the tool hook.

```python

def grab_customer_profile_hook(
    agent: Agent, function_name: str, function_call: Callable, arguments: Dict[str, Any]
):
    cust_id = arguments.get("customer")
    if cust_id not in agent.session_state["customer_profiles"]:
        raise ValueError(f"Customer profile for {cust_id} not found")
    customer_profile = agent.session_state["customer_profiles"][cust_id]

    # Replace the customer with the customer_profile for the function call
    arguments["customer"] = json.dumps(customer_profile)
    # Call the function with the updated arguments
    result = function_call(**arguments)

    return result
```

### Multiple Tool Hooks

You can also assign multiple tool hooks at once. They will be applied in the order they are assigned.

```python
agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[DuckDuckGoTools()],
    tool_hooks=[logger_hook, confirmation_hook],  # The logger_hook will run on the outer layer, and the confirmation_hook will run on the inner layer
)
```

You can also assign tool hooks to specific custom tools.

```python
@tool(tool_hooks=[logger_hook, confirmation_hook])
def get_top_hackernews_stories(num_stories: int) -> Iterator[str]:
    """Fetch top stories from Hacker News.

    Args:
        num_stories (int): Number of stories to retrieve
    """
    # Fetch top story IDs
    response = httpx.get("https://hacker-news.firebaseio.com/v0/topstories.json")
    story_ids = response.json()

    # Yield story details
    final_stories = []
    for story_id in story_ids[:num_stories]:
        story_response = httpx.get(
            f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
        )
        story = story_response.json()
        if "text" in story:
            story.pop("text", None)
        final_stories.append(story)

    return json.dumps(final_stories)

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[get_top_hackernews_stories],
)
```

## Pre and Post Hooks

Pre and post hooks let's you modify what happens before and after a tool is called. It is an alternative to tool hooks.

Set the `pre_hook` in the `@tool` decorator to run a function before the tool call.

Set the `post_hook` in the `@tool` decorator to run a function after the tool call.

Here's a demo example of using a `pre_hook`, `post_hook` along with Agent Context.

```python pre_and_post_hooks.py
import json
from typing import Iterator

import httpx
from agno.agent import Agent
from agno.tools import FunctionCall, tool


def pre_hook(fc: FunctionCall):
    print(f"Pre-hook: {fc.function.name}")
    print(f"Arguments: {fc.arguments}")
    print(f"Result: {fc.result}")


def post_hook(fc: FunctionCall):
    print(f"Post-hook: {fc.function.name}")
    print(f"Arguments: {fc.arguments}")
    print(f"Result: {fc.result}")


@tool(pre_hook=pre_hook, post_hook=post_hook)
def get_top_hackernews_stories(agent: Agent) -> Iterator[str]:
    num_stories = agent.context.get("num_stories", 5) if agent.context else 5

    # Fetch top story IDs
    response = httpx.get("https://hacker-news.firebaseio.com/v0/topstories.json")
    story_ids = response.json()

    # Yield story details
    for story_id in story_ids[:num_stories]:
        story_response = httpx.get(
            f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
        )
        story = story_response.json()
        if "text" in story:
            story.pop("text", None)
        yield json.dumps(story)


agent = Agent(
    context={
        "num_stories": 2,
    },
    tools=[get_top_hackernews_stories],
    markdown=True,
    show_tool_calls=True,
)
agent.print_response("What are the top hackernews stories?", stream=True)
```


