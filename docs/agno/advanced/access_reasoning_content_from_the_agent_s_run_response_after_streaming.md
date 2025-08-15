---
title: Access reasoning_content from the agent's run_response after streaming
category: advanced
source_lines: 21757-21802
line_count: 45
---

# Access reasoning_content from the agent's run_response after streaming
print("\n--- reasoning_content from agent.run_response after streaming ---")
if (
    hasattr(streaming_agent_with_model, "run_response")
    and streaming_agent_with_model.run_response
    and hasattr(streaming_agent_with_model.run_response, "reasoning_content")
    and streaming_agent_with_model.run_response.reasoning_content
):
    print(streaming_agent_with_model.run_response.reasoning_content)
else:
    print("No reasoning_content found in agent.run_response after streaming")

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

  <Step title="Run Example">
    <CodeGroup>
      ```bash Mac
      python cookbook/reasoning/agents/capture_reasoning_content_default_COT.py
      ```

      ```bash Windows
      python cookbook/reasoning/agents/capture_reasoning_content_default_COT.py
      ```
    </CodeGroup>
  </Step>
</Steps>


