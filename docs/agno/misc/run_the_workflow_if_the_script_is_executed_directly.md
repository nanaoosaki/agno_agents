---
title: Run the workflow if the script is executed directly
category: misc
source_lines: 83399-83475
line_count: 76
---

# Run the workflow if the script is executed directly
if __name__ == "__main__":
    import random

    from rich.prompt import Prompt

    # Fun example prompts to showcase the generator's versatility
    example_prompts = [
        "Why Cats Secretly Run the Internet",
        "The Science Behind Why Pizza Tastes Better at 2 AM",
        "Time Travelers' Guide to Modern Social Media",
        "How Rubber Ducks Revolutionized Software Development",
        "The Secret Society of Office Plants: A Survival Guide",
        "Why Dogs Think We're Bad at Smelling Things",
        "The Underground Economy of Coffee Shop WiFi Passwords",
        "A Historical Analysis of Dad Jokes Through the Ages",
    ]

    # Get topic from user
    topic = Prompt.ask(
        "[bold]Enter a blog post topic[/bold] (or press Enter for a random example)\n✨",
        default=random.choice(example_prompts),
    )

    # Convert the topic to a URL-safe string for use in session_id
    url_safe_topic = topic.lower().replace(" ", "-")

    # Initialize the blog post generator workflow
    # - Creates a unique session ID based on the topic
    # - Sets up SQLite storage for caching results
    generate_blog_post = BlogPostGenerator(
        session_id=f"generate-blog-post-on-{url_safe_topic}",
        storage=SqliteStorage(
            table_name="generate_blog_post_workflows",
            mode="workflow",
            auto_upgrade_schema=True,
            db_file="tmp/agno_workflows.db",
        ),
        debug_mode=True,
    )

    # Execute the workflow with caching enabled
    # Returns an iterator of RunResponse objects containing the generated content
    blog_post: Iterator[RunResponse] = generate_blog_post.run(
        topic=topic,
        use_search_cache=True,
        use_scrape_cache=True,
        use_cached_report=True,
    )

    # Print the response
    pprint_run_response(blog_post, markdown=True)
```

To convert this into **Workflows 2.0** structure, either we can break down the workflow into smaller steps and follow the [development guide](/workflows_2/types_of_workflows).
Or for simplicity we can directly replace the run method to a single custom function executor as mentioned [here](/workflows_2/types_of_workflows#2-fully-python-workflow).

It will look like this:

```python
import asyncio
import json
from textwrap import dedent
from typing import Dict, Optional

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage
from agno.tools.googlesearch import GoogleSearchTools
from agno.tools.newspaper4k import Newspaper4kTools
from agno.utils.log import logger
from agno.utils.pprint import pprint_run_response
from agno.workflow.v2.workflow import Workflow
from pydantic import BaseModel, Field


