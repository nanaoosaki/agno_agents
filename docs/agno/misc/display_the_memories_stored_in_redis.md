---
title: Display the memories stored in Redis
category: misc
source_lines: 18139-18183
line_count: 44
---

# Display the memories stored in Redis
memories = memory.get_user_memories(user_id=user_id)
print("Memories stored in Redis:")
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
    pip install -U agno openai redis
    ```
  </Step>

  <Step title="Run Redis">
    ```bash
    docker run --name my-redis -p 6379:6379 -d redis
    ```
  </Step>

  <Step title="Run Example">
    <CodeGroup>
      ```bash Mac/Linux
      python cookbook/agent_concepts/memory/redis_memory.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/memory/redis_memory.py
      ```
    </CodeGroup>
  </Step>
</Steps>


