---
title: What is Reasoning?
category: misc
source_lines: 66563-66692
line_count: 129
---

# What is Reasoning?
Source: https://docs.agno.com/reasoning/introduction

Reasoning gives Agents the ability to "think" before responding and "analyze" the results of their actions (i.e. tool calls), greatly improving the Agents' ability to solve problems that require sequential tool calls.

Reasoning Agents go through an internal chain of thought before responding, working through different ideas, validating and correcting as needed. Agno supports 3 approaches to reasoning:

1. [Reasoning Models](#reasoning-models)
2. [Reasoning Tools](#reasoning-tools)
3. [Reasoning Agents](#reasoning-agents)

Which approach works best will depend on your use case, we recommend trying them all and immersing yourself in this new era of Reasoning Agents.

## Reasoning Models

Reasoning models are a separate class of large language models trained with reinforcement learning to think before they answer. They produce an internal chain of thought before responding. Examples of reasoning models include OpenAI o-series, Claude 3.7 sonnet in extended-thinking mode, Gemini 2.0 flash thinking and DeepSeek-R1.

Reasoning at the model layer is all about what the model does **before it starts generating a response**. Reasoning models excel at single-shot use-cases. They're perfect for solving hard problems (coding, math, physics) that don't require multiple turns, or calling tools sequentially.

### Example

```python o3_mini.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat

agent = Agent(model=OpenAIChat(id="o3-mini"))
agent.print_response(
    "Solve the trolley problem. Evaluate multiple ethical frameworks. "
    "Include an ASCII diagram of your solution.",
    stream=True,
)
```

Read more about reasoning models in the [Reasoning Models Guide](/reasoning/reasoning-models).

## Reasoning Model + Response Model

What if we wanted to use a Reasoning Model to reason but a different model to generate the response? It is well known that reasoning models are great at solving problems but not that great at responding in a natural way (like claude sonnet or gpt-4o).

By using a separate model for reasoning and a different model for responding, we can have the best of both worlds.

### Example

Let's use deepseek-r1 from Groq for reasoning and claude sonnet for a natural response.

```python deepseek_plus_claude.py
from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.models.groq import Groq

deepseek_plus_claude = Agent(
    model=Claude(id="claude-3-7-sonnet-20250219"),
    reasoning_model=Groq(
        id="deepseek-r1-distill-llama-70b", temperature=0.6, max_tokens=1024, top_p=0.95
    ),
)
deepseek_plus_claude.print_response("9.11 and 9.9 -- which is bigger?", stream=True)
```

## Reasoning Tools

By giving a model a **"think" tool**, we can greatly improve its reasoning capabilities by providing a dedicated space for structured thinking. This is a simple, yet effective approach to add reasoning to non-reasoning models.

The research was first published by Anthropic in [this blog post](https://www.anthropic.com/engineering/claude-think-tool) but has been practiced by many AI Engineers (including our own team) long before it was published.

### Example

```python claude_thinking_tools.py
from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.tools.thinking import ThinkingTools
from agno.tools.yfinance import YFinanceTools

reasoning_agent = Agent(
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
    markdown=True,
)

if __name__ == "__main__":
    reasoning_agent.print_response(
        "Write a report on NVDA. Only the report, no other text.",
        stream=True,
        show_full_reasoning=True,
        stream_intermediate_steps=True,
    )
```

Read more about reasoning tools in the [Reasoning Tools Guide](/reasoning/reasoning-tools).

## Reasoning Agents

Reasoning Agents are a new type of multi-agent system developed by Agno that combines chain of thought reasoning with tool use.

You can enable reasoning on any Agent by setting `reasoning=True`.

When an Agent with `reasoning=True` is given a task, a separate "Reasoning Agent" first solves the problem using chain-of-thought. At each step, it calls tools to gather information, validate results, and iterate until it reaches a final answer. Once the Reasoning Agent has a final answer, it hands the results back to the original Agent to validate and provide a response.

### Example

```python reasoning_agent.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat

reasoning_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    reasoning=True,
    markdown=True,
)
reasoning_agent.print_response(
    "Solve the trolley problem. Evaluate multiple ethical frameworks. "
    "Include an ASCII diagram of your solution.",
    stream=True,
    show_full_reasoning=True,
)
```

Read more about reasoning agents in the [Reasoning Agents Guide](/reasoning/reasoning-agents).


