---
title: You can also get the user memories from the agent
category: misc
source_lines: 16984-17021
line_count: 37
---

# You can also get the user memories from the agent
memories = agent.get_user_memories(user_id=john_doe_id)
print("John Doe's memories:")
pprint(memories)
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export GOOGLE_API_KEY=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U agno google-generativeai
    ```
  </Step>

  <Step title="Run Example">
    <CodeGroup>
      ```bash Mac
      python cookbook/agent_concepts/memory/06_agent_with_memory.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/memory/06_agent_with_memory.py
      ```
    </CodeGroup>
  </Step>
</Steps>


