---
title: Agent that uses a structured output
category: misc
source_lines: 45633-45675
line_count: 42
---

# Agent that uses a structured output
structured_output_agent = Agent(
    model=Nebius(id="Qwen/Qwen3-30B-A3B"),
    description="You are a helpful assistant. Summarize the movie script based on the location in a JSON object.",
    response_model=MovieScript,
    debug_mode=True,
)

structured_output_agent.print_response("New York")
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export NEBIUS_API_KEY=xxx
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
      python cookbook/models/nebius/structured_output.py
      ```

      ```bash Windows
      python cookbook/models/nebius/structured_output.py
      ```
    </CodeGroup>
  </Step>
</Steps>


