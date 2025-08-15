---
title: New session, so new shopping list
category: misc
source_lines: 23549-23591
line_count: 42
---

# New session, so new shopping list
agent.print_response(
    "Add chicken and soup to my list.",
    stream=True,
    user_id=user_id_2,
    session_id="user_3_session_2",
)

print(f"Final shopping lists: \n{json.dumps(shopping_list, indent=2)}")
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
      python cookbook/agent_concepts/state/session_state_user_id.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/state/session_state_user_id.py
      ```
    </CodeGroup>
  </Step>
</Steps>


