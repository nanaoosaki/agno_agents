---
title: Azure OpenAI o1
category: misc
source_lines: 21942-21994
line_count: 52
---

# Azure OpenAI o1
Source: https://docs.agno.com/examples/concepts/reasoning/models/azure-openai/o1



## Code

```python cookbook/reasoning/models/azure_openai/o1.py
from agno.agent import Agent
from agno.models.azure.openai_chat import AzureOpenAI

agent = Agent(model=AzureOpenAI(id="o1"))
agent.print_response(
    "Solve the trolley problem. Evaluate multiple ethical frameworks. "
    "Include an ASCII diagram of your solution.",
    stream=True,
)
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export AZURE_OPENAI_API_KEY=xxx
    export AZURE_OPENAI_ENDPOINT=xxx
    export AZURE_DEPLOYMENT=xxx
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
      python cookbook/reasoning/models/azure_openai/o1.py
      ```

      ```bash Windows
      python cookbook/reasoning/models/azure_openai/o1.py
      ```
    </CodeGroup>
  </Step>
</Steps>


