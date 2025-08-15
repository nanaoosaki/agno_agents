---
title: Multi Agent Systems
category: misc
source_lines: 60281-60462
line_count: 181
---

# Multi Agent Systems
Source: https://docs.agno.com/introduction/multi-agent-systems

Teams of Agents working together towards a common goal.

## Level 4: Agent Teams that can reason and collaborate

Agents are the atomic unit of work, and work best when they have a narrow scope and a small number of tools. When the number of tools grows beyond what the model can handle or you need to handle multiple concepts, use a team of agents to spread the load.

Agno provides an industry leading multi-agent architecture that allows you to build Agent Teams that can reason, collaborate and coordinate. In this example, we'll build a team of 2 agents to analyze the semiconductor market performance, reasoning step by step.

```python level_4_team.py
from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.models.openai import OpenAIChat
from agno.team.team import Team
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.reasoning import ReasoningTools
from agno.tools.yfinance import YFinanceTools

web_agent = Agent(
    name="Web Search Agent",
    role="Handle web search requests and general research",
    model=OpenAIChat(id="gpt-4.1"),
    tools=[DuckDuckGoTools()],
    instructions="Always include sources",
    add_datetime_to_instructions=True,
)

finance_agent = Agent(
    name="Finance Agent",
    role="Handle financial data requests and market analysis",
    model=OpenAIChat(id="gpt-4.1"),
    tools=[YFinanceTools(stock_price=True, stock_fundamentals=True,analyst_recommendations=True, company_info=True)],
    instructions=[
        "Use tables to display stock prices, fundamentals (P/E, Market Cap), and recommendations.",
        "Clearly state the company name and ticker symbol.",
        "Focus on delivering actionable financial insights.",
    ],
    add_datetime_to_instructions=True,
)

reasoning_finance_team = Team(
    name="Reasoning Finance Team",
    mode="coordinate",
    model=Claude(id="claude-sonnet-4-20250514"),
    members=[web_agent, finance_agent],
    tools=[ReasoningTools(add_instructions=True)],
    instructions=[
        "Collaborate to provide comprehensive financial and investment insights",
        "Consider both fundamental analysis and market sentiment",
        "Use tables and charts to display data clearly and professionally",
        "Present findings in a structured, easy-to-follow format",
        "Only output the final consolidated analysis, not individual agent responses",
    ],
    markdown=True,
    show_members_responses=True,
    enable_agentic_context=True,
    add_datetime_to_instructions=True,
    success_criteria="The team has provided a complete financial analysis with data, visualizations, risk assessment, and actionable investment recommendations supported by quantitative analysis and market research.",
)

if __name__ == "__main__":
    reasoning_finance_team.print_response("""Compare the tech sector giants (AAPL, GOOGL, MSFT) performance:
        1. Get financial data for all three companies
        2. Analyze recent news affecting the tech sector
        3. Calculate comparative metrics and correlations
        4. Recommend portfolio allocation weights""",
        stream=True,
        show_full_reasoning=True,
        stream_intermediate_steps=True,
    )
```

Install dependencies and run the Agent team

<Steps>
  <Step title="Install dependencies">
    <CodeGroup>
      ```bash Mac
      uv pip install -U agno anthropic openai duckduckgo-search yfinance
      ```

      ```bash Windows
      uv pip install -U agno anthropic openai duckduckgo-search yfinance
      ```
    </CodeGroup>
  </Step>

  <Step title="Export your API keys">
    <CodeGroup>
      ```bash Mac
      export ANTHROPIC_API_KEY=sk-***
      export OPENAI_API_KEY=sk-***
      ```

      ```bash Windows
      setx ANTHROPIC_API_KEY sk-***
      setx OPENAI_API_KEY sk-***
      ```
    </CodeGroup>
  </Step>

  <Step title="Run the agent team">
    ```shell
    python level_4_team.py
    ```
  </Step>
</Steps>

## Level 5: Agentic Workflows with state and determinism

Workflows are deterministic, stateful, multi-agent programs built for production applications. We write the workflow in pure python, giving us extreme control over the execution flow.

Having built 100s of agentic systems, **no framework or step based approach will give you the flexibility and reliability of pure-python**. Want loops - use while/for, want conditionals - use if/else, want exceptional handling - use try/except.

<Check>
  Because the workflow logic is a python function, AI code editors can vibe code workflows for you.

  Add `https://docs.agno.com` as a document source and vibe away.
</Check>

Here's a simple workflow that caches previous outputs, you control every step: what gets cached, what gets streamed, what gets logged and what gets returned.

```python level_5_workflow.py
from typing import Iterator
from agno.agent import Agent, RunResponse
from agno.models.openai import OpenAIChat
from agno.utils.log import logger
from agno.utils.pprint import pprint_run_response
from agno.workflow import Workflow


class CacheWorkflow(Workflow):
    # Add agents or teams as attributes on the workflow
    agent = Agent(model=OpenAIChat(id="gpt-4o-mini"))

    # Write the logic in the `run()` method
    def run(self, message: str) -> Iterator[RunResponse]:
        logger.info(f"Checking cache for '{message}'")
        # Check if the output is already cached
        if self.session_state.get(message):
            logger.info(f"Cache hit for '{message}'")
            yield RunResponse(
                run_id=self.run_id, content=self.session_state.get(message)
            )
            return

        logger.info(f"Cache miss for '{message}'")
        # Run the agent and yield the response
        yield from self.agent.run(message, stream=True)

        # Cache the output after response is yielded
        self.session_state[message] = self.agent.run_response.content


if __name__ == "__main__":
    workflow = CacheWorkflow()
    # Run workflow (this is takes ~1s)
    response: Iterator[RunResponse] = workflow.run(message="Tell me a joke.")
    # Print the response
    pprint_run_response(response, markdown=True, show_time=True)
    # Run workflow again (this is immediate because of caching)
    response: Iterator[RunResponse] = workflow.run(message="Tell me a joke.")
    # Print the response
    pprint_run_response(response, markdown=True, show_time=True)
```

Run the workflow

```shell
python level_5_workflow.py
```

## Next

* Checkout the [Agent Playground](/introduction/playground) to interact with your Agents, Teams and Workflows.
* Learn how to [Monitor](/introduction/monitoring) your Agents, Teams and Workflows.
* Get help from the [Community](/introduction/community).


