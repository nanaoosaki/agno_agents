---
title: Knowledge Tools
category: knowledge
source_lines: 72526-72559
line_count: 33
---

# Knowledge Tools
Source: https://docs.agno.com/tools/reasoning_tools/knowledge-tools



The `KnowledgeTools` toolkit enables Agents to search, retrieve, and analyze information from knowledge bases. This toolkit integrates with `AgentKnowledge` and provides a structured workflow for finding and evaluating relevant information before responding to users.

The toolkit implements a "Think → Search → Analyze" cycle that allows an Agent to:

1. Think through the problem and plan search queries
2. Search the knowledge base for relevant information
3. Analyze the results to determine if they are sufficient or if additional searches are needed

This approach significantly improves an Agent's ability to provide accurate information by giving it tools to find, evaluate, and synthesize knowledge.

The toolkit includes the following tools:

* `think`: A scratchpad for planning, brainstorming keywords, and refining approaches. These thoughts remain internal to the Agent and are not shown to users.
* `search`: Executes queries against the knowledge base to retrieve relevant documents.
* `analyze`: Evaluates whether the returned documents are correct and sufficient, determining if further searches are needed.

## Example

Here's an example of how to use the `KnowledgeTools` toolkit:

```python
from agno.agent import Agent
from agno.embedder.openai import OpenAIEmbedder
from agno.knowledge.url import UrlKnowledge
from agno.models.openai import OpenAIChat
from agno.tools.knowledge import KnowledgeTools
from agno.vectordb.lancedb import LanceDb, SearchType

