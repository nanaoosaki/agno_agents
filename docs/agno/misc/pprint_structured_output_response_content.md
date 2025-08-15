---
title: pprint(structured_output_response.content)
category: misc
source_lines: 47664-47701
line_count: 37
---

# pprint(structured_output_response.content)

json_mode_agent.print_response("New York")
structured_output_agent.print_response("New York")
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
    pip install -U openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/models/openai/responses/structured_output.py
      ```

      ```bash Windows
      python cookbook/models/openai/responses/structured_output.py
      ```
    </CodeGroup>
  </Step>
</Steps>


