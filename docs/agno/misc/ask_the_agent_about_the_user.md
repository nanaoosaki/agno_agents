---
title: Ask the Agent about the user
category: misc
source_lines: 73632-73669
line_count: 37
---

# Ask the Agent about the user
agent.print_response("What do you know about me?")
```

## Toolkit Params

| Parameter                   | Type   | Default | Description                                                 |
| --------------------------- | ------ | ------- | ----------------------------------------------------------- |
| `session_id`                | `str`  | `None`  | Optional session ID. Auto-generated if not provided.        |
| `user_id`                   | `str`  | `None`  | Optional user ID. Auto-generated if not provided.           |
| `api_key`                   | `str`  | `None`  | Zep API key. If not provided, uses ZEP\_API\_KEY env var.   |
| `ignore_assistant_messages` | `bool` | `False` | Whether to ignore assistant messages when adding to memory. |
| `add_zep_message`           | `bool` | `True`  | Add a message to the current Zep session memory.            |
| `get_zep_memory`            | `bool` | `True`  | Retrieve memory for the current Zep session.                |
| `search_zep_memory`         | `bool` | `True`  | Search the Zep memory store for relevant information.       |
| `instructions`              | `str`  | `None`  | Custom instructions for using the Zep tools.                |
| `add_instructions`          | `bool` | `False` | Whether to add default instructions.                        |

## Toolkit Functions

| Function            | Description                                                                                                                                                                                                                                |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `add_zep_message`   | Adds a message to the current Zep session memory. Takes `role` (str) for the message sender and `content` (str) for the message text. Returns a confirmation or error message.                                                             |
| `get_zep_memory`    | Retrieves memory for the current Zep session. Takes optional `memory_type` (str) parameter with options "context" (default), "summary", or "messages". Returns the requested memory content or an error.                                   |
| `search_zep_memory` | Searches the Zep memory store for relevant information. Takes `query` (str) to find relevant facts and optional `search_scope` (str) parameter with options "messages" (default) or "summary". Returns search results or an error message. |

## Async Toolkit

The `ZepAsyncTools` class extends the `ZepTools` class and provides asynchronous versions of the toolkit functions.

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/zep.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/zep_tools.py)
* View [Async Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/zep_async_tools.py)


