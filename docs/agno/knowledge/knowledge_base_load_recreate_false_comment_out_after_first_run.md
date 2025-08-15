---
title: knowledge_base.load(recreate=False)  # Comment out after first run
category: knowledge
source_lines: 80013-80099
line_count: 86
---

# knowledge_base.load(recreate=False)  # Comment out after first run

agent = Agent(
    model=MistralChat(provider="mistral-large-latest", api_key=os.getenv("MISTRAL_API_KEY")),
    knowledge=knowledge_base,
    show_tool_calls=True,
)

agent.print_response(
    "What are the health benefits of Khao Niew Dam Piek Maphrao Awn?", markdown=True, show_full_reasoning=True
)
```

<Card title="Async Support ⚡">
  <div className="mt-2">
    <p>
      Cassandra also supports asynchronous operations, enabling concurrency and leading to better performance.
    </p>

    ```python async_cassandra.py
    import asyncio

    from agno.agent import Agent
    from agno.embedder.mistral import MistralEmbedder
    from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
    from agno.models.mistral import MistralChat
    from agno.vectordb.cassandra import Cassandra

    try:
        from cassandra.cluster import Cluster  # type: ignore
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

    agent = Agent(
        model=MistralChat(),
        knowledge=knowledge_base,
        show_tool_calls=True,
    )

    if __name__ == "__main__":
        # Comment out after first run
        asyncio.run(knowledge_base.aload(recreate=False))

        # Create and use the agent
        asyncio.run(
            agent.aprint_response(
                "What are the health benefits of Khao Niew Dam Piek Maphrao Awn?",
                markdown=True,
            )
        )
    ```

    <Tip className="mt-4">
      Use <code>aload()</code> and <code>aprint\_response()</code> methods with <code>asyncio.run()</code> for non-blocking operations in high-throughput applications.
    </Tip>
  </div>
</Card>

## Developer Resources

* View [Cookbook (Sync)](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/vector_dbs/cassandra_db/cassandra_db.py)
* View [Cookbook (Async)](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/vector_dbs/cassandra_db/async_cassandra_db.py)


