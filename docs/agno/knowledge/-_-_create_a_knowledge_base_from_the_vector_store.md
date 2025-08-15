---
title: -*- Create a knowledge base from the vector store
category: knowledge
source_lines: 61694-61717
line_count: 23
---

# -*- Create a knowledge base from the vector store
knowledge_base = LangChainKnowledgeBase(retriever=retriever)

agent = Agent(knowledge_base=knowledge_base, add_references_to_prompt=True)
conv.print_response("What did the president say about technology?")
```

## Params

| Parameter       | Type                 | Default | Description                                                               |
| --------------- | -------------------- | ------- | ------------------------------------------------------------------------- |
| `loader`        | `Optional[Callable]` | `None`  | LangChain loader.                                                         |
| `vectorstore`   | `Optional[Any]`      | `None`  | LangChain vector store used to create a retriever.                        |
| `search_kwargs` | `Optional[dict]`     | `None`  | Search kwargs when creating a retriever using the langchain vector store. |
| `retriever`     | `Optional[Any]`      | `None`  | LangChain retriever.                                                      |

`LangChainKnowledgeBase` is a subclass of the [AgentKnowledge](/reference/knowledge/base) class and has access to the same params.

## Developer Resources

* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/langchain_kb.py)


