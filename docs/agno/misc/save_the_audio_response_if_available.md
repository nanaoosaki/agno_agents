---
title: Save the audio response if available
category: misc
source_lines: 34750-34756
line_count: 6
---

# Save the audio response if available
if agent.run_response.response_audio is not None:
    write_audio_to_file(
        audio=agent.run_response.response_audio.content, filename="tmp/response.wav"
    )

