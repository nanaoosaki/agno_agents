---
title: Team with Reasoning Tools
category: tools
source_lines: 22699-22831
line_count: 132
---

# Team with Reasoning Tools
Source: https://docs.agno.com/examples/concepts/reasoning/teams/reasoning-tool-team



This is a multi-agent team reasoning example with reasoning tools.

<Tip>
  Enabling the reasoning option on the team leader helps optimize delegation and enhances multi-agent collaboration by selectively invoking deeper reasoning when required.
</Tip>

## Code

```python cookbook/reasoning/teams/reasoning_finance_team.py
from textwrap import dedent

from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.models.openai import OpenAIChat
from agno.team.team import Team
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.reasoning import ReasoningTools
from agno.tools.yfinance import YFinanceTools

web_agent = Agent(
    name="Web Search Agent",
    role="Handle web search requests",
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[DuckDuckGoTools()],
    instructions="Always include sources",
    add_datetime_to_instructions=True,
)

finance_agent = Agent(
    name="Finance Agent",
    role="Handle financial data requests",
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)
    ],
    instructions=[
        "You are a financial data specialist. Provide concise and accurate data.",
        "Use tables to display stock prices, fundamentals (P/E, Market Cap), and recommendations.",
        "Clearly state the company name and ticker symbol.",
        "Briefly summarize recent company-specific news if available.",
        "Focus on delivering the requested financial data points clearly.",
    ],
    add_datetime_to_instructions=True,
)

team_leader = Team(
    name="Reasoning Finance Team Leader",
    mode="coordinate",
    model=Claude(id="claude-3-7-sonnet-latest"),
    members=[
        web_agent,
        finance_agent,
    ],
    tools=[ReasoningTools(add_instructions=True)],
    instructions=[
        "Only output the final answer, no other text.",
        "Use tables to display data",
    ],
    markdown=True,
    show_members_responses=True,
    enable_agentic_context=True,
    add_datetime_to_instructions=True,
    success_criteria="The team has successfully completed the task.",
)


def run_team(task: str):
    team_leader.print_response(
        task,
        stream=True,
        stream_intermediate_steps=True,
        show_full_reasoning=True,
    )


if __name__ == "__main__":
    run_team(
        dedent("""\
    Analyze the impact of recent US tariffs on market performance across these key sectors:
    - Steel & Aluminum: (X, NUE, AA)
    - Technology Hardware: (AAPL, DELL, HPQ)
    - Agricultural Products: (ADM, BG, INGR)
    - Automotive: (F, GM, TSLA)

    For each sector:
    1. Compare stock performance before and after tariff implementation
    2. Identify supply chain disruptions and cost impact percentages
    3. Analyze companies' strategic responses (reshoring, price adjustments, supplier diversification)
    4. Assess analyst outlook changes directly attributed to tariff policies
    """)
    )

   
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export OPENAI_API_KEY=xxx
    export ANTHROPIC_API_KEY=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U openai anthropic agno
    ```
  </Step>

  <Step title="Run Example">
    <CodeGroup>
      ```bash Mac
      python cookbook/reasoning/teams/reasoning_finance_team.py
      ```

      ```bash Windows
      python cookbook/reasoning/teams/reasoning_finance_team.py
      ```
    </CodeGroup>
  </Step>
</Steps>


