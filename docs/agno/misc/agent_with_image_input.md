---
title: Agent with Image Input
category: misc
source_lines: 37881-37905
line_count: 24
---

# Agent with Image Input
Source: https://docs.agno.com/examples/models/aws/bedrock/image_agent



AWS Bedrock supports image input with models like `amazon.nova-pro-v1:0`. You can use this to analyze images and get information about them.

## Code

```python cookbook/models/aws/bedrock/image_agent.py
from pathlib import Path
from agno.agent import Agent
from agno.media import Image
from agno.models.aws import AwsBedrock
from agno.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=AwsBedrock(id="amazon.nova-pro-v1:0"),
    tools=[DuckDuckGoTools()],
    markdown=True,
)

image_path = Path(__file__).parent.joinpath("sample.jpg")

