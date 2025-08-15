---
title: Question with streaming
category: advanced
source_lines: 18585-18640
line_count: 55
---

# Question with streaming
output_stream: Iterator[RunResponse] = agent.run(
    "Is a golden retriever a good family dog?", 
    stream=True
)

with wave.open("tmp/answer_1.wav", "wb") as wav_file:
    wav_file.setnchannels(CHANNELS)
    wav_file.setsampwidth(SAMPLE_WIDTH)
    wav_file.setframerate(SAMPLE_RATE)
    
    for response in output_stream:
        if response.response_audio:
            if response.response_audio.transcript:
                print(response.response_audio.transcript, end="", flush=True)
            if response.response_audio.content:
                try:
                    pcm_bytes = base64.b64decode(response.response_audio.content)
                    wav_file.writeframes(pcm_bytes)
                except Exception as e:
                    print(f"Error decoding audio: {e}")
print()
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
      python cookbook/agent_concepts/multimodal/audio_streaming.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/multimodal/audio_streaming.py
      ```
    </CodeGroup>
  </Step>
</Steps>


