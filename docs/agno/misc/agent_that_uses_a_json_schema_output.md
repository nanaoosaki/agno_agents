---
title: Agent that uses a JSON schema output
category: misc
source_lines: 39700-39741
line_count: 41
---

# Agent that uses a JSON schema output
json_schema_output_agent = Agent(
    model=Cerebras(id="llama-4-scout-17b-16e-instruct"),
    description="You are a helpful assistant. Summarize the movie script based on the location in a JSON object.",
    response_model=MovieScript,
)

json_schema_output_agent.print_response("New York")
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
    pip install -U cerebras-cloud-sdk agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/models/cerebras/basic_json_schema.py
      ```

      ```bash Windows
      python cookbook/models/cerebras/basic_json_schema.py
      ```
    </CodeGroup>
  </Step>
</Steps>


