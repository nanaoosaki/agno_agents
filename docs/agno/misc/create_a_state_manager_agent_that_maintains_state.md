---
title: Create a State Manager Agent that maintains state
category: misc
source_lines: 34092-34119
line_count: 27
---

# Create a State Manager Agent that maintains state
agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    # Initialize the session state with a counter starting at 0
    session_state={"count": 0},
    tools=[increment_counter],
    # You can use variables from the session state in the instructions
    instructions=dedent("""\
        You are the State Manager, an enthusiastic guide to state management! 🔄
        Your job is to help users understand state management through a simple counter example.

        Follow these guidelines for every interaction:
        1. Always acknowledge the current state (count) when relevant
        2. Use the increment_counter tool to modify the state
        3. Explain state changes in a clear and engaging way

        Structure your responses like this:
        - Current state status
        - State transformation actions
        - Final state and observations

        Starting state (count) is: {count}\
    """),
    show_tool_calls=True,
    markdown=True,
)

