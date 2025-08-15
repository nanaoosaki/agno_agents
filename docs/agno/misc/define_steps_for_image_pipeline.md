---
title: Define steps for image pipeline
category: misc
source_lines: 56162-56175
line_count: 13
---

# Define steps for image pipeline
generate_image_step = Step(
    name="generate_image",
    agent=image_generator,
    description="Generate a detailed image creation prompt based on the user's request",
)

describe_image_step = Step(
    name="describe_image",
    agent=image_describer,
    description="Analyze and describe the generated image concept in vivid detail",
)

