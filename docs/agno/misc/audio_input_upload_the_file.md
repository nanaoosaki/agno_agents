---
title: Audio Input (Upload the file)
category: misc
source_lines: 41182-41202
line_count: 20
---

# Audio Input (Upload the file)
Source: https://docs.agno.com/examples/models/gemini/audio_input_file_upload



## Code

```python cookbook/models/google/gemini/audio_input_file_upload.py
from pathlib import Path

from agno.agent import Agent
from agno.media import Audio
from agno.models.google import Gemini

model = Gemini(id="gemini-2.0-flash-exp")
agent = Agent(
    model=model,
    markdown=True,
)

