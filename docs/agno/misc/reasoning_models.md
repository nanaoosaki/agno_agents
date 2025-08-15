---
title: Reasoning Models
category: misc
source_lines: 66858-66967
line_count: 109
---

# Reasoning Models
Source: https://docs.agno.com/reasoning/reasoning-models



Reasoning models are a new class of large language models trained with reinforcement learning to think before they answer. They produce a long internal chain of thought before responding. Examples of reasoning models include:

* OpenAI o1-pro and o3-mini
* Claude 3.7 sonnet in extended-thinking mode
* Gemini 2.0 flash thinking
* DeepSeek-R1

Reasoning models deeply consider and think through a plan before taking action. Its all about what the model does **before it starts generating a response**. Reasoning models excel at single-shot use-cases. They're perfect for solving hard problems (coding, math, physics) that don't require multiple turns, or calling tools sequentially.

## Examples

### o3-mini

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

### o3-mini with tools

```python o3_mini_with_tools.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.yfinance import YFinanceTools

agent = Agent(
    model=OpenAIChat(id="o3-mini"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    instructions="Use tables to display data.",
    show_tool_calls=True,
    markdown=True,
)
agent.print_response("Write a report comparing NVDA to TSLA", stream=True)
```

### o3-mini with reasoning effort

```python o3_mini_with_reasoning_effort.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.yfinance import YFinanceTools

agent = Agent(
    model=OpenAIChat(id="o3-mini", reasoning_effort="high"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    instructions="Use tables to display data.",
    show_tool_calls=True,
    markdown=True,
)
agent.print_response("Write a report comparing NVDA to TSLA", stream=True)
```

### DeepSeek-R1 using Groq

```python deepseek_r1_using_groq.py
from agno.agent import Agent
from agno.models.groq import Groq

agent = Agent(
    model=Groq(
        id="deepseek-r1-distill-llama-70b", temperature=0.6, max_tokens=1024, top_p=0.95
    ),
    markdown=True,
)
agent.print_response("9.11 and 9.9 -- which is bigger?", stream=True)
```

## Reasoning Model + Response Model

When you run the DeepSeek-R1 Agent above, you'll notice that the response is not that great. This is because DeepSeek-R1 is great at solving problems but not that great at responding in a natural way (like claude sonnet or gpt-4.5).

What if we wanted to use a Reasoning Model to reason but a different model to generate the response?

Great news! Agno allows you to use a Reasoning Model and a different Response Model together. By using a separate model for reasoning and a different model for responding, we can have the best of both worlds.

### DeepSeek-R1 + Claude Sonnet

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

## Developer Resources

* View [Examples](/examples/concepts/reasoning/models)
* View [Cookbook](https://github.com/agno-agi/agno/tree/main/cookbook/reasoning/models)


