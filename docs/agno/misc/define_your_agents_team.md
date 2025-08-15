---
title: Define your agents/team
category: misc
source_lines: 84245-84259
line_count: 14
---

# Define your agents/team
...

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

