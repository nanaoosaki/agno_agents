---
title: Reasoning Agents
category: misc
source_lines: 66692-66858
line_count: 166
---

# Reasoning Agents
Source: https://docs.agno.com/reasoning/reasoning-agents



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

## Enabling Agentic Reasoning

To enable Agentic Reasoning, set `reasoning=True` or set the `reasoning_model` to a model that supports structured outputs. If you do not set `reasoning_model`, the primary `Agent` model will be used for reasoning.

### Reasoning Model Requirements

The `reasoning_model` must be able to handle structured outputs, this includes models like gpt-4o and claude-3-7-sonnet that support structured outputs natively or gemini models that support structured outputs using JSON mode.

### Using a Reasoning Model that supports native Reasoning

If you set `reasoning_model` to a model that supports native Reasoning like o3-mini or deepseek-r1, the reasoning model will be used to reason and the primary `Agent` model will be used to respond. See [Reasoning Models + Response Models](/reasoning/reasoning-models#reasoning-model-response-model) for more information.

## Reasoning with tools

You can also use tools with a reasoning agent. Lets create a finance agent that can reason.

```python finance_reasoning.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.yfinance import YFinanceTools

reasoning_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    instructions=["Use tables to show data"],
    show_tool_calls=True,
    markdown=True,
    reasoning=True,
)
reasoning_agent.print_response("Write a report comparing NVDA to TSLA", stream=True, show_full_reasoning=True)
```

## More Examples

### Logical puzzles

```python logical_puzzle.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat

task = (
    "Three missionaries and three cannibals need to cross a river. "
    "They have a boat that can carry up to two people at a time. "
    "If, at any time, the cannibals outnumber the missionaries on either side of the river, the cannibals will eat the missionaries. "
    "How can all six people get across the river safely? Provide a step-by-step solution and show the solutions as an ascii diagram"
)
reasoning_agent = Agent(
    model=OpenAIChat(id="gpt-4o-2024-08-06"), reasoning=True, markdown=True
)
reasoning_agent.print_response(task, stream=True, show_full_reasoning=True)
```

### Mathematical proofs

```python mathematical_proof.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat

task = "Prove that for any positive integer n, the sum of the first n odd numbers is equal to n squared. Provide a detailed proof."
reasoning_agent = Agent(
    model=OpenAIChat(id="gpt-4o-2024-08-06"), reasoning=True, markdown=True
)
reasoning_agent.print_response(task, stream=True, show_full_reasoning=True)
```

### Scientific research

```python scientific_research.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat

task = (
    "Read the following abstract of a scientific paper and provide a critical evaluation of its methodology,"
    "results, conclusions, and any potential biases or flaws:\n\n"
    "Abstract: This study examines the effect of a new teaching method on student performance in mathematics. "
    "A sample of 30 students was selected from a single school and taught using the new method over one semester. "
    "The results showed a 15% increase in test scores compared to the previous semester. "
    "The study concludes that the new teaching method is effective in improving mathematical performance among high school students."
)
reasoning_agent = Agent(
    model=OpenAIChat(id="gpt-4o-2024-08-06"), reasoning=True, markdown=True
)
reasoning_agent.print_response(task, stream=True, show_full_reasoning=True)
```

### Ethical dilemma

```python ethical_dilemma.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat

task = (
    "You are a train conductor faced with an emergency: the brakes have failed, and the train is heading towards "
    "five people tied on the track. You can divert the train onto another track, but there is one person tied there. "
    "Do you divert the train, sacrificing one to save five? Provide a well-reasoned answer considering utilitarian "
    "and deontological ethical frameworks. "
    "Provide your answer also as an ascii art diagram."
)
reasoning_agent = Agent(
    model=OpenAIChat(id="gpt-4o-2024-08-06"), reasoning=True, markdown=True
)
reasoning_agent.print_response(task, stream=True, show_full_reasoning=True)
```

### Planning an itinerary

```python planning_itinerary.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat

task = "Plan an itinerary from Los Angeles to Las Vegas"
reasoning_agent = Agent(
    model=OpenAIChat(id="gpt-4o-2024-08-06"), reasoning=True, markdown=True
)
reasoning_agent.print_response(task, stream=True, show_full_reasoning=True)
```

### Creative writing

```python creative_writing.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat

task = "Write a short story about life in 5000000 years"
reasoning_agent = Agent(
    model=OpenAIChat(id="gpt-4o-2024-08-06"), reasoning=True, markdown=True
)
reasoning_agent.print_response(task, stream=True, show_full_reasoning=True)
```

## Developer Resources

* View [Examples](/examples/concepts/reasoning/agents)
* View [Cookbook](https://github.com/agno-agi/agno/tree/main/cookbook/reasoning/agents)


