---
title: Initialize the Agent with the knowledge_base
category: knowledge
source_lines: 61620-61653
line_count: 33
---

# Initialize the Agent with the knowledge_base
agent = Agent(
    knowledge=knowledge_base,
    search_knowledge=True,
)

if __name__ == "__main__":
    # Comment out after first run
    asyncio.run(knowledge_base.aload(recreate=False))

    # Create and use the agent
    asyncio.run(
        agent.aprint_response(
            "Ask anything from the json knowledge base", markdown=True
        )
    )
```

## Params

| Parameter | Type               | Default        | Description                                                                              |
| --------- | ------------------ | -------------- | ---------------------------------------------------------------------------------------- |
| `path`    | `Union[str, Path]` | -              | Path to `JSON` files.<br />Can point to a single JSON file or a directory of JSON files. |
| `reader`  | `JSONReader`       | `JSONReader()` | A `JSONReader` that converts the `JSON` files into `Documents` for the vector database.  |

`JSONKnowledgeBase` is a subclass of the [AgentKnowledge](/reference/knowledge/base) class and has access to the same params.

## Developer Resources

* View [Sync loading Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/json_kb.py)
* View [Async loading Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/json_kb_async.py)


