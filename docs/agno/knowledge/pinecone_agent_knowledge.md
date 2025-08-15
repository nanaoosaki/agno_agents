---
title: Pinecone Agent Knowledge
category: knowledge
source_lines: 80988-81131
line_count: 143
---

# Pinecone Agent Knowledge
Source: https://docs.agno.com/vectordb/pinecone



## Setup

Follow the instructions in the [Pinecone Setup Guide](https://docs.pinecone.io/guides/get-started/quickstart) to get started quickly with Pinecone.

```shell
pip install pinecone
```

<Info>
  We do not yet support Pinecone v6.x.x. We are actively working to achieve
  compatibility. In the meantime, we recommend using **Pinecone v5.4.2** for the
  best experience.
</Info>

## Example

```python agent_with_knowledge.py
import os
import typer
from typing import Optional
from rich.prompt import Prompt

from agno.agent import Agent
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.pineconedb import PineconeDb

api_key = os.getenv("PINECONE_API_KEY")
index_name = "thai-recipe-hybrid-search"

vector_db = PineconeDb(
    name=index_name,
    dimension=1536,
    metric="cosine",
    spec={"serverless": {"cloud": "aws", "region": "us-east-1"}},
    api_key=api_key,
    use_hybrid_search=True,
    hybrid_alpha=0.5,
)

knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=vector_db,
)

def pinecone_agent(user: str = "user"):
    run_id: Optional[str] = None

    agent = Agent(
        run_id=run_id,
        user_id=user,
        knowledge=knowledge_base,
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
    knowledge_base.load(recreate=True, upsert=True)

    typer.run(pinecone_agent)
```

<Card title="Async Support ⚡">
  <div className="mt-2">
    <p>
      Pinecone also supports asynchronous operations, enabling concurrency and leading to better performance.
    </p>

    ```python async_pinecone.py
    import asyncio
    from os import getenv

    from agno.agent import Agent
    from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
    from agno.vectordb.pineconedb import PineconeDb

    api_key = getenv("PINECONE_API_KEY")
    index_name = "thai-recipe-index"

    vector_db = PineconeDb(
        name=index_name,
        dimension=1536,
        metric="cosine",
        spec={"serverless": {"cloud": "aws", "region": "us-east-1"}},
        api_key=api_key,
    )

    knowledge_base = PDFUrlKnowledgeBase(
        urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
        vector_db=vector_db,
    )

    agent = Agent(
        knowledge=knowledge_base,
        # Show tool calls in the response
        show_tool_calls=True,
        # Enable the agent to search the knowledge base
        search_knowledge=True,
        # Enable the agent to read the chat history
        read_chat_history=True,
    )

    if __name__ == "__main__":
        # Comment out after first run
        asyncio.run(knowledge_base.aload(recreate=False, upsert=True))

        # Create and use the agent
        asyncio.run(agent.aprint_response("How to make Tom Kha Gai", markdown=True))
    ```

    <Tip className="mt-4">
      Use <code>aload()</code> and <code>aprint\_response()</code> methods with <code>asyncio.run()</code> for non-blocking operations in high-throughput applications.
    </Tip>
  </div>
</Card>

## PineconeDb Params

<Snippet file="vectordb_pineconedb_params.mdx" />

## Developer Resources

* View [Cookbook (Sync)](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/vector_dbs/pinecone_db/pinecone_db.py)
* View [Cookbook (Async)](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/vector_dbs/pinecone_db/async_pinecone_db.py)


