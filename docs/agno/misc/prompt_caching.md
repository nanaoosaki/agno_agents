---
title: Prompt Caching
category: misc
source_lines: 37367-37421
line_count: 54
---

# Prompt Caching
Source: https://docs.agno.com/examples/models/anthropic/prompt_caching

Learn how to use prompt caching with Anthropic models and Agno.

Prompt caching can help reducing processing time and costs. Consider it if you are using the same prompt multiple times in any flow.

You can read more about prompt caching with Anthropic models [here](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching).

## Usage

To use prompt caching in your Agno setup, pass the `cache_system_prompt` argument when initializing the `Claude` model:

```python
from agno.agent import Agent
from agno.models.anthropic import Claude

agent = Agent(
    model=Claude(
        id="claude-3-5-sonnet-20241022",
        cache_system_prompt=True,
    ),
)
```

Notice that for prompt caching to work, the prompt needs to be of a certain length. You can read more about this on Anthropic's [docs](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching#cache-limitations).

## Extended cache

You can also use Anthropic's extended cache beta feature. This updates the cache duration from 5 minutes to 1 hour. To activate it, pass the `extended_cache_time` argument and the following beta header:

```python
from agno.agent import Agent
from agno.models.anthropic import Claude

agent = Agent(
    model=Claude(
        id="claude-3-5-sonnet-20241022",
        default_headers={"anthropic-beta": "extended-cache-ttl-2025-04-11"},
        cache_system_prompt=True,
        extended_cache_time=True,
    ),
)
```

## Working example

```python cookbook/models/anthropic/prompt_caching_extended.py
from pathlib import Path

from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.utils.media import download_file

