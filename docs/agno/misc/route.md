---
title: Route
category: misc
source_lines: 70131-70333
line_count: 202
---

# Route
Source: https://docs.agno.com/teams/route



In **Route Mode**, the Team Leader directs user queries to the most appropriate team member based on the content of the request.

The Team Leader acts as a smart router, analyzing the query and selecting the best-suited agent to handle it. The member's response is then returned directly to the user.

## How Route Mode Works

In "route" mode:

1. The team receives a user query
2. A Team Leader analyzes the query to determine which team member has the right expertise
3. The query is forwarded to the selected team member
4. The response from the team member is returned directly to the user

This mode is particularly useful when you have specialized agents with distinct expertise areas and want to automatically direct queries to the right specialist.

<Steps>
  <Step title="Create Multi Language Team">
    Create a file `multi_language_team.py`

    ```python multi_language_team.py
    from agno.agent import Agent
    from agno.models.anthropic import Claude
    from agno.models.deepseek import DeepSeek
    from agno.models.mistral.mistral import MistralChat
    from agno.models.openai import OpenAIChat
    from agno.team.team import Team

    english_agent = Agent(
        name="English Agent",
        role="You can only answer in English",
        model=OpenAIChat(id="gpt-4.5-preview"),
        instructions=[
            "You must only respond in English",
        ],
    )

    japanese_agent = Agent(
        name="Japanese Agent",
        role="You can only answer in Japanese",
        model=DeepSeek(id="deepseek-chat"),
        instructions=[
            "You must only respond in Japanese",
        ],
    )
    chinese_agent = Agent(
        name="Chinese Agent",
        role="You can only answer in Chinese",
        model=DeepSeek(id="deepseek-chat"),
        instructions=[
            "You must only respond in Chinese",
        ],
    )
    spanish_agent = Agent(
        name="Spanish Agent",
        role="You can only answer in Spanish",
        model=OpenAIChat(id="gpt-4.5-preview"),
        instructions=[
            "You must only respond in Spanish",
        ],
    )

    french_agent = Agent(
        name="French Agent",
        role="You can only answer in French",
        model=MistralChat(id="mistral-large-latest"),
        instructions=[
            "You must only respond in French",
        ],
    )

    german_agent = Agent(
        name="German Agent",
        role="You can only answer in German",
        model=Claude("claude-3-5-sonnet-20241022"),
        instructions=[
            "You must only respond in German",
        ],
    )
    multi_language_team = Team(
        name="Multi Language Team",
        mode="route",
        model=OpenAIChat("gpt-4.5-preview"),
        members=[
            english_agent,
            spanish_agent,
            japanese_agent,
            french_agent,
            german_agent,
            chinese_agent,
        ],
        show_tool_calls=True,
        markdown=True,
        instructions=[
            "You are a language router that directs questions to the appropriate language agent.",
            "If the user asks in a language whose agent is not a team member, respond in English with:",
            "'I can only answer in the following languages: English, Spanish, Japanese, French and German. Please ask your question in one of these languages.'",
            "Always check the language of the user's input before routing to an agent.",
            "For unsupported languages like Italian, respond in English with the above message.",
        ],
        show_members_responses=True,
    )


    # Ask "How are you?" in all supported languages
    multi_language_team.print_response(
        "How are you?", stream=True  # English
    )

    multi_language_team.print_response(
        "你好吗？", stream=True  # Chinese
    )

    multi_language_team.print_response(
        "お元気ですか?", stream=True  # Japanese
    )

    multi_language_team.print_response(
        "Comment allez-vous?",
        stream=True,  # French
    )
    ```
  </Step>

  <Step title="Run the team">
    Install libraries

    ```shell
    pip install openai mistral agno
    ```

    Run the team

    ```shell
    python multi_language_team.py
    ```
  </Step>
</Steps>

## Structured Output with Route Mode

One powerful feature of route mode is its ability to maintain structured output from member agents.
When using a Pydantic model for the response, the response from the selected team member will be automatically parsed into the specified structure.

### Defining Structured Output Models

```python
from pydantic import BaseModel
from typing import List, Optional
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.team import Team


class StockAnalysis(BaseModel):
    symbol: str
    company_name: str
    analysis: str

class CompanyAnalysis(BaseModel):
    company_name: str
    analysis: str

stock_searcher = Agent(
    name="Stock Searcher",
    model=OpenAIChat("gpt-4o"),
    response_model=StockAnalysis,
    role="Searches for information on stocks and provides price analysis.",
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
        )
    ],
)

company_info_agent = Agent(
    name="Company Info Searcher",
    model=OpenAIChat("gpt-4o"),
    role="Searches for information about companies and recent news.",
    response_model=CompanyAnalysis,
    tools=[
        YFinanceTools(
            stock_price=False,
            company_info=True,
            company_news=True,
        )
    ],
)

team = Team(
    name="Stock Research Team",
    mode="route",
    model=OpenAIChat("gpt-4o"),
    members=[stock_searcher, company_info_agent],
    markdown=True,
)

