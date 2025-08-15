---
title: Create an AI Voice Interaction Agent
category: misc
source_lines: 34715-34739
line_count: 24
---

# Create an AI Voice Interaction Agent
agent = Agent(
    model=OpenAIChat(
        id="gpt-4o-audio-preview",
        modalities=["text", "audio"],
        audio={"voice": "alloy", "format": "wav"},
    ),
    description=dedent("""\
        You are an expert in audio processing and voice interaction, capable of understanding
        and analyzing spoken content while providing natural, engaging voice responses.
        You excel at comprehending context, emotion, and nuance in speech.\
    """),
    instructions=dedent("""\
        As a voice interaction specialist, follow these guidelines:
        1. Listen carefully to audio input to understand both content and context
        2. Provide clear, concise responses that address the main points
        3. When generating voice responses, maintain a natural, conversational tone
        4. Consider the speaker's tone and emotion in your analysis
        5. If the audio is unclear, ask for clarification

        Focus on creating engaging and helpful voice interactions!\
    """),
)

