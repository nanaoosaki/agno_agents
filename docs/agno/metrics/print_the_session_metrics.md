---
title: Print the session metrics
category: metrics
source_lines: 20240-20276
line_count: 36
---

# Print the session metrics
print("---" * 5, "Session Metrics", "---" * 5)
pprint(agent.session_metrics)
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
    pip install -U openai agno yfinance rich
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/agent_concepts/other/agent_metrics.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/other/agent_metrics.py
      ```
    </CodeGroup>
  </Step>
</Steps>


