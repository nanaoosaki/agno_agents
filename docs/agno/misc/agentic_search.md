---
title: Agentic Search
category: misc
source_lines: 62348-62395
line_count: 47
---

# Agentic Search
Source: https://docs.agno.com/knowledge/search



Using an Agent to iteratively search for information is called **Agentic Search** and the process of **searching, reasoning and responding** is known as **Agentic RAG**.

The model interprets your query, generates relevant keywords and searches its knowledge.

<Tip>
  The Agent's response is only as good as its search. **Better search = Better responses**
</Tip>

You can use semantic search, keyword search or hybrid search. We recommend using **hybrid search with reranking** for best in class agentic search.

Because the Agent is searching for the information it needs, this pattern is called **Agentic Search** and is becoming very popular with Agent builders.

<Check>
  Let's build some examples to see Agentic Search in action.
</Check>

## Agentic RAG

When we add a knowledge base to an Agent, behind the scenes, we give the model a tool to search that knowledge base for the information it needs.

The Model generates a set of keywords and calls the `search_knowledge_base()` tool to retrieve the relevant information or few-shot examples.

Here's a working example that uses Hybrid Search + Reranking:

<Tip>
  You may remove the reranking step if you don't need it.
</Tip>

```python agentic_rag.py
"""This cookbook shows how to implement Agentic RAG using Hybrid Search and Reranking.
1. Run: `pip install agno anthropic cohere lancedb tantivy sqlalchemy` to install the dependencies
2. Export your ANTHROPIC_API_KEY and CO_API_KEY
3. Run: `python cookbook/agent_concepts/agentic_search/agentic_rag.py` to run the agent
"""

from agno.agent import Agent
from agno.embedder.cohere import CohereEmbedder
from agno.knowledge.url import UrlKnowledge
from agno.models.anthropic import Claude
from agno.reranker.cohere import CohereReranker
from agno.vectordb.lancedb import LanceDb, SearchType

