---
title: Coordinate
category: misc
source_lines: 69429-69545
line_count: 116
---

# Coordinate
Source: https://docs.agno.com/teams/coordinate



In **Coordinate Mode**, the Team Leader delegates tasks to team members and synthesizes their outputs into a cohesive response.

## How Coordinate Mode Works

In "coordinate" mode:

1. The team receives a user query
2. A Team Leader analyzes the query and decides how to break it down into subtasks
3. The Team Leader delegates specific tasks to appropriate team members
4. Team members complete their assigned tasks and return their results
5. The Team Leader synthesizes all outputs into a final, cohesive response

This mode is ideal for complex tasks that require multiple specialized skills, coordination, and synthesis of different outputs.

<Steps>
  <Step title="Create a coordinate mode team">
    Create a file `content_team.py`

    ```python content_team.py

    searcher = Agent(
        name="Searcher",
        role="Searches the top URLs for a topic",
        instructions=[
            "Given a topic, first generate a list of 3 search terms related to that topic.",
            "For each search term, search the web and analyze the results.Return the 10 most relevant URLs to the topic.",
            "You are writing for the New York Times, so the quality of the sources is important.",
        ],
        tools=[DuckDuckGoTools()],
        add_datetime_to_instructions=True,
    )
    writer = Agent(
        name="Writer",
        role="Writes a high-quality article",
        description=(
            "You are a senior writer for the New York Times. Given a topic and a list of URLs, "
            "your goal is to write a high-quality NYT-worthy article on the topic."
        ),
        instructions=[
            "First read all urls using `read_article`."
            "Then write a high-quality NYT-worthy article on the topic."
            "The article should be well-structured, informative, engaging and catchy.",
            "Ensure the length is at least as long as a NYT cover story -- at a minimum, 15 paragraphs.",
            "Ensure you provide a nuanced and balanced opinion, quoting facts where possible.",
            "Focus on clarity, coherence, and overall quality.",
            "Never make up facts or plagiarize. Always provide proper attribution.",
            "Remember: you are writing for the New York Times, so the quality of the article is important.",
        ],
        tools=[Newspaper4kTools()],
        add_datetime_to_instructions=True,
    )

    editor = Team(
        name="Editor",
        mode="coordinate",
        model=OpenAIChat("gpt-4o"),
        members=[searcher, writer],
        description="You are a senior NYT editor. Given a topic, your goal is to write a NYT worthy article.",
        instructions=[
            "First ask the search journalist to search for the most relevant URLs for that topic.",
            "Then ask the writer to get an engaging draft of the article.",
            "Edit, proofread, and refine the article to ensure it meets the high standards of the New York Times.",
            "The article should be extremely articulate and well written. "
            "Focus on clarity, coherence, and overall quality.",
            "Remember: you are the final gatekeeper before the article is published, so make sure the article is perfect.",
        ],
        add_datetime_to_instructions=True,
        add_member_tools_to_system_message=False,  # This can be tried to make the agent more consistently get the transfer tool call correct
        enable_agentic_context=True,  # Allow the agent to maintain a shared context and send that to members.
        share_member_interactions=True,  # Share all member responses with subsequent member requests.
        show_members_responses=True,
        markdown=True,
    )
    editor.print_response("Write an article about latest developments in AI.")
    ```
  </Step>

  <Step title="Run the team">
    Install libraries

    ```shell
    pip install openai duckduckgo-search newspaper4k lxml_html_clean
    ```

    Run the team

    ```shell
    python content_team.py
    ```
  </Step>
</Steps>

## Defining Success Criteria

You can guide the coordinator by specifying success criteria for the team:

```python
strategy_team = Team(
    members=[market_analyst, competitive_analyst, strategic_planner],
    mode="coordinate",
    name="Strategy Team",
    description="A team that develops strategic recommendations",
    success_criteria="Produce actionable strategic recommendations supported by market and competitive analysis",
)

response = strategy_team.run(
    "Develop a market entry strategy for our new AI-powered healthcare product"
)
```


