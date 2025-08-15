---
title: Define the two distinct pipelines
category: misc
source_lines: 56188-56231
line_count: 43
---

# Define the two distinct pipelines
image_sequence = Steps(
    name="image_generation",
    description="Complete image generation and analysis workflow",
    steps=[generate_image_step, describe_image_step],
)

video_sequence = Steps(
    name="video_generation",
    description="Complete video production and analysis workflow",
    steps=[generate_video_step, describe_video_step],
)


def media_sequence_selector(step_input: StepInput) -> List[Step]:
    """
    Simple pipeline selector based on keywords in the message.

    Args:
        step_input: StepInput containing message

    Returns:
        List of Steps to execute
    """

    # Check if message exists and is a string
    if not step_input.message or not isinstance(step_input.message, str):
        return [image_sequence]  # Default to image sequence

    # Convert message to lowercase for case-insensitive matching
    message_lower = step_input.message.lower()

    # Check for video keywords
    if "video" in message_lower:
        return [video_sequence]
    # Check for image keywords
    elif "image" in message_lower:
        return [image_sequence]
    else:
        # Default to image for any other case
        return [image_sequence]


