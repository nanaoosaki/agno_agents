---
title: ChromaDB Agent Knowledge
category: knowledge
source_lines: 80099-80207
line_count: 108
---

# ChromaDB Agent Knowledge
Source: https://docs.agno.com/vectordb/chroma



## Setup

```shell
pip install chromadb
```

## Example

```python agent_with_knowledge.py
import typer
from rich.prompt import Prompt
from typing import Optional

from agno.agent import Agent
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.chroma import ChromaDb

knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=ChromaDb(collection="recipes"),
)

def pdf_agent(user: str = "user"):
    run_id: Optional[str] = None

    agent = Agent(
        run_id=run_id,
        user_id=user,
        knowledge_base=knowledge_base,
        use_tools=True,
        show_tool_calls=True,
        debug_mode=True,
    )
    if run_id is None:
        run_id = agent.run_id
        print(f"Started Run: {run_id}\n")
    else:
        print(f"Continuing Run: {run_id}\n")

    while True:
        message = Prompt.ask(f"[bold] :sunglasses: {user} [/bold]")
        if message in ("exit", "bye"):
            break
        agent.print_response(message)

if __name__ == "__main__":
    # Comment out after first run
    knowledge_base.load(recreate=False)

    typer.run(pdf_agent)
```

<Card title="Async Support ⚡">
  <div className="mt-2">
    <p>
      ChromaDB also supports asynchronous operations, enabling concurrency and leading to better performance.
    </p>

    ```python async_chroma_db.py
    # install chromadb - `pip install chromadb`

    import asyncio

    from agno.agent import Agent
    from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
    from agno.vectordb.chroma import ChromaDb

    # Initialize ChromaDB
    vector_db = ChromaDb(collection="recipes", path="tmp/chromadb", persistent_client=True)

    # Create knowledge base
    knowledge_base = PDFUrlKnowledgeBase(
        urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
        vector_db=vector_db,
    )

    # Create and use the agent
    agent = Agent(knowledge=knowledge_base, show_tool_calls=True)

    if __name__ == "__main__":
        # Comment out after first run
        asyncio.run(knowledge_base.aload(recreate=False))

        # Create and use the agent
        asyncio.run(agent.aprint_response("How to make Tom Kha Gai", markdown=True))
    ```

    <Tip className="mt-4">
      Use <code>aload()</code> and <code>aprint\_response()</code> methods with <code>asyncio.run()</code> for non-blocking operations in high-throughput applications.
    </Tip>
  </div>
</Card>

## ChromaDb Params

<Snippet file="vectordb_chromadb_params.mdx" />

## Developer Resources

* View [Cookbook (Sync)](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/vector_dbs/chroma_db/chroma_db.py)
* View [Cookbook (Async)](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/vector_dbs/chroma_db/async_chroma_db.py)


