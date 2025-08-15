---
title: Video Generation
category: misc
source_lines: 36470-36495
line_count: 25
---

# Video Generation
Source: https://docs.agno.com/examples/getting-started/video-generation



This example shows how to create an AI agent that generates videos using ModelsLabs.
You can use this agent to create various types of short videos, from animated scenes
to creative visual stories.

Example prompts to try:

* "Create a serene video of waves crashing on a beach at sunset"
* "Generate a magical video of butterflies flying in a enchanted forest"
* "Create a timelapse of a blooming flower in a garden"
* "Generate a video of northern lights dancing in the night sky"

## Code

```python video_generation.py
from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.models_labs import ModelsLabTools

