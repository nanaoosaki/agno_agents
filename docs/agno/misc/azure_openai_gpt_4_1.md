---
title: Azure OpenAI GPT 4.1
category: misc
source_lines: 22057-22111
line_count: 54
---

# Azure OpenAI GPT 4.1
Source: https://docs.agno.com/examples/concepts/reasoning/models/azure-openai/reasoning-model-gpt4-1



## Code

```python cookbook/reasoning/models/azure_openai/reasoning_model_gpt_4_1.py
from agno.agent import Agent
from agno.models.azure.openai_chat import AzureOpenAI

agent = Agent(
    model=AzureOpenAI(id="gpt-4o-mini"), reasoning_model=AzureOpenAI(id="gpt-4.1")
)
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
      python cookbook/reasoning/models/azure_openai/reasoning_model_gpt_4_1.py
      ```

      ```bash Windows
      python cookbook/reasoning/models/azure_openai/reasoning_model_gpt_4_1.py
      ```
    </CodeGroup>
  </Step>
</Steps>


