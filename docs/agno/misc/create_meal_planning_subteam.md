---
title: Create meal planning subteam
category: misc
source_lines: 51339-51414
line_count: 75
---

# Create meal planning subteam
meal_planning_team = Team(
    name="Meal Planning Team",
    team_id="meal_planning",
    mode="coordinate",
    model=OpenAIChat(id="gpt-4o-mini"),
    members=[recipe_agent],
    instructions=[
        "You are a meal planning team that suggests recipes based on shopping list items.",
        "IMPORTANT: When users ask 'What can I make with these ingredients?' or any recipe-related questions, IMMEDIATELY forward the EXACT SAME request to the recipe_agent WITHOUT asking for further information.",
        "DO NOT ask the user for ingredients - the recipe_agent will work with what's already in the shopping list.",
        "Your primary job is to forward recipe requests directly to the recipe_agent without modification.",
    ],
)


def add_chore(team: Team, chore: str, priority: str = "medium") -> str:
    """Add a chore to the list with priority level.

    Args:
        chore (str): The chore to add to the list
        priority (str): Priority level of the chore (low, medium, high)

    Returns:
        str: Confirmation message
    """
    # Initialize chores list if it doesn't exist
    if "chores" not in team.session_state:
        team.session_state["chores"] = []

    # Validate priority
    valid_priorities = ["low", "medium", "high"]
    if priority.lower() not in valid_priorities:
        priority = "medium"  # Default to medium if invalid

    # Add the chore with timestamp and priority
    from datetime import datetime

    chore_entry = {
        "description": chore,
        "priority": priority.lower(),
        "added_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }

    team.session_state["chores"].append(chore_entry)

    return f"Added chore: '{chore}' with {priority} priority"


shopping_team = Team(
    name="Shopping List Team",
    mode="coordinate",
    model=OpenAIChat(id="gpt-4o-mini"),
    team_session_state={"shopping_list": []},
    tools=[list_items, add_chore],
    session_state={"chores": []},
    team_id="shopping_list_team",
    members=[
        shopping_mgmt_team,
        meal_planning_team,
    ],
    show_tool_calls=True,
    markdown=True,
    instructions=[
        "You are a team that manages a shopping list & helps plan meals using that list.",
        "If you need to add or remove items from the shopping list, forward the full request to the Shopping Management Team.",
        "IMPORTANT: If the user asks about recipes or what they can make with ingredients, IMMEDIATELY forward the EXACT request to the meal_planning_team with NO additional questions.",
        "Example: When user asks 'What can I make with these ingredients?', you should simply forward this exact request to meal_planning_team without asking for more information.",
        "If you need to list the items in the shopping list, use the list_items tool.",
        "If the user got something from the shopping list, it means it can be removed from the shopping list.",
        "After each completed task, use the add_chore tool to log exactly what was done with high priority.",
    ],
    show_members_responses=True,
)

