---
title: Video to Shorts Agent
category: misc
source_lines: 19360-19399
line_count: 39
---

# Video to Shorts Agent
Source: https://docs.agno.com/examples/concepts/multimodal/video-to-shorts



## Code

```python
import subprocess
import time
from pathlib import Path

from agno.agent import Agent
from agno.media import Video
from agno.models.google import Gemini
from agno.utils.log import logger
from google.generativeai import get_file, upload_file

video_path = Path(__file__).parent.joinpath("sample.mp4")
output_dir = Path("tmp/shorts")

agent = Agent(
    name="Video2Shorts",
    description="Process videos and generate engaging shorts.",
    model=Gemini(id="gemini-2.0-flash-exp"),
    markdown=True,
    debug_mode=True,
    instructions=[
        "Analyze the provided video directly—do NOT reference or analyze any external sources or YouTube videos.",
        "Identify engaging moments that meet the specified criteria for short-form content.",
        """Provide your analysis in a **table format** with these columns:
   - Start Time | End Time | Description | Importance Score""",
        "Ensure all timestamps use MM:SS format and importance scores range from 1-10. ",
        "Focus only on segments between 15 and 60 seconds long.",
        "Base your analysis solely on the provided video content.",
        "Deliver actionable insights to improve the identified segments for short-form optimization.",
    ],
)

