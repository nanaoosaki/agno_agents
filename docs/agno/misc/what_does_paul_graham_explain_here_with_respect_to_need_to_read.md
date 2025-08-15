---
title: What does Paul Graham explain here with respect to need to read?
category: misc
source_lines: 9820-9855
line_count: 35
---

# What does Paul Graham explain here with respect to need to read?

```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API keys (optional)">
    ```bash
    export OPENAI_API_KEY=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U agno "uvicorn[standard]" openai duckduckgo-search yfinance lancedb sqlalchemy 
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/apps/playground/reasoning_demo.py
      ```

      ```bash Windows
      python cookbook/apps/playground/reasoning_demo.py
      ```
    </CodeGroup>
  </Step>
</Steps>


