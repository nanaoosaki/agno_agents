---
title: It uses the default model of the Agent
category: misc
source_lines: 21831-21877
line_count: 46
---

# It uses the default model of the Agent
reasoning_agent = Agent(
    model=OpenAIChat(id="gpt-4o", max_tokens=1200),
    reasoning=True,
    markdown=True,
)
reasoning_agent.print_response(
    "Give me steps to write a python script for fibonacci series",
    stream=True,
    show_full_reasoning=True,
)


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
      python cookbook/reasoning/agents/default_chain_of_thought.py
      ```

      ```bash Windows
      python cookbook/reasoning/agents/default_chain_of_thought.py
      ```
    </CodeGroup>
  </Step>
</Steps>


