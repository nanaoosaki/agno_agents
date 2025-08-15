---
title: Save the response audio to a file
category: misc
source_lines: 46489-46527
line_count: 38
---

# Save the response audio to a file
if response.response_audio is not None:
    write_audio_to_file(
        audio=agent.run_response.response_audio.content, filename="tmp/scary_story.wav"
    )
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export OPENAI_API_KEY=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/models/openai/chat/audio_output_agent.py
      ```

      ```bash Windows
      python cookbook/models/openai/chat/audio_output_agent.py
      ```
    </CodeGroup>
  </Step>
</Steps>


