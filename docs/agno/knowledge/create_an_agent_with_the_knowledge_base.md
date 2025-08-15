---
title: Create an agent with the knowledge base
category: knowledge
source_lines: 62674-62702
line_count: 28
---

# Create an agent with the knowledge base
agent = Agent(knowledge=knowledge_base, search_knowledge=True, debug_mode=True)

if __name__ == "__main__":
    # Comment out after first run
    asyncio.run(knowledge_base.aload(recreate=False))

    # Create and use the agent
    asyncio.run(agent.aprint_response("How does agno work?", markdown=True))
```

## Params

| Parameter   | Type                      | Default | Description                                                                                       |
| ----------- | ------------------------- | ------- | ------------------------------------------------------------------------------------------------- |
| `urls`      | `List[str]`               | `[]`    | URLs to read                                                                                      |
| `reader`    | `Optional[WebsiteReader]` | `None`  | A `WebsiteReader` that reads the urls and converts them into `Documents` for the vector database. |
| `max_depth` | `int`                     | `3`     | Maximum depth to crawl.                                                                           |
| `max_links` | `int`                     | `10`    | Number of links to crawl.                                                                         |

`WebsiteKnowledgeBase` is a subclass of the [AgentKnowledge](/reference/knowledge/base) class and has access to the same params.

## Developer Resources

* View [Sync loading Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/website_kb.py)
* View [Async loading Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/website_kb_async.py)


