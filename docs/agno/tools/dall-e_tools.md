---
title: DALL-E Tools
category: tools
source_lines: 28355-28428
line_count: 73
---

# DALL-E Tools
Source: https://docs.agno.com/examples/concepts/tools/others/dalle



## Code

```python cookbook/tools/dalle_tools.py
from pathlib import Path

from agno.agent import Agent
from agno.tools.dalle import DalleTools
from agno.utils.media import download_image

agent = Agent(tools=[DalleTools()], name="DALL-E Image Generator")

agent.print_response(
    "Generate an image of a futuristic city with flying cars and tall skyscrapers",
    markdown=True,
)

custom_dalle = DalleTools(
    model="dall-e-3", size="1792x1024", quality="hd", style="natural"
)

agent_custom = Agent(
    tools=[custom_dalle],
    name="Custom DALL-E Generator",
    show_tool_calls=True,
)

response = agent_custom.run(
    "Create a panoramic nature scene showing a peaceful mountain lake at sunset",
    markdown=True,
)
if response.images:
    download_image(
        url=response.images[0].url,
        save_path=Path(__file__).parent.joinpath("tmp/nature.jpg"),
    )
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export OPENAI_API_KEY=xxx  # Required for DALL-E image generation
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/tools/dalle_tools.py
      ```

      ```bash Windows
      python cookbook/tools/dalle_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


