---
title: Create a Context-Aware Agent that can access real-time HackerNews data
category: advanced
source_lines: 33889-33907
line_count: 18
---

# Create a Context-Aware Agent that can access real-time HackerNews data
agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    # Each function in the context is evaluated when the agent is run,
    # think of it as dependency injection for Agents
    context={"top_hackernews_stories": get_top_hackernews_stories},
    # add_context will automatically add the context to the user message
    # add_context=True,
    # Alternatively, you can manually add the context to the instructions
    instructions=dedent("""\
        You are an insightful tech trend observer! 📰

        Here are the top stories on HackerNews:
        {top_hackernews_stories}\
    """),
    markdown=True,
)

