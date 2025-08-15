---
title: Define steps for video pipeline
category: misc
source_lines: 56175-56188
line_count: 13
---

# Define steps for video pipeline
generate_video_step = Step(
    name="generate_video",
    agent=video_generator,
    description="Create a comprehensive video production plan and storyboard",
)

describe_video_step = Step(
    name="describe_video",
    agent=video_describer,
    description="Analyze and critique the video production plan with professional insights",
)

