---
title: Agent Teams [Deprecated]
category: misc
source_lines: 2481-2555
line_count: 74
---

# Agent Teams [Deprecated]
Source: https://docs.agno.com/agents/teams



<Note>
  Agent Teams were an initial implementation of our multi-agent architecture (2023-2025) that use a transfer/handoff mechanism. After 2 years of experimentation, we've learned that this mechanism is not scalable and do NOT recommend it for complex multi-agent systems.

  Please use the new [Teams](/teams) architecture instead.
</Note>

We can combine multiple Agents to form a team and tackle tasks as a cohesive unit. Here's a simple example that converts an agent into a team to write an article about the top stories on hackernews.

```python hackernews_team.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.hackernews import HackerNewsTools
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.newspaper4k import Newspaper4kTools

hn_researcher = Agent(
    name="HackerNews Researcher",
    model=OpenAIChat("gpt-4o"),
    role="Gets top stories from hackernews.",
    tools=[HackerNewsTools()],
)

web_searcher = Agent(
    name="Web Searcher",
    model=OpenAIChat("gpt-4o"),
    role="Searches the web for information on a topic",
    tools=[DuckDuckGoTools()],
    add_datetime_to_instructions=True,
)

article_reader = Agent(
    name="Article Reader",
    model=OpenAIChat("gpt-4o"),
    role="Reads articles from URLs.",
    tools=[Newspaper4kTools()],
)

hn_team = Agent(
    name="Hackernews Team",
    model=OpenAIChat("gpt-4o"),
    team=[hn_researcher, web_searcher, article_reader],
    instructions=[
        "First, search hackernews for what the user is asking about.",
        "Then, ask the article reader to read the links for the stories to get more information.",
        "Important: you must provide the article reader with the links to read.",
        "Then, ask the web searcher to search for each story to get more information.",
        "Finally, provide a thoughtful and engaging summary.",
    ],
    show_tool_calls=True,
    markdown=True,
)
hn_team.print_response("Write an article about the top 2 stories on hackernews", stream=True)
```

Run the script to see the output.

```bash
pip install -U openai duckduckgo-search newspaper4k lxml_html_clean agno

python hackernews_team.py
```

## How to build Agent Teams

1. Add a `name` and `role` parameter to the member Agents.
2. Create a Team Leader that can delegate tasks to team-members.
3. Use your Agent team just like you would use a regular Agent.


