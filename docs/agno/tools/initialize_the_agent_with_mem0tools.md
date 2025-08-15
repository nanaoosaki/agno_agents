---
title: Initialize the Agent with Mem0Tools
category: tools
source_lines: 73260-73282
line_count: 22
---

# Initialize the Agent with Mem0Tools
agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[Mem0Tools()],
    user_id=USER_ID,
    session_id=SESSION_ID,
    add_state_in_messages=True,
    markdown=True,
    instructions=dedent(
        """
        You have an evolving memory of this user. Proactively capture new 
        personal details, preferences, plans, and relevant context the user 
        shares, and naturally bring them up in later conversation. Before 
        answering questions about past details, recall from your memory 
        to provide precise and personalized responses. Keep your memory concise: store only meaningful 
        information that enhances long-term dialogue. If the user asks to start fresh,
        clear all remembered information and proceed anew.
        """
    ),
    show_tool_calls=True,
)

