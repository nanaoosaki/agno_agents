---
title: Please download a sample audio file to test this Agent and upload using:
category: misc
source_lines: 41279-41320
line_count: 41
---

# Please download a sample audio file to test this Agent and upload using:
audio_path = Path(__file__).parent.joinpath("sample.mp3")

agent.print_response(
    "Tell me about this audio",
    audio=[Audio(filepath=audio_path)],
    stream=True,
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
    pip install -U google-genai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/models/google/gemini/audio_input_local_file_upload.py
      ```

      ```bash Windows
      python cookbook/models/google/gemini/audio_input_local_file_upload.py
      ```
    </CodeGroup>
  </Step>
</Steps>


