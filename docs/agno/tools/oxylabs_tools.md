---
title: Oxylabs Tools
category: tools
source_lines: 31260-31310
line_count: 50
---

# Oxylabs Tools
Source: https://docs.agno.com/examples/concepts/tools/web_scrape/oxylabs

Use Oxylabs with Agno to scrape and crawl the web.

## Code

```python cookbook/tools/oxylabs_tools.py
from agno.agent import Agent
from agno.tools.oxylabs import OxylabsTools

agent = Agent(
    tools=[OxylabsTools()],
    markdown=True,
    show_tool_calls=True,
)

agent.print_response("""
Let's search for 'latest iPhone reviews' and provide a summary of the top 3 results. 
""")

print(response)
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API keys">
    ```bash
    export OXYLABS_USERNAME=your_oxylabs_username
    export OXYLABS_PASSWORD=your_oxylabs_password
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U oxylabs agno openai
    ```
  </Step>

  <Step title="Run the example">
    ```bash
    python cookbook/tools/oxylabs_tools.py
    ```
  </Step>
</Steps>


