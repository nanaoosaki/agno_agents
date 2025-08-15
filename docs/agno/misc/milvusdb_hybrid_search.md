---
title: MilvusDB Hybrid Search
category: misc
source_lines: 12521-12597
line_count: 76
---

# MilvusDB Hybrid Search
Source: https://docs.agno.com/examples/concepts/hybrid-search/milvusdb



## Code

```python cookbook/agent_concepts/knowledge/vector_dbs/milvus_db/milvus_db_hybrid_search.py
import typer
from agno.agent import Agent
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.milvus import Milvus, SearchType
from rich.prompt import Prompt

vector_db = Milvus(
    collection="recipes", uri="tmp/milvus.db", search_type=SearchType.hybrid
)

knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=vector_db,
)


def milvusdb_agent(user: str = "user"):
    agent = Agent(
        user_id=user,
        knowledge=knowledge_base,
        search_knowledge=True,
    )

    while True:
        message = Prompt.ask(f"[bold] :sunglasses: {user} [/bold]")
        if message in ("exit", "bye"):
            break
        agent.print_response(message)


if __name__ == "__main__":
    # Comment out after first run
    knowledge_base.load(recreate=True)

    typer.run(milvusdb_agent)
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
    pip install -U pymilvus tantivy pypdf openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/agent_concepts/knowledge/vector_dbs/milvus_db/milvus_db_hybrid_search.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/knowledge/vector_dbs/milvus_db/milvus_db_hybrid_search.py
      ```
    </CodeGroup>
  </Step>
</Steps>


