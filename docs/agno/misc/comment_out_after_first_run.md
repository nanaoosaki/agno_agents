---
title: Comment out after first run
category: misc
source_lines: 80256-80317
line_count: 61
---

# Comment out after first run
agent.knowledge.load(recreate=False)  # type: ignore

agent.print_response("How do I make pad thai?", markdown=True)
agent.print_response("What was my last question?", stream=True)
```

<Card title="Async Support ⚡">
  <div className="mt-2">
    <p>
      Clickhouse also supports asynchronous operations, enabling concurrency and leading to better performance.
    </p>

    ```python async_clickhouse.py
    import asyncio

    from agno.agent import Agent
    from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
    from agno.storage.agent.sqlite import SqliteAgentStorage
    from agno.vectordb.clickhouse import Clickhouse

    agent = Agent(
        storage=SqliteAgentStorage(table_name="recipe_agent"),
        knowledge=PDFUrlKnowledgeBase(
            urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
            vector_db=Clickhouse(
                table_name="recipe_documents",
                host="localhost",
                port=8123,
                username="ai",
                password="ai",
            ),
        ),
        # Show tool calls in the response
        show_tool_calls=True,
        # Enable the agent to search the knowledge base
        search_knowledge=True,
        # Enable the agent to read the chat history
        read_chat_history=True,
    )

    if __name__ == "__main__":
        # Comment out after first run
        asyncio.run(agent.knowledge.aload(recreate=False))

        # Create and use the agent
        asyncio.run(agent.aprint_response("How to make Tom Kha Gai", markdown=True))
    ```

    <Tip className="mt-4">
      Use <code>aload()</code> and <code>aprint\_response()</code> methods with <code>asyncio.run()</code> for non-blocking operations in high-throughput applications.
    </Tip>
  </div>
</Card>

## Developer Resources

* View [Cookbook (Sync)](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/vector_dbs/clickhouse_db/clickhouse.py)
* View [Cookbook (Async)](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/vector_dbs/clickhouse_db/async_clickhouse.py)


