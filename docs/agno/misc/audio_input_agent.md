---
title: Audio Input Agent
category: misc
source_lines: 46405-46418
line_count: 13
---

# Audio Input Agent
Source: https://docs.agno.com/examples/models/openai/chat/audio_input_agent



## Code

```python cookbook/models/openai/chat/audio_input_agent.py
import requests
from agno.agent import Agent, RunResponse  # noqa
from agno.media import Audio
from agno.models.openai import OpenAIChat

