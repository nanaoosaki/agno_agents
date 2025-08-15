---
title: Confluence Tools
category: tools
source_lines: 28295-28355
line_count: 60
---

# Confluence Tools
Source: https://docs.agno.com/examples/concepts/tools/others/confluence



## Code

```python cookbook/tools/confluence_tools.py
from agno.agent import Agent
from agno.tools.confluence import ConfluenceTools

agent = Agent(
    name="Confluence agent",
    tools=[ConfluenceTools()],
    show_tool_calls=True,
    markdown=True,
)

agent.print_response("How many spaces are there and what are their names?")
agent.print_response(
    "What is the content present in page 'Large language model in LLM space'"
)
agent.print_response("Can you extract all the page names from 'LLM' space")
agent.print_response("Can you create a new page named 'TESTING' in 'LLM' space")
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API credentials">
    ```bash
    export CONFLUENCE_API_TOKEN=xxx
    export CONFLUENCE_SITE_URL=xxx
    export CONFLUENCE_USERNAME=xxx
    export OPENAI_API_KEY=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U atlassian-python-api openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/tools/confluence_tools.py
      ```

      ```bash Windows
      python cookbook/tools/confluence_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


