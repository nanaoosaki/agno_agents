---
title: Query the stored memories
category: misc
source_lines: 73287-73351
line_count: 64
---

# Query the stored memories
agent.print_response("Summarize all the details of the conversation")
```

## Toolkit Params

| Parameter    | Type   | Default | Description                                                   |
| ------------ | ------ | ------- | ------------------------------------------------------------- |
| `config`     | `dict` | `None`  | Configuration dictionary for self-hosted Mem0 instance.       |
| `api_key`    | `str`  | `None`  | Mem0 API key. If not provided, uses MEM0\_API\_KEY env var.   |
| `user_id`    | `str`  | `None`  | Default user ID for memory operations.                        |
| `org_id`     | `str`  | `None`  | Organization ID. If not provided, uses MEM0\_ORG\_ID env var. |
| `project_id` | `str`  | `None`  | Project ID. If not provided, uses MEM0\_PROJECT\_ID env var.  |
| `infer`      | `bool` | `True`  | Whether to enable automatic memory inference and extraction.  |

## Toolkit Functions

| Function              | Description                                                                                                                                              |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `add_memory`          | Adds facts to the user's memory. Supports both text strings and structured dictionaries. Returns success confirmation or error message.                  |
| `search_memory`       | Performs semantic search across the user's stored memories. Takes `query` (str) to find relevant facts. Returns list of search results or error message. |
| `get_all_memories`    | Retrieves all memories for the current user. Returns list of all stored memories.                                                                        |
| `delete_all_memories` | Deletes all memories associated with the current user. Returns success confirmation or error message.                                                    |

## Configuration Options

```python
from agno.tools.mem0 import Mem0Tools

config = {
    "vector_store": {
        "provider": "chroma",
        "config": {
            "collection_name": "test",
            "path": "db",
        }
    },
    "llm": {
        "provider": "openai",
        "config": {
            "model": "gpt-4o-mini",
            "temperature": 0.1,
            "max_tokens": 1000,
        }
    },
    "embedder": {
        "provider": "openai",
        "config": {
            "model": "text-embedding-ada-002",
        }
    }
}

mem0_tools = Mem0Tools(config=config)
```

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/mem0.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/mem0_tools.py)
* [Mem0 Documentation](https://docs.mem0.ai/)
* [Mem0 Platform](https://app.mem0.ai/dashboard/api-keys)


