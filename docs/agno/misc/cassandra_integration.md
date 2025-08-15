---
title: Cassandra Integration
category: misc
source_lines: 32565-32646
line_count: 81
---

# Cassandra Integration
Source: https://docs.agno.com/examples/concepts/vectordb/cassandra



## Code

```python cookbook/agent_concepts/vector_dbs/cassandra_db.py
from agno.agent import Agent
from agno.embedder.mistral import MistralEmbedder
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.models.mistral import MistralChat
from agno.vectordb.cassandra import Cassandra

try:
    from cassandra.cluster import Cluster
except (ImportError, ModuleNotFoundError):
    raise ImportError(
        "Could not import cassandra-driver python package.Please install it with pip install cassandra-driver."
    )

cluster = Cluster()

session = cluster.connect()
session.execute(
    """
    CREATE KEYSPACE IF NOT EXISTS testkeyspace
    WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 }
    """
)

knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=Cassandra(
        table_name="recipes",
        keyspace="testkeyspace",
        session=session,
        embedder=MistralEmbedder(),
    ),
)

knowledge_base.load(recreate=True)  # Comment out after first run

agent = Agent(
    model=MistralChat(),
    knowledge=knowledge_base,
    show_tool_calls=True,
)

agent.print_response(
    "What are the health benefits of Khao Niew Dam Piek Maphrao Awn?",
    markdown=True,
    show_full_reasoning=True,
)
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Install libraries">
    ```bash
    pip install -U cassandra-driver pypdf openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/agent_concepts/vector_dbs/cassandra_db.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/vector_dbs/cassandra_db.py
      ```
    </CodeGroup>
  </Step>
</Steps>


