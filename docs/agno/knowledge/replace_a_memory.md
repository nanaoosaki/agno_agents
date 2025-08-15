---
title: Replace a memory
category: knowledge
source_lines: 16601-16639
line_count: 38
---

# Replace a memory
print("\nReplacing memory")
memory.replace_user_memory(
    memory_id=memory_id_1,
    memory=UserMemory(memory="The user's name is Jane Mary Doe", topics=["name"]),
    user_id=jane_doe_id,
)
print("Memory replaced")
memories = memory.get_user_memories(user_id=jane_doe_id)
print("Memories:")
pprint(memories)
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Install libraries">
    ```bash
    pip install -U agno rich
    ```
  </Step>

  <Step title="Run Example">
    <CodeGroup>
      ```bash Mac
      python cookbook/agent_concepts/memory/01_standalone_memory.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/memory/01s̄_standalone_memory.py
      ```
    </CodeGroup>
  </Step>
</Steps>


