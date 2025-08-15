---
title: Redis Team Storage
category: misc
source_lines: 24634-24666
line_count: 32
---

# Redis Team Storage
Source: https://docs.agno.com/examples/concepts/storage/team_storage/redis



Agno supports using Redis as a storage backend for Teams using the `RedisStorage` class.

## Usage

### Run Redis

Install [docker desktop](https://docs.docker.com/desktop/install/mac-install/) and run **Redis** on port **6379** using:

```bash
docker run --name my-redis -p 6379:6379 -d redis
```

```python redis_storage_for_team.py
"""
Run: `pip install openai duckduckgo-search newspaper4k lxml_html_clean agno redis` to install the dependencies
"""

from typing import List

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.storage.redis import RedisStorage
from agno.team import Team
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.hackernews import HackerNewsTools
from pydantic import BaseModel

