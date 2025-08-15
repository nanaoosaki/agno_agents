---
title: Use the agent to ask a question and print a response.
category: misc
source_lines: 61850-61868
line_count: 18
---

# Use the agent to ask a question and print a response.
agent.print_response("Explain what this text means: low end eats the high end", markdown=True)
```

## Params

| Parameter   | Type                 | Default | Description                                                           |
| ----------- | -------------------- | ------- | --------------------------------------------------------------------- |
| `retriever` | `BaseRetriever`      | `None`  | LlamaIndex retriever used for querying the knowledge base.            |
| `loader`    | `Optional[Callable]` | `None`  | Optional callable function to load documents into the knowledge base. |

`LlamaIndexKnowledgeBase` is a subclass of the [AgentKnowledge](/reference/knowledge/base) class and has access to the same params.

## Developer Resources

* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/llamaindex_kb.py)


