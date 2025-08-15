---
title: agent.print_response("Share the NVDA stock price and analyst recommendations", stream=True)
category: misc
source_lines: 43523-43559
line_count: 36
---

# agent.print_response("Share the NVDA stock price and analyst recommendations", stream=True)
agent.print_response("Summarize fundamentals for TSLA", stream=True)
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export LANGDB_API_KEY=xxx
    export LANGDB_PROJECT_ID=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U yfinance agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/models/langdb/finance_agent.py
      ```

      ```bash Windows
      python cookbook/models/langdb/finance_agent.py
      ```
    </CodeGroup>
  </Step>
</Steps>


