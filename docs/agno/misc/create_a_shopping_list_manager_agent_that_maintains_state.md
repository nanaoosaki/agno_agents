---
title: Create a Shopping List Manager Agent that maintains state
category: misc
source_lines: 23640-23658
line_count: 18
---

# Create a Shopping List Manager Agent that maintains state
agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    # Initialize the session state with an empty shopping list
    session_state={"shopping_list": []},
    tools=[add_item, remove_item, list_items],
    # You can use variables from the session state in the instructions
    instructions=dedent("""\
        Your job is to manage a shopping list.

        The shopping list starts empty. You can add items, remove items by name, and list all items.

        Current shopping list: {shopping_list}
    """),
    add_state_in_messages=True,
    markdown=True,
)

