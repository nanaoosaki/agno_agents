---
title: Run the agent asynchronously
category: misc
source_lines: 46310-46351
line_count: 41
---

# Run the agent asynchronously
async def run_agents_async():
    await structured_output_agent.aprint_response("Llamas ruling the world")


asyncio.run(run_agents_async())
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Install Ollama">
    Follow the [installation guide](https://github.com/ollama/ollama?tab=readme-ov-file#macos) and run:

    ```bash
    ollama pull llama3.2
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U ollama agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/models/ollama/structured_output.py
      ```

      ```bash Windows
      python cookbook/models/ollama/structured_output.py
      ```
    </CodeGroup>
  </Step>
</Steps>


