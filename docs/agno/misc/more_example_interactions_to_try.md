---
title: More example interactions to try:
category: misc
source_lines: 34756-34793
line_count: 37
---

# More example interactions to try:
"""
Try these voice interaction scenarios:
1. "Can you summarize the main points discussed in this recording?"
2. "What emotions or tone do you detect in the speaker's voice?"
3. "Please provide a detailed analysis of the speech patterns and clarity"
4. "Can you identify any background noises or audio quality issues?"
5. "What is the overall context and purpose of this recording?"

Note: You can use your own audio files by converting them to base64 format.
Example for using your own audio file:

with open('your_audio.wav', 'rb') as audio_file:
    audio_data = audio_file.read()
    agent.run("Analyze this audio", audio=[Audio(content=audio_data, format="wav")])
"""
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Install libraries">
    ```bash
    pip install openai requests agno
    ```
  </Step>

  <Step title="Run the agent">
    ```bash
    python audio_agent.py
    ```
  </Step>
</Steps>


