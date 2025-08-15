---
title: Ask the agent about the knowledge base
category: knowledge
source_lines: 13389-13432
line_count: 43
---

# Ask the agent about the knowledge base
agent.print_response("Ask me about something from the knowledge base", markdown=True)
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Install libraries">
    ```bash
    pip install -U sqlalchemy 'psycopg[binary]' pgvector python-docx agno
    ```
  </Step>

  <Step title="Run PgVector">
    ```bash
    docker run -d \
      -e POSTGRES_DB=ai \
      -e POSTGRES_USER=ai \
      -e POSTGRES_PASSWORD=ai \
      -e PGDATA=/var/lib/postgresql/data/pgdata \
      -v pgvolume:/var/lib/postgresql/data \
      -p 5532:5432 \
      --name pgvector \
      agnohq/pgvector:16
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/agent_concepts/knowledge/docx_kb.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/knowledge/docx_kb.py
      ```
    </CodeGroup>
  </Step>
</Steps>


