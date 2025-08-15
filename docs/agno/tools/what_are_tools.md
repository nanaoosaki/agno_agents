---
title: What are Tools?
category: tools
source_lines: 71648-71720
line_count: 72
---

# What are Tools?
Source: https://docs.agno.com/tools/introduction

Tools are functions that helps Agno Agents to interact with the external world.

Tools make agents - "agentic" by enabling them to interact with external systems like searching the web, running SQL, sending an email or calling APIs.

Agno comes with 80+ pre-built toolkits, but in most cases, you will write your own tools. The general syntax is:

```python
import random

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools import tool


@tool(show_result=True, stop_after_tool_call=True)
def get_weather(city: str) -> str:
    """Get the weather for a city."""
    # In a real implementation, this would call a weather API
    weather_conditions = ["sunny", "cloudy", "rainy", "snowy", "windy"]
    random_weather = random.choice(weather_conditions)

    return f"The weather in {city} is {random_weather}."


agent = Agent(
    model=OpenAIChat(model="gpt-4o-mini"),
    tools=[get_weather],
    markdown=True,
)
agent.print_response("What is the weather in San Francisco?", stream=True)
```

<Tip>
  In the example above, the `get_weather` function is a tool. When it is called, the tool result will be shown in the output because we set `show_result=True`.

  Then, the Agent will stop after the tool call because we set `stop_after_tool_call=True`.
</Tip>

### Using the Toolkit Class

The `Toolkit` class provides a way to manage multiple tools with additional control over their execution. You can specify which tools should stop the agent after execution and which should have their results shown.

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.googlesearch import GoogleSearchTools

agent = Agent(
    model=OpenAIChat(id="gpt-4.5-preview"),
    tools=[
        GoogleSearchTools(
            stop_after_tool_call_tools=["google_search"],
            show_result_tools=["google_search"],
        )
    ],
    show_tool_calls=True,
)

agent.print_response("What's the latest about gpt 4.5?", markdown=True)
```

In this example, the `GoogleSearchTools` toolkit is configured to stop the agent after executing the `google_search` function and to show the result of this function.

Read more about:

* [Available Toolkits](/tools/toolkits)
* [Using functions as tools](/tools/tool-decorator)


