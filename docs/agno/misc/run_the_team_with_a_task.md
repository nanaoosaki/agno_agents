---
title: Run the team with a task
category: misc
source_lines: 69828-69930
line_count: 102
---

# Run the team with a task
content_team.print_response("Create a short article about quantum computing")
```

### Research Team

Here's an example of a research team that combines multiple specialized agents:

<Steps>
  <Step title="Create HackerNews Team">
    Create a file `hackernews_team.py`

    ```python hackernews_team.py
    from typing import List

    from agno.agent import Agent
    from agno.models.openai import OpenAIChat
    from agno.team import Team
    from agno.tools.duckduckgo import DuckDuckGoTools
    from agno.tools.hackernews import HackerNewsTools
    from agno.tools.newspaper4k import Newspaper4kTools
    from pydantic import BaseModel

    class Article(BaseModel):
        title: str
        summary: str
        reference_links: List[str]


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
        role="Reads articles from URLs.",
        tools=[Newspaper4kTools()],
    )

    hackernews_team = Team(
        name="HackerNews Team",
        mode="coordinate",
        model=OpenAIChat("gpt-4o"),
        members=[hn_researcher, web_searcher, article_reader],
        instructions=[
            "First, search hackernews for what the user is asking about.",
            "Then, ask the article reader to read the links for the stories to get more information.",
            "Important: you must provide the article reader with the links to read.",
            "Then, ask the web searcher to search for each story to get more information.",
            "Finally, provide a thoughtful and engaging summary.",
        ],
        response_model=Article,
        show_tool_calls=True,
        markdown=True,
        debug_mode=True,
        show_members_responses=True,
    )

    # Run the team
    report = hackernews_team.run(
        "What are the top stories on hackernews?"
    ).content

    print(f"Title: {report.title}")
    print(f"Summary: {report.summary}")
    print(f"Reference Links: {report.reference_links}")
    ```
  </Step>

  <Step title="Run the team">
    Install libraries

    ```shell
    pip install openai duckduckgo-search newspaper4k lxml_html_clean agno
    ```

    Run the team

    ```shell
    python hackernews_team.py
    ```
  </Step>
</Steps>

## Developer Resources

* View [Usecases](/examples/teams/)
* View [Examples](/examples/concepts/storage/team_storage)
* View [Cookbook](https://github.com/agno-agi/agno/tree/main/cookbook/examples/teams)


