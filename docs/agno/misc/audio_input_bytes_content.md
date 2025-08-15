---
title: Audio Input (Bytes Content)
category: misc
source_lines: 41121-41141
line_count: 20
---

# Audio Input (Bytes Content)
Source: https://docs.agno.com/examples/models/gemini/audio_input_bytes_content



## Code

```python cookbook/models/google/gemini/audio_input_bytes_content.py
import requests
from agno.agent import Agent
from agno.media import Audio
from agno.models.google import Gemini

agent = Agent(
    model=Gemini(id="gemini-2.0-flash-exp"),
    markdown=True,
)

url = "https://openaiassets.blob.core.windows.net/$web/API/docs/audio/alloy.wav"

