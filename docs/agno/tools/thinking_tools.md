---
title: Thinking Tools
category: tools
source_lines: 72743-72856
line_count: 113
---

# Thinking Tools
Source: https://docs.agno.com/tools/reasoning_tools/thinking-tools



The `ThinkingTools` toolkit provides Agents with a dedicated space for reflection during execution. This toolkit enables an Agent to use a scratchpad for thinking through problems, listing rules, checking information, verifying compliance, and evaluating results before taking actions.

Unlike approaches that have agents immediately respond or take action, this toolkit encourages thoughtful consideration by giving the Agent space to "think" about its actions, examine its own responses, and maintain a log of its thought process throughout the conversation.

The toolkit includes the following tool:

* `think`: This tool serves as a scratchpad for the Agent to reason through problems, list applicable rules, verify collected information, and evaluate planned actions for compliance and correctness.

## Example

Here's an example of how to use the `ThinkingTools` toolkit:

```python
from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.tools.thinking import ThinkingTools
from agno.tools.yfinance import YFinanceTools

thinking_agent = Agent(
    model=Claude(id="claude-3-7-sonnet-latest"),
    tools=[
        ThinkingTools(add_instructions=True),
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            company_info=True,
            company_news=True,
        ),
    ],
    instructions="Use tables where possible",
    show_tool_calls=True,
    markdown=True,
)

thinking_agent.print_response("Write a report comparing NVDA to TSLA", stream=True)
```

The toolkit comes with default instructions to help the Agent use the tool effectively. Here is how you can enable them:

```python
thinking_agent = Agent(
    model=Claude(id="claude-3-7-sonnet-latest"),
    tools=[
        ThinkingTools(
            think=True,
            add_instructions=True,
        ),
    ],
)
```

`ThinkingTools` can be used with any model provider that supports function calling. Here is an example with of a thinking Agent using `OpenAIChat`:

```python
from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.thinking import ThinkingTools

thinking_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[ThinkingTools(add_instructions=True)],
    instructions=dedent("""\
        You are an expert problem-solving assistant with strong analytical skills! 🧠

        Your approach to problems:
        1. First, break down complex questions into component parts
        2. Clearly state your assumptions
        3. Develop a structured reasoning path
        4. Consider multiple perspectives
        5. Evaluate evidence and counter-arguments
        6. Draw well-justified conclusions

        When solving problems:
        - Use explicit step-by-step reasoning
        - Identify key variables and constraints
        - Explore alternative scenarios
        - Highlight areas of uncertainty
        - Explain your thought process clearly
        \
    """),
    add_datetime_to_instructions=True,
    stream_intermediate_steps=True,
    show_tool_calls=True,
    markdown=True,
)
```

This Agent can be used to address complex problems where careful consideration is needed:

```python
thinking_agent.print_response(
    "We need to implement a new content moderation policy for our platform. "
    stream=True
)
```

or,

```python
thinking_agent.print_response(
    "Our company is developing a new AI product. We need to consider ethical implications "
    stream=True,
)
```


