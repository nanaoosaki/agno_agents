---
title: Context In Instructions
category: advanced
source_lines: 11618-11641
line_count: 23
---

# Context In Instructions
Source: https://docs.agno.com/examples/concepts/context/03-context_in_instructions



## Code

```python cookbook/agent_concepts/context/03-context_in_instructions.py
import json
from textwrap import dedent

import httpx
from agno.agent import Agent
from agno.models.openai import OpenAIChat


def get_upcoming_spacex_launches(num_launches: int = 5) -> str:
    url = "https://api.spacexdata.com/v5/launches/upcoming"
    launches = httpx.get(url).json()
    launches = sorted(launches, key=lambda x: x["date_unix"])[:num_launches]
    return json.dumps(launches, indent=4)


