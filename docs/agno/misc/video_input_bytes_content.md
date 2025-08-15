---
title: Video Input (Bytes Content)
category: misc
source_lines: 41935-41955
line_count: 20
---

# Video Input (Bytes Content)
Source: https://docs.agno.com/examples/models/gemini/video_input_bytes_content



## Code

```python cookbook/models/google/gemini/video_input_bytes_content.py
import requests
from agno.agent import Agent
from agno.media import Video
from agno.models.google import Gemini

agent = Agent(
    model=Gemini(id="gemini-2.0-flash-exp"),
    markdown=True,
)

url = "https://videos.pexels.com/video-files/5752729/5752729-uhd_2560_1440_30fps.mp4"

