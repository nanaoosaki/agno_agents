---
title: Create an agent with the knowledge base and the retriever
category: knowledge
source_lines: 61753-61786
line_count: 33
---

# Create an agent with the knowledge base and the retriever
agent = Agent(
    model=Claude(id="claude-3-7-sonnet-latest"),
    # Agentic RAG is enabled by default when `knowledge` is provided to the Agent.
    knowledge=knowledge_base,
    retriever=lightrag_retriever,
    # search_knowledge=True gives the Agent the ability to search on demand
    # search_knowledge is True by default
    search_knowledge=True,
    instructions=[
        "Include sources in your response.",
        "Always search your knowledge before answering the question.",
        "Use the async_search method to search the knowledge base.",
    ],
    markdown=True,
)

asyncio.run(agent.aprint_response("What are Agno Agents?"))
```

## Params

| Parameter             | Type               | Default | Description                                                          |
| --------------------- | ------------------ | ------- | -------------------------------------------------------------------- |
| `lightrag_server_url` | `str`              | -       | URL to LightRAG server.                                              |
| `path`                | `Union[str, Path]` | -       | Path to documents. Can point to a single file or directory of files. |
| `url`                 | `str`              | -       | URLs of the website to read.                                         |

## Developer Resources

* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/agentic_search/lightrag)


