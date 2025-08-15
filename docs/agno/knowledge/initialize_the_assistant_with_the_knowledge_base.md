---
title: Initialize the Assistant with the knowledge_base
category: knowledge
source_lines: 62562-62595
line_count: 33
---

# Initialize the Assistant with the knowledge_base
agent = Agent(
    knowledge=knowledge_base,
    search_knowledge=True,
)

if __name__ == "__main__":
    # Comment out after first run
    asyncio.run(knowledge_base.aload(recreate=False))

    asyncio.run(
        agent.aprint_response(
            "What knowledge is available in my knowledge base?", markdown=True
        )
    )
```

## Params

| Parameter | Type               | Default        | Description                                                                           |
| --------- | ------------------ | -------------- | ------------------------------------------------------------------------------------- |
| `path`    | `Union[str, Path]` | -              | Path to text files. Can point to a single text file or a directory of text files.     |
| `formats` | `List[str]`        | `[".txt"]`     | Formats accepted by this knowledge base.                                              |
| `reader`  | `TextReader`       | `TextReader()` | A `TextReader` that converts the text files into `Documents` for the vector database. |

`TextKnowledgeBase` is a subclass of the [AgentKnowledge](/reference/knowledge/base) class and has access to the same params.

## Developer Resources

* View [Sync loading Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/text_kb.py)
* View [Async loading Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/text_kb_async.py)


