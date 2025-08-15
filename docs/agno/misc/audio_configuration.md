---
title: Audio Configuration
category: misc
source_lines: 18567-18585
line_count: 18
---

# Audio Configuration
SAMPLE_RATE = 24000  # Hz (24kHz)
CHANNELS = 1  # Mono
SAMPLE_WIDTH = 2  # Bytes (16 bits)

agent = Agent(
    model=OpenAIChat(
        id="gpt-4o-audio-preview",
        modalities=["text", "audio"],
        audio={
            "voice": "alloy",
            "format": "pcm16",  # Required for streaming
        },
    ),
    debug_mode=True,
    add_history_to_messages=True,
)

