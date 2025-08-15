---
title: Planner Tasks Configuration
category: misc
source_lines: 52426-52651
line_count: 225
---

# Planner Tasks Configuration
tasks_config = {
    "analyze_blog": {
        "description": (
            "Analyze the markdown file at {blog_path} to create a developer-focused technical overview\n\n"
            "1. Map out the core idea that the blog discusses\n"
            "2. Identify key sections and what each section is about\n"
            "3. For each section, extract all URLs that appear inside image markdown syntax ![](image_url)\n"
            "4. You must associate these identified image URLs to their corresponding sections, so that we can use them with the tweets as media pieces\n\n"
            "Focus on details that are important for a comprehensive understanding of the blog.\n\n"
        ),
        "expected_output": (
            "A technical analysis containing:\n"
            "- Blog title and core concept/idea\n"
            "- Key technical sections identified with their main points\n"
            "- Important code examples or technical concepts covered\n"
            "- Key takeaways for developers\n"
            "- Relevant URLs to media that are associated with the key sections and can be associated with a tweet, this must be done.\n\n"
        ),
    },
    "create_twitter_thread_plan": {
        "description": (
            "Develop an engaging Twitter thread based on the blog analysis provided and closely follow the writing style provided in the {path_to_example_threads}\n\n"
            "The thread should break down complex technical concepts into digestible, tweet-sized chunks "
            "that maintain technical accuracy while being accessible.\n\n"
            "Plan should include:\n"
            "- A strong hook tweet that captures attention, it should be under 10 words, it must be the same as the title of the blog\n"
            "- Logical flow from basic to advanced concepts\n"
            "- Code snippets or key technical highlights that fit Twitter's format\n"
            "- Relevant URLs to media that are associated with the key sections and must be associated with their corresponding tweets\n"
            "- Clear takeaways for engineering audience\n\n"
            "Make sure to cover:\n"
            "- The core problem being solved\n"
            "- Key technical innovations or approaches\n"
            "- Interesting implementation details\n"
            "- Real-world applications or benefits\n"
            "- Call to action for the conclusion\n"
            "- Add relevant URLs to each tweet that can be associated with a tweet\n\n"
            "Focus on creating a narrative that technical audiences will find valuable "
            "while keeping each tweet concise, accessible, and impactful.\n\n"
        ),
        "expected_output": (
            "A Twitter thread with a list of tweets, where each tweet has the following:\n"
            "- content\n"
            "- URLs to media that are associated with the tweet, whenever possible\n"
            "- is_hook: true if the tweet is a hook tweet, false otherwise\n\n"
        ),
    },
    "create_linkedin_post_plan": {
        "description": (
            "Develop a comprehensive LinkedIn post based on the blog analysis provided\n\n"
            "The post should present technical content in a professional, long-form format "
            "while maintaining engagement and readability.\n\n"
            "Plan should include:\n"
            "- An attention-grabbing opening statement, it should be the same as the title of the blog\n"
            "- Well-structured body that breaks down the technical content\n"
            "- Professional tone suitable for LinkedIn's business audience\n"
            "- One main blog URL placed strategically at the end of the post\n"
            "- Strategic use of line breaks and formatting\n"
            "- Relevant hashtags (3-5 maximum)\n\n"
            "Make sure to cover:\n"
            "- The core technical problem and its business impact\n"
            "- Key solutions and technical approaches\n"
            "- Real-world applications and benefits\n"
            "- Professional insights or lessons learned\n"
            "- Clear call to action\n\n"
            "Focus on creating content that resonates with both technical professionals "
            "and business leaders while maintaining technical accuracy.\n\n"
        ),
        "expected_output": (
            "A LinkedIn post plan containing:\n- content\n- a main blog URL that is associated with the post\n\n"
        ),
    },
}
```

For Scheduling logic, create `scheduler.py`

```python scheduler.py
import datetime
from typing import Any, Dict, Optional

