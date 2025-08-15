---
title: Query for Jordan Mitchell's experience and skills with filters in query so that Agent can automatically pick them up
category: misc
source_lines: 16187-16217
line_count: 30
---

# Query for Jordan Mitchell's experience and skills with filters in query so that Agent can automatically pick them up
agent.print_response(
    "Tell me about Jordan Mitchell's experience and skills with jordan_mitchell as user id and document type cv",
    markdown=True,
)
```

## Usage

<Steps>
  <Step title="Install libraries">
    ```bash
    pip install -U agno openai lancedb
    ```
  </Step>

  <Step title="Run the example">
    <CodeGroup>
      ```bash Mac
      python cookbook/agent_concepts/knowledge/filters/text/agentic_filtering.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/knowledge/filters/text/agentic_filtering.py
      ```
    </CodeGroup>
  </Step>
</Steps>


