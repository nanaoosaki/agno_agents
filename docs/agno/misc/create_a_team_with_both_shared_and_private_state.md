---
title: Create a team with both shared and private state
category: misc
source_lines: 70652-70672
line_count: 20
---

# Create a team with both shared and private state
shopping_team = Team(
    name="Shopping Team",
    mode="coordinate",
    model=OpenAIChat(id="gpt-4o-mini"),
    members=[shopping_agent],
    # Shared state - accessible by all members
    team_session_state={"shopping_list": []},
    # Team's private state - only accessible by team
    session_state={"chores": []},
    tools=[list_items, add_chore],
    instructions=[
        "You manage a shopping list.",
        "Forward add/remove requests to the Shopping List Agent.",
        "Use list_items to show the current list.",
        "Log completed tasks using add_chore.",
    ],
    show_tool_calls=True,
)

