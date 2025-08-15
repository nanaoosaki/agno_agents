---
title: We still provide a docstring to the tool; This will be used to populate the `user_input_schema`
category: misc
source_lines: 2800-2853
line_count: 53
---

# We still provide a docstring to the tool; This will be used to populate the `user_input_schema`
@tool(requires_user_input=True)
def send_email(to: str, subject: str, body: str) -> dict:
    """Send an email to the user.

    Args:
        to (str): The address to send the email to.
        subject (str): The subject of the email.
        body (str): The body of the email.
    """
    # Implementation here
    return f"Email sent to {to} with subject {subject} and body {body}"

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[send_email],
)

agent.run("Send an email please")
if agent.is_paused:
    for tool in agent.run_response.tools_requiring_user_input:
        input_schema: List[UserInputField] = tool.user_input_schema

        for field in input_schema:
            # Display field information to the user
            print(f"\nField: {field.name} ({field.field_type.__name__}) -> {field.description}")

            # Get user input
            user_value = input(f"Please enter a value for {field.name}: ")

            # Update the field value
            field.value = user_value

    run_response = (
        agent.continue_run()
    )
```

The `RunResponse` object has a list of tools and in the case of `requires_user_input`, the tools that require input will have `user_input_schema` populated.
This is a list of `UserInputField` objects.

```python
class UserInputField:
    name: str  # The name of the field
    field_type: Type  # The required type of the field
    description: Optional[str] = None  # The description of the field
    value: Optional[Any] = None  # The value of the field. Populated by the agent or the user.
```

You can also specify which fields should be filled by the user while the agent will provide the rest of the fields.

```python

