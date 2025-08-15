---
title: Team with Knowledge Tools
category: knowledge
source_lines: 22569-22699
line_count: 130
---

# Team with Knowledge Tools
Source: https://docs.agno.com/examples/concepts/reasoning/teams/knowledge-tool-team



This is a team reasoning example with knowledge tools.

<Tip>
  Enabling the reasoning option on the team leader helps optimize delegation and enhances multi-agent collaboration by selectively invoking deeper reasoning when required.
</Tip>

## Code

```python cookbook/reasoning/teams/knowledge_tool_team.py
from textwrap import dedent

from agno.agent import Agent
from agno.knowledge.url import UrlKnowledge
from agno.models.openai import OpenAIChat
from agno.team.team import Team
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.knowledge import KnowledgeTools
from agno.tools.yfinance import YFinanceTools
from agno.vectordb.lancedb import LanceDb, SearchType

agno_docs = UrlKnowledge(
    urls=["https://www.paulgraham.com/read.html"],
    # Use LanceDB as the vector database and store embeddings in the `agno_docs` table
    vector_db=LanceDb(
        uri="tmp/lancedb",
        table_name="agno_docs",
        search_type=SearchType.hybrid,
    ),
)

knowledge_tools = KnowledgeTools(
    knowledge=agno_docs,
    think=True,
    search=True,
    analyze=True,
    add_few_shot=True,
)

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
    add_datetime_to_instructions=True,
)

team_leader = Team(
    name="Reasoning Finance Team",
    mode="coordinate",
    model=OpenAIChat(id="gpt-4o"),
    members=[
        web_agent,
        finance_agent,
    ],
    tools=[knowledge_tools],
    instructions=[
        "Only output the final answer, no other text.",
        "Use tables to display data",
    ],
    markdown=True,
    show_members_responses=True,
    enable_agentic_context=True,
    add_datetime_to_instructions=True,
    success_criteria="The team has successfully completed the task.",
    debug_mode=True,
)


def run_team(task: str):
    # Comment out after first run
    agno_docs.load(recreate=True)
    team_leader.print_response(
        task,
        stream=True,
        stream_intermediate_steps=True,
        show_full_reasoning=True,
    )


if __name__ == "__main__":
    run_team("What does Paul Graham talk about the need to read in this essay?")
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export OPENAI_API_KEY=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U openai agno
    ```
  </Step>

  <Step title="Run Example">
    <CodeGroup>
      ```bash Mac
      python cookbook/reasoning/teams/knowledge_tool_team.py
      ```

      ```bash Windows
      python cookbook/reasoning/teams/knowledge_tool_team.py
      ```
    </CodeGroup>
  </Step>
</Steps>


