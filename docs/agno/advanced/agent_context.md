---
title: Agent Context
category: advanced
source_lines: 33838-33889
line_count: 51
---

# Agent Context
Source: https://docs.agno.com/examples/getting-started/agent-context



This example shows how to inject external dependencies into an agent. The context is evaluated when the agent is run, acting like dependency injection for Agents.

Example prompts to try:

* "Summarize the top stories on HackerNews"
* "What are the trending tech discussions right now?"
* "Analyze the current top stories and identify trends"
* "What's the most upvoted story today?"

## Code

```python agent_context.py
import json
from textwrap import dedent

import httpx
from agno.agent import Agent
from agno.models.openai import OpenAIChat


def get_top_hackernews_stories(num_stories: int = 5) -> str:
    """Fetch and return the top stories from HackerNews.

    Args:
        num_stories: Number of top stories to retrieve (default: 5)
    Returns:
        JSON string containing story details (title, url, score, etc.)
    """
    # Get top stories
    stories = [
        {
            k: v
            for k, v in httpx.get(
                f"https://hacker-news.firebaseio.com/v0/item/{id}.json"
            )
            .json()
            .items()
            if k != "kids"  # Exclude discussion threads
        }
        for id in httpx.get(
            "https://hacker-news.firebaseio.com/v0/topstories.json"
        ).json()[:num_stories]
    ]
    return json.dumps(stories, indent=4)


