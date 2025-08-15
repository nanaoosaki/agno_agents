---
title: Define two completely different workflows as Steps
category: misc
source_lines: 84865-84898
line_count: 33
---

# Define two completely different workflows as Steps
image_sequence = Steps(
    name="image_generation",
    description="Complete image generation and analysis workflow",
    steps=[
        Step(name="generate_image", agent=image_generator),
        Step(name="describe_image", agent=image_describer),
    ],
)

video_sequence = Steps(
    name="video_generation", 
    description="Complete video production and analysis workflow",
    steps=[
        Step(name="generate_video", agent=video_generator),
        Step(name="describe_video", agent=video_describer),
    ],
)

def media_sequence_selector(step_input) -> List[Step]:
    """Route to appropriate media generation pipeline"""
    if not step_input.message:
        return [image_sequence]
        
    message_lower = step_input.message.lower()
    
    if "video" in message_lower:
        return [video_sequence]
    elif "image" in message_lower:
        return [image_sequence]
    else:
        return [image_sequence]  # Default

