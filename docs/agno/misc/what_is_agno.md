---
title: What is Agno?
category: misc
source_lines: 59803-59839
line_count: 36
---

# What is Agno?
Source: https://docs.agno.com/introduction

Agno is a python framework for building multi-agent systems with shared memory, knowledge and reasoning.

Engineers and researchers use Agno to build:

* **Level 1:** Agents with tools and instructions ([example](/introduction/agents#level-1%3A-agents-with-tools-and-instructions)).
* **Level 2:** Agents with knowledge and storage ([example](/introduction/agents#level-2%3A-agents-with-knowledge-and-storage)).
* **Level 3:** Agents with memory and reasoning ([example](/introduction/agents#level-3%3A-agents-with-memory-and-reasoning)).
* **Level 4:** Agent Teams that can reason and collaborate ([example](/introduction/multi-agent-systems#level-4%3A-agent-teams-that-can-reason-and-collaborate)).
* **Level 5:** Agentic Workflows with state and determinism ([example](/introduction/multi-agent-systems#level-5%3A-agentic-workflows-with-state-and-determinism)).

**Example:** Level 1 Reasoning Agent that uses the YFinance API to answer questions:

```python Reasoning Finance Agent
from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.tools.reasoning import ReasoningTools
from agno.tools.yfinance import YFinanceTools

reasoning_agent = Agent(
    model=Claude(id="claude-sonnet-4-20250514"),
    tools=[
        ReasoningTools(add_instructions=True),
        YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True),
    ],
    instructions="Use tables to display data.",
    markdown=True,
)
```

<Accordion title="Watch the reasoning finance agent in action">
  <video autoPlay muted controls className="w-full aspect-video" style={{ borderRadius: "8px" }} src="https://mintlify.s3.us-west-1.amazonaws.com/agno/videos/reasoning_finance_agent.mp4" />
</Accordion>

