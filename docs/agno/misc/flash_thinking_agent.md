---
title: Flash Thinking Agent
category: misc
source_lines: 41426-41479
line_count: 53
---

# Flash Thinking Agent
Source: https://docs.agno.com/examples/models/gemini/flash_thinking



## Code

```python cookbook/models/google/gemini/flash_thinking_agent.py
from agno.agent import Agent
from agno.models.google import Gemini

task = (
    "Three missionaries and three cannibals need to cross a river. "
    "They have a boat that can carry up to two people at a time. "
    "If, at any time, the cannibals outnumber the missionaries on either side of the river, the cannibals will eat the missionaries. "
    "How can all six people get across the river safely? Provide a step-by-step solution and show the solutions as an ascii diagram"
)

agent = Agent(model=Gemini(id="gemini-2.0-flash-thinking-exp-1219"), markdown=True)
agent.print_response(task, stream=True)
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export GOOGLE_API_KEY=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U google-genai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/models/google/gemini/flash_thinking_agent.py
      ```

      ```bash Windows
      python cookbook/models/google/gemini/flash_thinking_agent.py
      ```
    </CodeGroup>
  </Step>
</Steps>


