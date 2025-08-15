---
title: -*- Print the messages in the memory
category: knowledge
source_lines: 16522-16556
line_count: 34
---

# -*- Print the messages in the memory
pprint(
    [
        m.model_dump(include={"role", "content"})
        for m in agent.get_messages_for_session()
    ]
)
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Install libraries">
    ```bash
    pip install -U agno
    ```
  </Step>

  <Step title="Run Example">
    <CodeGroup>
      ```bash Mac
      python cookbook/agent_concepts/memory/00_builtin_memory.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/memory/00_builtin_memory.py
      ```
    </CodeGroup>
  </Step>
</Steps>


