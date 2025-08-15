---
title: Display the memories stored in SQLite
category: misc
source_lines: 18245-18283
line_count: 38
---

# Display the memories stored in SQLite
memories = memory.get_user_memories(user_id=user_id)
print("Memories stored in SQLite:")
for i, m in enumerate(memories):
    print(f"{i}: {m.memory}")
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set environment variables">
    ```bash
    export OPENAI_API_KEY=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U agno openai
    ```
  </Step>

  <Step title="Run Example">
    <CodeGroup>
      ```bash Mac/Linux
      python cookbook/agent_concepts/memory/sqlite_memory.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/memory/sqlite_memory.py
      ```
    </CodeGroup>
  </Step>
</Steps>


