---
title: Knowledge Base
category: knowledge
source_lines: 80604-80691
line_count: 87
---

# Knowledge Base
knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=vector_db,
)

def lancedb_agent(user: str = "user"):
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
    knowledge_base.load(recreate=True)

    typer.run(lancedb_agent)
```

<Card title="Async Support ⚡">
  <div className="mt-2">
    <p>
      LanceDB also supports asynchronous operations, enabling concurrency and leading to better performance.
    </p>

    ```python async_lance_db.py
    # install lancedb - `pip install lancedb`
    import asyncio

    from agno.agent import Agent
    from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
    from agno.vectordb.lancedb import LanceDb

    # Initialize LanceDB
    vector_db = LanceDb(
        table_name="recipes",
        uri="tmp/lancedb",  # You can change this path to store data elsewhere
    )

    # Create knowledge base
    knowledge_base = PDFUrlKnowledgeBase(
        urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
        vector_db=vector_db,
    )
    agent = Agent(knowledge=knowledge_base, show_tool_calls=True, debug_mode=True)

    if __name__ == "__main__":
        # Load knowledge base asynchronously
        asyncio.run(knowledge_base.aload(recreate=False))  # Comment out after first run

        # Create and use the agent asynchronously
        asyncio.run(agent.aprint_response("How to make Tom Kha Gai", markdown=True))
    ```

    <Tip className="mt-4">
      Use <code>aload()</code> and <code>aprint\_response()</code> methods with <code>asyncio.run()</code> for non-blocking operations in high-throughput applications.
    </Tip>
  </div>
</Card>

## LanceDb Params

<Snippet file="vectordb_lancedb_params.mdx" />

## Developer Resources

* View [Cookbook (Sync)](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/vector_dbs/lance_db/lance_db.py)
* View [Cookbook (Async)](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/vector_dbs/lance_db/async_lance_db.py)


