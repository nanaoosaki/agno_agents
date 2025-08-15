---
title: Redis Workflow Storage
category: misc
source_lines: 25529-25563
line_count: 34
---

# Redis Workflow Storage
Source: https://docs.agno.com/examples/concepts/storage/workflow_storage/redis



Agno supports using Redis as a storage backend for Workflows using the `RedisStorage` class.

## Usage

### Run Redis

Install [docker desktop](https://docs.docker.com/desktop/install/mac-install/) and run **Redis** on port **6379** using:

```bash
docker run --name my-redis -p 6379:6379 -d redis
```

```python redis_storage_for_workflow.py
"""
Run: `pip install openai httpx newspaper4k redis agno` to install the dependencies
"""

import json
from typing import Iterator

import httpx
from agno.agent import Agent
from agno.run.response import RunResponse
from agno.storage.redis import RedisStorage
from agno.tools.newspaper4k import Newspaper4kTools
from agno.utils.log import logger
from agno.utils.pprint import pprint_run_response
from agno.workflow import Workflow

