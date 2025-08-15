---
title: pprint(run.content)
category: misc
source_lines: 39339-39377
line_count: 38
---

# pprint(run.content)

agent.print_response("New York")
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
      python cookbook/models/azure/openai/structured_output.py
      ```

      ```bash Windows
      python cookbook/models/azure/openai/structured_output.py
      ```
    </CodeGroup>
  </Step>
</Steps>


