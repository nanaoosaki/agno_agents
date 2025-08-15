---
title: Get audio files from storage/audio directory
category: misc
source_lines: 76374-76428
line_count: 54
---

# Get audio files from storage/audio directory
agno_root_dir = Path(__file__).parent.parent.parent.resolve()
audio_storage_dir = agno_root_dir.joinpath("storage/audio")
if not audio_storage_dir.exists():
    audio_storage_dir.mkdir(exist_ok=True, parents=True)

agent = Agent(
    name="Transcription Agent",
    model=OpenAIChat(id="gpt-4o"),
    tools=[MLXTranscribeTools(base_dir=audio_storage_dir)],
    instructions=[
        "To transcribe an audio file, use the `transcribe` tool with the name of the audio file as the argument.",
        "You can find all available audio files using the `read_files` tool.",
    ],
    markdown=True,
)

agent.print_response("Summarize the reid hoffman ted talk, split into sections", stream=True)
```

## Toolkit Params

| Parameter                         | Type                           | Default                                  | Description                                  |
| --------------------------------- | ------------------------------ | ---------------------------------------- | -------------------------------------------- |
| `base_dir`                        | `Path`                         | `Path.cwd()`                             | Base directory for audio files               |
| `read_files_in_base_dir`          | `bool`                         | `True`                                   | Whether to register the read\_files function |
| `path_or_hf_repo`                 | `str`                          | `"mlx-community/whisper-large-v3-turbo"` | Path or HuggingFace repo for the model       |
| `verbose`                         | `bool`                         | `None`                                   | Enable verbose output                        |
| `temperature`                     | `float` or `Tuple[float, ...]` | `None`                                   | Temperature for sampling                     |
| `compression_ratio_threshold`     | `float`                        | `None`                                   | Compression ratio threshold                  |
| `logprob_threshold`               | `float`                        | `None`                                   | Log probability threshold                    |
| `no_speech_threshold`             | `float`                        | `None`                                   | No speech threshold                          |
| `condition_on_previous_text`      | `bool`                         | `None`                                   | Whether to condition on previous text        |
| `initial_prompt`                  | `str`                          | `None`                                   | Initial prompt for transcription             |
| `word_timestamps`                 | `bool`                         | `None`                                   | Enable word-level timestamps                 |
| `prepend_punctuations`            | `str`                          | `None`                                   | Punctuations to prepend                      |
| `append_punctuations`             | `str`                          | `None`                                   | Punctuations to append                       |
| `clip_timestamps`                 | `str` or `List[float]`         | `None`                                   | Clip timestamps                              |
| `hallucination_silence_threshold` | `float`                        | `None`                                   | Hallucination silence threshold              |
| `decode_options`                  | `dict`                         | `None`                                   | Additional decoding options                  |

## Toolkit Functions

| Function     | Description                                 |
| ------------ | ------------------------------------------- |
| `transcribe` | Transcribes an audio file using MLX Whisper |
| `read_files` | Lists all audio files in the base directory |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/mlx_transcribe.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/mlx_transcribe_tools.py)


