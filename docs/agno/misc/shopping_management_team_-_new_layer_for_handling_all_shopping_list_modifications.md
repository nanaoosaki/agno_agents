---
title: Shopping management team - new layer for handling all shopping list modifications
category: misc
source_lines: 51279-51339
line_count: 60
---

# Shopping management team - new layer for handling all shopping list modifications
shopping_mgmt_team = Team(
    name="Shopping Management Team",
    team_id="shopping_management",
    mode="coordinate",
    model=OpenAIChat(id="gpt-4o-mini"),
    show_tool_calls=True,
    members=[shopping_list_agent],
    instructions=[
        "Manage adding and removing items from the shopping list using the Shopping List Agent",
        "Forward requests to add or remove items to the Shopping List Agent",
    ],
)


def get_ingredients(agent: Agent) -> str:
    """Retrieve ingredients from the shopping list to use for recipe suggestions.

    Args:
        meal_type (str): Type of meal to suggest (breakfast, lunch, dinner, snack, or any)
    """
    shopping_list = agent.team_session_state["shopping_list"]

    if not shopping_list:
        return "The shopping list is empty. Add some ingredients first to get recipe suggestions."

    # Just return the ingredients - the agent will create recipes
    return f"Available ingredients from shopping list: {', '.join(shopping_list)}"


recipe_agent = Agent(
    name="Recipe Suggester",
    agent_id="recipe_suggester",
    role="Suggest recipes based on available ingredients",
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[get_ingredients],
    instructions=[
        "First, use the get_ingredients tool to get the current ingredients from the shopping list",
        "After getting the ingredients, create detailed recipe suggestions based on those ingredients",
        "Create at least 3 different recipe ideas using the available ingredients",
        "For each recipe, include: name, ingredients needed (highlighting which ones are from the shopping list), and brief preparation steps",
        "Be creative but practical with recipe suggestions",
        "Consider common pantry items that people usually have available in addition to shopping list items",
        "Consider dietary preferences if mentioned by the user",
        "If no meal type is specified, suggest a variety of options (breakfast, lunch, dinner, snacks)",
    ],
)


def list_items(team: Team) -> str:
    """List all items in the shopping list."""
    shopping_list = team.team_session_state["shopping_list"]

    if not shopping_list:
        return "The shopping list is empty."

    items_text = "\n".join([f"- {item}" for item in shopping_list])
    return f"Current shopping list:\n{items_text}"