import requests
from agno.utils.log import logger
from dotenv import load_dotenv
from pydantic import BaseModel

from cookbook.workflows.content_creator_workflow.config import (
    HEADERS,
    TYPEFULLY_API_URL,
    PostType,
)

load_dotenv()


def json_to_typefully_content(thread_json: Dict[str, Any]) -> str:
    """Convert JSON thread format to Typefully's format with 4 newlines between tweets."""
    tweets = thread_json["tweets"]
    formatted_tweets = []
    for tweet in tweets:
        tweet_text = tweet["content"]
        if "media_urls" in tweet and tweet["media_urls"]:
            tweet_text += f"\n{tweet['media_urls'][0]}"
        formatted_tweets.append(tweet_text)

    return "\n\n\n\n".join(formatted_tweets)


def json_to_linkedin_content(thread_json: Dict[str, Any]) -> str:
    """Convert JSON thread format to Typefully's format."""
    content = thread_json["content"]
    if "url" in thread_json and thread_json["url"]:
        content += f"\n{thread_json['url']}"
    return content


def schedule_thread(
    content: str,
    schedule_date: str = "next-free-slot",
    threadify: bool = False,
    share: bool = False,
    auto_retweet_enabled: bool = False,
    auto_plug_enabled: bool = False,
) -> Optional[Dict[str, Any]]:
    """Schedule a thread on Typefully."""
    payload = {
        "content": content,
        "schedule-date": schedule_date,
        "threadify": threadify,
        "share": share,
        "auto_retweet_enabled": auto_retweet_enabled,
        "auto_plug_enabled": auto_plug_enabled,
    }

    payload = {key: value for key, value in payload.items() if value is not None}

    try:
        response = requests.post(TYPEFULLY_API_URL, json=payload, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        return None


def schedule(
    thread_model: BaseModel,
    hours_from_now: int = 1,
    threadify: bool = False,
    share: bool = True,
    post_type: PostType = PostType.TWITTER,
) -> Optional[Dict[str, Any]]:
    """
    Schedule a thread from a Pydantic model.

    Args:
        thread_model: Pydantic model containing thread data
        hours_from_now: Hours from now to schedule the thread (default: 1)
        threadify: Whether to let Typefully split the content (default: False)
        share: Whether to get a share URL in response (default: True)

    Returns:
        API response dictionary or None if failed
    """
    try:
        thread_content = ""
        # Convert Pydantic model to dict
        thread_json = thread_model.model_dump()
        logger.info("######## Thread JSON: ", thread_json)
        # Convert to Typefully format
        if post_type == PostType.TWITTER:
            thread_content = json_to_typefully_content(thread_json)
        elif post_type == PostType.LINKEDIN:
            thread_content = json_to_linkedin_content(thread_json)

        # Calculate schedule time
        schedule_date = (
            datetime.datetime.utcnow() + datetime.timedelta(hours=hours_from_now)
        ).isoformat() + "Z"

        if thread_content:
            # Schedule the thread
            response = schedule_thread(
                content=thread_content,
                schedule_date=schedule_date,
                threadify=threadify,
                share=share,
            )

            if response:
                logger.info("Thread scheduled successfully!")
                return response
            else:
                logger.error("Failed to schedule the thread.")
                return None
        return None

    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return None
```

Define workflow in `workflow.py`:

```python workflow.py
import json
from typing import List, Optional

from agno.agent import Agent, RunResponse
from agno.models.openai import OpenAIChat
from agno.run.response import RunEvent
from agno.tools.firecrawl import FirecrawlTools
from agno.utils.log import logger
from agno.workflow import Workflow
from dotenv import load_dotenv
from pydantic import BaseModel, Field

from cookbook.workflows.content_creator_workflow.config import PostType
from cookbook.workflows.content_creator_workflow.prompts import (
    agents_config,
    tasks_config,
)
from cookbook.workflows.content_creator_workflow.scheduler import schedule

