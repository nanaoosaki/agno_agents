---
title: Custom Tools
category: tools
source_lines: 34869-34923
line_count: 54
---

# Custom Tools
Source: https://docs.agno.com/examples/getting-started/custom-tools



This example shows how to create and use your own custom tool with Agno.
You can replace the Hacker News functionality with any API or service you want!

Some ideas for your own tools:

* Weather data fetcher
* Stock price analyzer
* Personal calendar integration
* Custom database queries
* Local file operations

## Code

```python custom_tools.py
import json
from textwrap import dedent

import httpx
from agno.agent import Agent
from agno.models.openai import OpenAIChat


def get_top_hackernews_stories(num_stories: int = 10) -> str:
    """Use this function to get top stories from Hacker News.

    Args:
        num_stories (int): Number of stories to return. Defaults to 10.

    Returns:
        str: JSON string of top stories.
    """

    # Fetch top story IDs
    response = httpx.get("https://hacker-news.firebaseio.com/v0/topstories.json")
    story_ids = response.json()

    # Fetch story details
    stories = []
    for story_id in story_ids[:num_stories]:
        story_response = httpx.get(
            f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
        )
        story = story_response.json()
        if "text" in story:
            story.pop("text", None)
        stories.append(story)
    return json.dumps(stories)


