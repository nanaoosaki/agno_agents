---
title: Initialize the Agent with the knowledge base and filters
category: knowledge
source_lines: 16320-16327
line_count: 7
---

# Initialize the Agent with the knowledge base and filters
agent = Agent(
    knowledge=knowledge_base,
    search_knowledge=True,
    knowledge_filters={"user_id": "jordan_mitchell"},
)

