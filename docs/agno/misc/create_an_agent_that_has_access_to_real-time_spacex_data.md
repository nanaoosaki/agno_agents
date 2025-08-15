---
title: Create an Agent that has access to real-time SpaceX data
category: misc
source_lines: 11641-11689
line_count: 48
---

# Create an Agent that has access to real-time SpaceX data
agent = Agent(
    model=OpenAIChat(id="gpt-4.1"),
    # Each function in the context is evaluated at runtime
    context={"upcoming_spacex_launches": get_upcoming_spacex_launches},
    description=dedent("""\
        You are a cosmic analyst and spaceflight enthusiast. 🚀

        Here are the next SpaceX launches:
        {upcoming_spacex_launches}\
    """),
    # add_state_in_messages will make the `upcoming_spacex_launches` variable
    # available in the description and instructions
    add_state_in_messages=True,
    markdown=True,
)

agent.print_response(
    "Tell me about the upcoming SpaceX missions.",
    stream=True,
)
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Install libraries">
    ```bash
    pip install -U agno httpx
    ```
  </Step>

  <Step title="Run Example">
    <CodeGroup>
      ```bash Mac
      python cookbook/agent_concepts/context/03-context_in_instructions.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/context/03-context_in_instructions.py
      ```
    </CodeGroup>
  </Step>
</Steps>


