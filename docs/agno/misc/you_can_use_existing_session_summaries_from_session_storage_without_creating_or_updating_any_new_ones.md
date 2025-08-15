---
title: You can use existing session summaries from session storage without creating or updating any new ones.
category: misc
source_lines: 17867-17904
line_count: 37
---

# You can use existing session summaries from session storage without creating or updating any new ones.
agent = Agent(
    model=Gemini(id="gemini-2.0-flash-exp"),
    memory=memory,
    storage=PostgresStorage(table_name="agent_sessions", db_url=db_url),
    add_session_summary_references=True,
    session_id=session_id,
)

agent.print_response("What are my hobbies?", user_id=user_id)
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
      python 13_session_summary_references.py
      ```

      ```bash Windows
      python 13_session_summary_references.py
      ```
    </CodeGroup>
  </Step>
</Steps>


