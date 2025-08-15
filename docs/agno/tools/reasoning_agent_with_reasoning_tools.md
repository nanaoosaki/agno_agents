---
title: Reasoning Agent with Reasoning Tools
category: tools
source_lines: 23052-23115
line_count: 63
---

# Reasoning Agent with Reasoning Tools
Source: https://docs.agno.com/examples/concepts/reasoning/tools/reasoning-tools



This example shows how to create an agent that uses the ReasoningTools to solve
complex problems through step-by-step reasoning. The agent breaks down questions,
analyzes intermediate results, and builds structured reasoning paths to arrive at
well-justified conclusions.

## Code

```python cookbook/reasoning/tools/reasoning_tools.py


from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.reasoning import ReasoningTools

reasoning_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[ReasoningTools(add_instructions=True)],
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
        - Consider both short and long-term implications
        - Evaluate trade-offs explicitly
        
        For quantitative problems:
        - Show your calculations
        - Explain the significance of numbers
        - Consider confidence intervals when appropriate
        - Identify source data reliability
        
        For qualitative reasoning:
        - Assess how different factors interact
        - Consider psychological and social dynamics
        - Evaluate practical constraints
        - Address value considerations
        \
    """),
    add_datetime_to_instructions=True,
    stream_intermediate_steps=True,
    show_tool_calls=True,
    markdown=True,
)

