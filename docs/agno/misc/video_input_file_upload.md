---
title: Video Input (File Upload)
category: misc
source_lines: 41996-42018
line_count: 22
---

# Video Input (File Upload)
Source: https://docs.agno.com/examples/models/gemini/video_input_file_upload



## Code

```python cookbook/models/google/gemini/video_input_file_upload.py
import time
from pathlib import Path

from agno.agent import Agent
from agno.media import Video
from agno.models.google import Gemini
from agno.utils.log import logger

model = Gemini(id="gemini-2.0-flash-exp")
agent = Agent(
    model=model,
    markdown=True,
)

