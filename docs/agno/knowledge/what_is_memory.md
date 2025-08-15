---
title: What is Memory?
category: knowledge
source_lines: 62869-62891
line_count: 22
---

# What is Memory?
Source: https://docs.agno.com/memory/introduction

Memory gives an Agent the ability to recall relevant information.

Memory is a part of the Agent's context that helps it provide the best, most personalized response.

<Check>
  If the user tells the Agent they like to ski, then future responses can reference this information to provide a more personalized experience.
</Check>

1. **Session Storage (chat history and session state):** Session storage saves an Agent's sessions in a database and enables Agents to have multi-turn conversations. Session storage also holds the session state, which is persisted across runs because it is saved to the database after each run. Session storage is a form of short-term memory **called "Storage" in Agno**.

2. **User Memories (user preferences):** The Agent can store insights and facts about the user that it learns through conversation. This helps the agents personalize its response to the user it is interacting with. Think of this as adding "ChatGPT like memory" to your agent. **This is called "Memory" in Agno**.

3. **Session Summaries (chat summary):** The Agent can store a condensed representations of the session, useful when chat histories gets too long. **This is called "Summary" in Agno**.

<Note>
  If you haven't, we also recommend reading the Memory section of the [Agents](/agents/memory) to get familiar with the basics.
</Note>


