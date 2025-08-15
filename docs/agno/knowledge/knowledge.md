---
title: Knowledge
category: knowledge
source_lines: 470-492
line_count: 22
---

# Knowledge
Source: https://docs.agno.com/agents/knowledge



**Knowledge** is domain-specific information that the Agent can **search** at runtime to make better decisions (dynamic few-shot learning) and provide accurate responses (agentic RAG). Knowledge is stored in a vector db and this **searching on demand** pattern is called Agentic RAG.

<Accordion title="Dynamic Few-Shot Learning: Text2Sql Agent" icon="database">
  Example: If we're building a Text2Sql Agent, we'll need to give the table schemas, column names, data types, example queries, common "gotchas" to help it generate the best-possible SQL query.

  We're obviously not going to put this all in the system prompt, instead we store this information in a vector database and let the Agent query it at runtime.

  Using this information, the Agent can then generate the best-possible SQL query. This is called dynamic few-shot learning.
</Accordion>

**Agno Agents use Agentic RAG** by default, meaning when we provide `knowledge` to an Agent, it will search this knowledge base, at runtime, for the specific information it needs to achieve its task.

The pseudo steps for adding knowledge to an Agent are:

```python
from agno.agent import Agent, AgentKnowledge

