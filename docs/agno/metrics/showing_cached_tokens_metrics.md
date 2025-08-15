---
title: Showing cached tokens metrics
category: metrics
source_lines: 20161-20196
line_count: 35
---

# Showing cached tokens metrics
print(f"Cached tokens: {agent.run_response.metrics['cached_tokens']}")
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
    pip install -U requests openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/agent_concepts/other/agent_extra_metrics.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/other/agent_extra_metrics.py
      ```
    </CodeGroup>
  </Step>
</Steps>


