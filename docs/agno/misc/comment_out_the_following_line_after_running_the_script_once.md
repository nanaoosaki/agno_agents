---
title: Comment out the following line after running the script once
category: misc
source_lines: 18304-18354
line_count: 50
---

# Comment out the following line after running the script once
client.add(messages, user_id=user_id)

agent = Agent(
    model=OpenAIChat(),
    context={"memory": client.get_all(user_id=user_id)},
    add_context=True,
)
run: RunResponse = agent.run("What do you know about me?")

pprint_run_response(run)

messages = [{"role": i.role, "content": str(i.content)} for i in (run.messages or [])]
client.add(messages, user_id=user_id)
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API keys">
    ```bash
    export OPENAI_API_KEY=xxx
    export MEM0_API_KEY=xxx (optional)
    export MEM0_ORG_ID=xxx (optional)
    export MEM0_PROJECT_ID=xxx (optional)
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U openai mem0 agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/agent_concepts/memory/mem0_memory.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/memory/mem0_memory.py
      ```
    </CodeGroup>
  </Step>
</Steps>


