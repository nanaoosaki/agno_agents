---
title: Audio Output Agent
category: misc
source_lines: 46465-46478
line_count: 13
---

# Audio Output Agent
Source: https://docs.agno.com/examples/models/openai/chat/audio_output_agent



## Code

```python cookbook/models/openai/chat/audio_output_agent.py
from agno.agent import Agent, RunResponse  # noqa
from agno.models.openai import OpenAIChat
from agno.utils.audio import write_audio_to_file


