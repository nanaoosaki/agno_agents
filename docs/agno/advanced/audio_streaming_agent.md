---
title: Audio Streaming Agent
category: advanced
source_lines: 18553-18567
line_count: 14
---

# Audio Streaming Agent
Source: https://docs.agno.com/examples/concepts/multimodal/audio-streaming



## Code

```python
import base64
import wave
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from typing import Iterator

