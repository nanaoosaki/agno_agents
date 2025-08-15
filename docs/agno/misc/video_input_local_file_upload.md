---
title: Video Input (Local File Upload)
category: misc
source_lines: 42086-42105
line_count: 19
---

# Video Input (Local File Upload)
Source: https://docs.agno.com/examples/models/gemini/video_input_local_file_upload



## Code

```python cookbook/models/google/gemini/video_input_local_file_upload.py
from pathlib import Path

from agno.agent import Agent
from agno.media import Video
from agno.models.google import Gemini

agent = Agent(
    model=Gemini(id="gemini-2.0-flash-exp"),
    markdown=True,
)

