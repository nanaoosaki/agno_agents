---
title: Create an Agent that maintains state
category: misc
source_lines: 23491-23509
line_count: 18
---

# Create an Agent that maintains state
agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[add_item, remove_item, get_shopping_list],
    # Reference the in-memory database
    instructions=[
        "Current User ID: {current_user_id}",
        "Current Session ID: {current_session_id}",
    ],
    # Important: Add the state in the instructions
    add_state_in_messages=True,
    markdown=True,
)

user_id_1 = "john_doe"
user_id_2 = "mark_smith"
user_id_3 = "carmen_sandiago"

