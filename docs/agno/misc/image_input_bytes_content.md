---
title: Image Input Bytes Content
category: misc
source_lines: 36957-36985
line_count: 28
---

# Image Input Bytes Content
Source: https://docs.agno.com/examples/models/anthropic/image_input_bytes



## Code

```python cookbook/models/anthropic/image_input_bytes.py
from pathlib import Path
from agno.agent import Agent
from agno.media import Image
from agno.models.anthropic.claude import Claude
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.utils.media import download_image

agent = Agent(
    model=Claude(id="claude-3-5-sonnet-20241022"),
    tools=[DuckDuckGoTools()],
    markdown=True,
)

image_path = Path(__file__).parent.joinpath("sample.jpg")

download_image(
    url="https://upload.wikimedia.org/wikipedia/commons/0/0c/GoldenGateBridge-001.jpg",
    output_path=str(image_path),
)

