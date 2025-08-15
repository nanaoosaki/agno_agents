---
title: Giphy Tools
category: tools
source_lines: 28802-28861
line_count: 59
---

# Giphy Tools
Source: https://docs.agno.com/examples/concepts/tools/others/giphy



## Code

```python cookbook/tools/giphy_tools.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.giphy import GiphyTools

gif_agent = Agent(
    name="Gif Generator Agent",
    model=OpenAIChat(id="gpt-4o"),
    tools=[GiphyTools(limit=5)],
    description="You are an AI agent that can generate gifs using Giphy.",
    instructions=[
        "When the user asks you to create a gif, come up with the appropriate Giphy query and use the `search_gifs` tool to find the appropriate gif.",
    ],
    debug_mode=True,
    show_tool_calls=True,
)

gif_agent.print_response("I want a gif to send to a friend for their birthday.")
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export GIPHY_API_KEY=xxx
    export OPENAI_API_KEY=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U giphy_client openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/tools/giphy_tools.py
      ```

      ```bash Windows
      python cookbook/tools/giphy_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


