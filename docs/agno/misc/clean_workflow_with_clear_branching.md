---
title: Clean workflow with clear branching
category: misc
source_lines: 84898-84912
line_count: 14
---

# Clean workflow with clear branching
media_workflow = Workflow(
    name="AI Media Generation Workflow",
    description="Generate and analyze images or videos using AI agents",
    steps=[
        Router(
            name="Media Type Router",
            description="Routes to appropriate media generation pipeline",
            selector=media_sequence_selector,
            choices=[image_sequence, video_sequence],  # Clear choices
        )
    ],
)

