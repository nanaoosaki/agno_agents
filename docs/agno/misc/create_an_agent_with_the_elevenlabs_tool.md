---
title: Create an Agent with the ElevenLabs tool
category: misc
source_lines: 75530-75564
line_count: 34
---

# Create an Agent with the ElevenLabs tool
agent = Agent(tools=[
    ElevenLabsTools(
        voice_id="JBFqnCBsd6RMkjVDRZzb", model_id="eleven_multilingual_v2", target_directory="audio_generations"
    )
], name="ElevenLabs Agent")

agent.print_response("Generate a audio summary of the big bang theory", markdown=True)
```

## Toolkit Params

| Parameter          | Type            | Default                  | Description                                                                                                                                                                    |
| ------------------ | --------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `api_key`          | `str`           | `None`                   | The Eleven Labs API key for authentication                                                                                                                                     |
| `voice_id`         | `str`           | `JBFqnCBsd6RMkjVDRZzb`   | The voice ID to use for the audio generation                                                                                                                                   |
| `target_directory` | `Optional[str]` | `None`                   | The directory to save the audio file                                                                                                                                           |
| `model_id`         | `str`           | `eleven_multilingual_v2` | The model's id to use for the audio generation                                                                                                                                 |
| `output_format`    | `str`           | `mp3_44100_64`           | The output format to use for the audio generation (check out [the docs](https://elevenlabs.io/docs/api-reference/text-to-speech#parameter-output-format) for more information) |

## Toolkit Functions

| Function                | Description                                     |
| ----------------------- | ----------------------------------------------- |
| `text_to_speech`        | Convert text to speech                          |
| `generate_sound_effect` | Generate sound effect audio from a text prompt. |
| `get_voices`            | Get the list of voices available                |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/eleven_labs.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/elevenlabs_tools.py)


