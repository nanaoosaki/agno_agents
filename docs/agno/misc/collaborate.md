---
title: Collaborate
category: misc
source_lines: 69271-69429
line_count: 158
---

# Collaborate
Source: https://docs.agno.com/teams/collaborate



In **Collaborate Mode**, all team members respond to the user query at once. This gives the team coordinator to review whether the team has reached a consensus on a particular topic and then synthesize the responses from all team members into a single response.

This is especially useful when used with `async await`, because it allows the individual members to respond concurrently and the coordinator to synthesize the responses asynchronously.

## How Collaborate Mode Works

In "collaborate" mode:

1. The team receives a user query
2. All team members get sent a query. When running synchronously, this happens one by one. When running asynchronously, this happens concurrently.
3. Each team member produces an output
4. The coordinator reviews the outputs and synthesizes them into a single response

<Steps>
  <Step title="Create a collaborate mode team">
    Create a file `discussion_team.py`

    ```python discussion_team.py
    import asyncio
    from textwrap import dedent

    from agno.agent import Agent
    from agno.models.openai import OpenAIChat
    from agno.team.team import Team
    from agno.tools.arxiv import ArxivTools
    from agno.tools.duckduckgo import DuckDuckGoTools
    from agno.tools.googlesearch import GoogleSearchTools
    from agno.tools.hackernews import HackerNewsTools

    reddit_researcher = Agent(
        name="Reddit Researcher",
        role="Research a topic on Reddit",
        model=OpenAIChat(id="gpt-4o"),
        tools=[DuckDuckGoTools()],
        add_name_to_instructions=True,
        instructions=dedent("""
        You are a Reddit researcher.
        You will be given a topic to research on Reddit.
        You will need to find the most relevant posts on Reddit.
        """),
    )

    hackernews_researcher = Agent(
        name="HackerNews Researcher",
        model=OpenAIChat("gpt-4o"),
        role="Research a topic on HackerNews.",
        tools=[HackerNewsTools()],
        add_name_to_instructions=True,
        instructions=dedent("""
        You are a HackerNews researcher.
        You will be given a topic to research on HackerNews.
        You will need to find the most relevant posts on HackerNews.
        """),
    )

    academic_paper_researcher = Agent(
        name="Academic Paper Researcher",
        model=OpenAIChat("gpt-4o"),
        role="Research academic papers and scholarly content",
        tools=[GoogleSearchTools(), ArxivTools()],
        add_name_to_instructions=True,
        instructions=dedent("""
        You are a academic paper researcher.
        You will be given a topic to research in academic literature.
        You will need to find relevant scholarly articles, papers, and academic discussions.
        Focus on peer-reviewed content and citations from reputable sources.
        Provide brief summaries of key findings and methodologies.
        """),
    )

    twitter_researcher = Agent(
        name="Twitter Researcher",
        model=OpenAIChat("gpt-4o"),
        role="Research trending discussions and real-time updates",
        tools=[DuckDuckGoTools()],
        add_name_to_instructions=True,
        instructions=dedent("""
        You are a Twitter/X researcher.
        You will be given a topic to research on Twitter/X.
        You will need to find trending discussions, influential voices, and real-time updates.
        Focus on verified accounts and credible sources when possible.
        Track relevant hashtags and ongoing conversations.
        """),
    )


    agent_team = Team(
        name="Discussion Team",
        mode="collaborate",
        model=OpenAIChat("gpt-4o"),
        members=[
            reddit_researcher,
            hackernews_researcher,
            academic_paper_researcher,
            twitter_researcher,
        ],
        instructions=[
            "You are a discussion master.",
            "You have to stop the discussion when you think the team has reached a consensus.",
        ],
        success_criteria="The team has reached a consensus.",
        enable_agentic_context=True,
        show_tool_calls=True,
        markdown=True,
        show_members_responses=True,
    )

    if __name__ == "__main__":
        asyncio.run(
            agent_team.print_response(
                message="Start the discussion on the topic: 'What is the best way to learn to code?'",
                stream=True,
                stream_intermediate_steps=True,
            )
        )

    ```
  </Step>

  <Step title="Run the team">
    Install libraries

    ```shell
    pip install openai duckduckgo-search arxiv pypdf googlesearch-python pycountry
    ```

    Run the team

    ```shell
    python discussion_team.py
    ```
  </Step>
</Steps>

## Defining Success Criteria

You can guide the collaborative team by specifying success criteria for the team coordinator to evaluate:

```python
strategy_team = Team(
    members=[hackernews_researcher, academic_paper_researcher, twitter_researcher],
    mode="collaborate",
    name="Research Team",
    description="A team that researches a topic",
    success_criteria="The team has reached a consensus on the topic",
)

response = strategy_team.run(
    "What is the best way to learn to code?"
)
```


