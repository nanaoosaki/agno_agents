---
title: Image Agent with Bytes
category: misc
source_lines: 49201-49230
line_count: 29
---

# Image Agent with Bytes
Source: https://docs.agno.com/examples/models/xai/image_agent_bytes



## Code

```python cookbook/models/xai/image_agent_bytes.py
from pathlib import Path

from agno.agent import Agent
from agno.media import Image
from agno.models.xai import xAI
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.utils.media import download_image

agent = Agent(
    model=xAI(id="grok-2-vision-latest"),
    tools=[DuckDuckGoTools()],
    markdown=True,
)

image_path = Path(__file__).parent.joinpath("sample.jpg")

download_image(
    url="https://upload.wikimedia.org/wikipedia/commons/0/0c/GoldenGateBridge-001.jpg",
    output_path=str(image_path),
)

