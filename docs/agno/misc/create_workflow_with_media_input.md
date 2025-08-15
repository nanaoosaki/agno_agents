---
title: Create workflow with media input
category: misc
source_lines: 82958-82970
line_count: 12
---

# Create workflow with media input
media_workflow = Workflow(
    name="Image Analysis and Research Workflow",
    description="Analyze an image and research related news",
    steps=[analysis_step, research_step],
    storage=SqliteStorage(
        table_name="workflow_v2",
        db_file="tmp/workflow_v2.db",
        mode="workflow_v2",
    ),
)

