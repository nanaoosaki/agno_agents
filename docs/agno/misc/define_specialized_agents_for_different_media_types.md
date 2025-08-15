---
title: Define specialized agents for different media types
category: misc
source_lines: 56109-56162
line_count: 53
---

# Define specialized agents for different media types
image_generator = Agent(
    name="Image Generator",
    model=OpenAIChat(id="gpt-4o"),
    tools=[OpenAITools(image_model="gpt-image-1")],
    instructions="""You are an expert image generation specialist.
    When users request image creation, you should ACTUALLY GENERATE the image using your available image generation tools.

    Always use the generate_image tool to create the requested image based on the user's specifications.
    Include detailed, creative prompts that incorporate style, composition, lighting, and mood details.

    After generating the image, provide a brief description of what you created.""",
)

image_describer = Agent(
    name="Image Describer",
    model=OpenAIChat(id="gpt-4o"),
    instructions="""You are an expert image analyst and describer.
    When you receive an image (either as input or from a previous step), analyze and describe it in vivid detail, including:
    - Visual elements and composition
    - Colors, lighting, and mood
    - Artistic style and technique
    - Emotional impact and narrative

    If no image is provided, work with the image description or prompt from the previous step.
    Provide rich, engaging descriptions that capture the essence of the visual content.""",
)

video_generator = Agent(
    name="Video Generator",
    model=OpenAIChat(id="gpt-4o"),
    # Video Generation only works on VertexAI mode
    tools=[GeminiTools(vertexai=True)],
    instructions="""You are an expert video production specialist.
    Create detailed video generation prompts and storyboards based on user requests.
    Include scene descriptions, camera movements, transitions, and timing.
    Consider pacing, visual storytelling, and technical aspects like resolution and duration.
    Format your response as a comprehensive video production plan.""",
)

video_describer = Agent(
    name="Video Describer",
    model=OpenAIChat(id="gpt-4o"),
    instructions="""You are an expert video analyst and critic.
    Analyze and describe videos comprehensively, including:
    - Scene composition and cinematography
    - Narrative flow and pacing
    - Visual effects and production quality
    - Audio-visual harmony and mood
    - Technical execution and artistic merit
    Provide detailed, professional video analysis.""",
)

