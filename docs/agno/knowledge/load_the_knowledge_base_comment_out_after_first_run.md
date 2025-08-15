---
title: Load the knowledge base: Comment out after first run
category: knowledge
source_lines: 80924-80988
line_count: 64
---

# Load the knowledge base: Comment out after first run
knowledge_base.load(recreate=True, upsert=True)

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    knowledge=knowledge_base,
    # Add a tool to read chat history.
    read_chat_history=True,
    show_tool_calls=True,
    markdown=True,
    # debug_mode=True,
)
agent.print_response("How do I make chicken and galangal in coconut milk soup", stream=True)
agent.print_response("What was my last question?", stream=True)
```

<Card title="Async Support ⚡">
  <div className="mt-2">
    <p>
      PgVector also supports asynchronous operations, enabling concurrency and leading to better performance.
    </p>

    ```python async_pgvector.py
    import asyncio

    from agno.agent import Agent
    from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
    from agno.vectordb.pgvector import PgVector

    db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

    vector_db = PgVector(table_name="recipes", db_url=db_url)

    knowledge_base = PDFUrlKnowledgeBase(
        urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
        vector_db=vector_db,
    )

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

## PgVector Params

<Snippet file="vectordb_pgvector_params.mdx" />

## Developer Resources

* View [Cookbook (Sync)](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/vector_dbs/pgvector_db/pg_vector.py)
* View [Cookbook (Async)](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/vector_dbs/pgvector_db/async_pg_vector.py)


