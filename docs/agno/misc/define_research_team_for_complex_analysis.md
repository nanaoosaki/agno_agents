---
title: Define research team for complex analysis
category: misc
source_lines: 84076-84104
line_count: 28
---

# Define research team for complex analysis
research_team = Team(
    name="Research Team",
    mode="coordinate",
    members=[hackernews_agent, web_agent],
    instructions="Research tech topics from Hackernews and the web",
)

content_planner = Agent(
    name="Content Planner",
    model=OpenAIChat(id="gpt-4o"),
    instructions=[
        "Plan a content schedule over 4 weeks for the provided topic and research content",
        "Ensure that I have posts for 3 posts per week",
    ],
)

content_creation_workflow = Workflow(
    name="Content Creation Workflow",
    description="Automated content creation from blog posts to social media",
    storage=SqliteStorage(
        table_name="workflow_v2",
        db_file="tmp/workflow_v2.db",
        mode="workflow_v2",
    ),
    steps=[research_team, content_planner],
)

