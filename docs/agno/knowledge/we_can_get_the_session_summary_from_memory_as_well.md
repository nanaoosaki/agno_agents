---
title: We can get the session summary from memory as well
category: knowledge
source_lines: 17209-17247
line_count: 38
---

# We can get the session summary from memory as well
session_summary = memory.get_session_summary(
    session_id=session_id_2, user_id=mark_gonzales_id
)
pprint(session_summary)
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
    pip install -U agno openai
    ```
  </Step>

  <Step title="Run Example">
    <CodeGroup>
      ```bash Mac
      python cookbook/agent_concepts/memory/08_agent_with_summaries.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/memory/08_agent_with_summaries.py
      ```
    </CodeGroup>
  </Step>
</Steps>


