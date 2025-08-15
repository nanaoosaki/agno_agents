---
title: Audio Input (Local file)
category: misc
source_lines: 41261-41279
line_count: 18
---

# Audio Input (Local file)
Source: https://docs.agno.com/examples/models/gemini/audio_input_local_file_upload



## Code

```python cookbook/models/google/gemini/audio_input_local_file_upload.py
from pathlib import Path
from agno.agent import Agent
from agno.media import Audio
from agno.models.google import Gemini

agent = Agent(
    model=Gemini(id="gemini-2.0-flash-exp"),
    markdown=True,
)

