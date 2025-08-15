---
title: Redis Storage
category: misc
source_lines: 69084-69106
line_count: 22
---

# Redis Storage
Source: https://docs.agno.com/storage/redis



Agno supports using Redis as a storage backend for Agents using the `RedisStorage` class.

## Usage

### Run Redis

Install [docker desktop](https://docs.docker.com/desktop/install/mac-install/) and run **Redis** on port **6379** using:

```bash
docker run --name my-redis -p 6379:6379 -d redis
```

```python redis_storage_for_agent.py
from agno.agent import Agent
from agno.storage.redis import RedisStorage
from agno.tools.duckduckgo import DuckDuckGoTools

