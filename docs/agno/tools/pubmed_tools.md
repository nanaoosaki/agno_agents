---
title: PubMed Tools
category: tools
source_lines: 30205-30255
line_count: 50
---

# PubMed Tools
Source: https://docs.agno.com/examples/concepts/tools/search/pubmed



## Code

```python cookbook/tools/pubmed_tools.py
from agno.agent import Agent
from agno.tools.pubmed import PubMedTools

agent = Agent(
    tools=[PubMedTools()],
    show_tool_calls=True,
    markdown=True,
)
agent.print_response("Find recent research papers about COVID-19 vaccines")
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export OPENAI_API_KEY=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U biopython openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/tools/pubmed_tools.py
      ```

      ```bash Windows
      python cookbook/tools/pubmed_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


