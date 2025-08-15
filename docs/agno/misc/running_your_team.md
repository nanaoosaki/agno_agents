---
title: Running your Team
category: misc
source_lines: 70339-70362
line_count: 23
---

# Running your Team
Source: https://docs.agno.com/teams/run

Learn how to run a team and get the response.

The `Team.run()` function runs the team and generates a response, either as a `TeamRunResponse` object or a stream of `TeamRunResponseEvent` objects.

Many of our examples use `team.print_response()` which is a helper utility to print the response in the terminal. It uses `team.run()` under the hood.

Here's how to run your team. The response is captured in the `response` and `response_stream` variables.

```python
from agno.team import Team
from agno.models.openai import OpenAIChat

agent_1 = Agent(name="News Agent", role="Get the latest news")

agent_2 = Agent(name="Weather Agent", role="Get the weather for the next 7 days")

team = Team(name="News and Weather Team", mode="coordinate", members=[agent_1, agent_2])

response = team.run("What is the weather in Tokyo?")

