---
title: Print the response in the terminal (streaming)
category: advanced
source_lines: 39866-39901
line_count: 35
---

# Print the response in the terminal (streaming)
agent.print_response("write a two sentence horror story", stream=True)
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export CEREBRAS_API_KEY=xxx
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
      python cookbook/models/cerebras_openai/basic_stream.py
      ```

      ```bash Windows
      python cookbook/models/cerebras_openai/basic_stream.py
      ```
    </CodeGroup>
  </Step>
</Steps>


