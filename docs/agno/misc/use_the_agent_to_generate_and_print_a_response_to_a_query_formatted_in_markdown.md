---
title: Use the agent to generate and print a response to a query, formatted in Markdown
category: misc
source_lines: 21394-21430
line_count: 36
---

# Use the agent to generate and print a response to a query, formatted in Markdown
agent.print_response(
    "What is the first step of making Gluai Buat Chi from the knowledge base?",
    markdown=True,
)
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Install Ollama">
    Follow the installation instructions at [Ollama's website](https://ollama.ai)
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U lancedb sqlalchemy agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/agent_concepts/rag/rag_with_lance_db_and_sqlite.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/rag/rag_with_lance_db_and_sqlite.py
      ```
    </CodeGroup>
  </Step>
</Steps>


