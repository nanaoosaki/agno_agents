---
title: Try the meal planning feature
category: misc
source_lines: 51429-51469
line_count: 40
---

# Try the meal planning feature
shopping_team.print_response("What can I make with these ingredients?", stream=True)
print(f"Session state: {shopping_team.team_session_state}")

shopping_team.print_response(
    "Clear everything from my list and start over with just bananas and yogurt",
    stream=True,
)
print(f"Shared Session state: {shopping_team.team_session_state}")


print(f"Team session state: {shopping_team.session_state}")

```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Install required libraries">
    ```bash
    pip install openai
    ```
  </Step>

  <Step title="Set environment variables">
    ```bash
    export OPENAI_API_KEY=****
    ```
  </Step>

  <Step title="Run the agent">
    ```bash
    python cookbook/teams/team_with_nested_shared_state.py
    ```
  </Step>
</Steps>


