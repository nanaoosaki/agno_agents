---
title: Updating Tools
category: tools
source_lines: 71083-71125
line_count: 42
---

# Updating Tools
Source: https://docs.agno.com/tools/attaching-tools

Learn how to add/update tools on Agents and Teams after they have been created.

Tools can be added to Agents and Teams post-creation. This gives you the flexibility to add tools to an existing Agent or Team instance after initialization, which is useful for dynamic tool management or when you need to conditionally add tools based on runtime requirements.
The whole collection of tools available to an Agent or Team can also be updated by using the `set_tools` call. Note that this will remove any other tools already assigned to your Agent or Team and override it with the list of tools provided to `set_tools`.

## Agent Example

Create your own tool, for example `get_weather`. Then call `add_tool` to attach it to your Agent.

```python add_agent_tool_post_initialization.py
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
    model=OpenAIChat(id="gpt-4o-mini"),
    markdown=True,
)

agent.print_response("What can you do?", stream=True)

agent.add_tool(get_weather)

agent.print_response("What is the weather in San Francisco?", stream=True)
```

