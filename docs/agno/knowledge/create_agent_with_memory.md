---
title: Create agent with memory
category: knowledge
source_lines: 17942-18002
line_count: 60
---

# Create agent with memory
agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    memory=memory,
    enable_user_memories=True,
)

async def run_example():
    # Use the agent with MongoDB-backed memory
    await agent.aprint_response(
        "My name is Jane Smith and I enjoy painting and photography.",
        user_id="jane@example.com",
    )
    
    await agent.aprint_response(
        "What are my creative interests?",
        user_id="jane@example.com",
    )
    
    # Display the memories stored in MongoDB
    memories = memory.get_user_memories(user_id="jane@example.com")
    print("Memories stored in MongoDB:")
    for i, m in enumerate(memories):
        print(f"{i}: {m.memory}")

if __name__ == "__main__":
    asyncio.run(run_example())
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
    pip install -U agno openai pymongo
    ```
  </Step>

  <Step title="Run Example">
    <CodeGroup>
      ```bash Mac/Linux
      python cookbook/agent_concepts/memory/mongodb_memory.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/memory/mongodb_memory.py
      ```
    </CodeGroup>
  </Step>
</Steps>


