---
title: Image Agent (Bytes Content)
category: misc
source_lines: 47268-47297
line_count: 29
---

# Image Agent (Bytes Content)
Source: https://docs.agno.com/examples/models/openai/responses/image_agent_bytes



## Code

```python cookbook/models/openai/responses/image_agent_bytes.py
from pathlib import Path

from agno.agent import Agent
from agno.media import Image
from agno.models.openai import OpenAIResponses
from agno.tools.googlesearch import GoogleSearchTools
from agno.utils.media import download_image

agent = Agent(
    model=OpenAIResponses(id="gpt-4o"),
    tools=[GoogleSearchTools()],
    markdown=True,
)

image_path = Path(__file__).parent.joinpath("sample.jpg")

download_image(
    url="https://upload.wikimedia.org/wikipedia/commons/0/0c/GoldenGateBridge-001.jpg",
    output_path=str(image_path),
)

