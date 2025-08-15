---
title: Image Generation
category: misc
source_lines: 35236-35261
line_count: 25
---

# Image Generation
Source: https://docs.agno.com/examples/getting-started/image-generation



This example shows how to create an AI agent that generates images using DALL-E.
You can use this agent to create various types of images, from realistic photos to artistic
illustrations and creative concepts.

Example prompts to try:

* "Create a surreal painting of a floating city in the clouds at sunset"
* "Generate a photorealistic image of a cozy coffee shop interior"
* "Design a cute cartoon mascot for a tech startup"
* "Create an artistic portrait of a cyberpunk samurai"

## Code

```python image_generation.py
from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.dalle import DalleTools

