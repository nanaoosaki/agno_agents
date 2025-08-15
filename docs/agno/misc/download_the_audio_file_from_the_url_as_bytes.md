---
title: Download the audio file from the URL as bytes
category: misc
source_lines: 41141-41182
line_count: 41
---

# Download the audio file from the URL as bytes
response = requests.get(url)
audio_content = response.content

agent.print_response(
    "Tell me about this audio",
    audio=[Audio(content=audio_content)],
)
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export GOOGLE_API_KEY=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U google-genai requests agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/models/google/gemini/audio_input_bytes_content.py
      ```

      ```bash Windows
      python cookbook/models/google/gemini/audio_input_bytes_content.py
      ```
    </CodeGroup>
  </Step>
</Steps>


