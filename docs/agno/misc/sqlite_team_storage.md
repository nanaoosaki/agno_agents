---
title: Sqlite Team Storage
category: misc
source_lines: 24846-24927
line_count: 81
---

# Sqlite Team Storage
Source: https://docs.agno.com/examples/concepts/storage/team_storage/sqlite



Agno supports using Sqlite as a storage backend for Teams using the `SqliteStorage` class.

## Usage

You need to provide either `db_url`, `db_file` or `db_engine`. The following example uses `db_file`.

```python sqlite_storage_for_team.py
"""
Run: `pip install openai duckduckgo-search newspaper4k lxml_html_clean agno` to install the dependencies
"""

from typing import List

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage
from agno.team import Team
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.hackernews import HackerNewsTools
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


hn_team = Team(
    name="HackerNews Team",
    mode="coordinate",
    model=OpenAIChat("gpt-4o"),
    members=[hn_researcher, web_searcher],
    storage=SqliteStorage(
        table_name="team_sessions", db_file="tmp/data.db", auto_upgrade_schema=True
    ),
    instructions=[
        "First, search hackernews for what the user is asking about.",
        "Then, ask the web searcher to search for each story to get more information.",
        "Finally, provide a thoughtful and engaging summary.",
    ],
    response_model=Article,
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
    show_members_responses=True,
)

hn_team.print_response("Write an article about the top 2 stories on hackernews")
```

## Params

<Snippet file="storage-sqlite-params.mdx" />

## Developer Resources

* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/storage/sqllite_storage/sqlite_storage_for_team.py)


