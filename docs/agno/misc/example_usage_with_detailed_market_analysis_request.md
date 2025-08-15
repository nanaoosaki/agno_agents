---
title: Example usage with detailed market analysis request
category: misc
source_lines: 49113-49146
line_count: 33
---

# Example usage with detailed market analysis request
finance_agent.print_response(
    "Write a comprehensive report on TSLA",
    stream=True,
    stream_intermediate_steps=True,
)
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export XAI_API_KEY=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U openai yfinance agno
    ```
  </Step>

  <Step title="Run Agent">
    ```bash
    python cookbook/models/xai/finance_agent.py
    ```
  </Step>
</Steps>


