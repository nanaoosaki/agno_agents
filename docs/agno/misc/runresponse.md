---
title: RunResponse
category: misc
source_lines: 67104-67266
line_count: 162
---

# RunResponse
Source: https://docs.agno.com/reference/agents/run-response



## RunResponse Attributes

| Attribute           | Type                   | Default | Description                                                                                                                      |
| ------------------- | ---------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `content`           | `Any`                  | `None`  | Content of the response.                                                                                                         |
| `content_type`      | `str`                  | `"str"` | Specifies the data type of the content.                                                                                          |
| `thinking`          | `str`                  | `None`  | Any thinking content the model produced (used by Anthropic models).                                                              |
| `reasoning_content` | `str`                  | `None`  | Any reasoning content the model produced.                                                                                        |
| `messages`          | `List[Message]`        | `None`  | A list of messages included in the response.                                                                                     |
| `metrics`           | `Dict[str, Any]`       | `None`  | Usage metrics of the run.                                                                                                        |
| `model`             | `str`                  | `None`  | The model used in the run.                                                                                                       |
| `model_provider`    | `str`                  | `None`  | The model provider used in the run.                                                                                              |
| `run_id`            | `str`                  | `None`  | Run Id.                                                                                                                          |
| `agent_id`          | `str`                  | `None`  | Agent Id for the run.                                                                                                            |
| `session_id`        | `str`                  | `None`  | Session Id for the run.                                                                                                          |
| `tools`             | `List[Dict[str, Any]]` | `None`  | List of tools provided to the model.                                                                                             |
| `images`            | `List[Image]`          | `None`  | List of images the model produced.                                                                                               |
| `videos`            | `List[Video]`          | `None`  | List of videos the model produced.                                                                                               |
| `audio`             | `List[Audio]`          | `None`  | List of audio snippets the model produced.                                                                                       |
| `response_audio`    | `ModelResponseAudio`   | `None`  | The model's raw response in audio.                                                                                               |
| `citations`         | `Citations`            | `None`  | Any citations used in the response.                                                                                              |
| `created_at`        | `int`                  | -       | Unix timestamp of the response creation.                                                                                         |
| `extra_data`        | `RunResponseExtraData` | `None`  | Extra data containing optional fields like `references`, `add_messages`, `history`, `reasoning_steps`, and `reasoning_messages`. |

## RunResponseEvent Types and Attributes

### Base RunResponseEvent Attributes

All events inherit from `BaseAgentRunResponseEvent` which provides these common attributes:

| Attribute    | Type            | Default           | Description                          |
| ------------ | --------------- | ----------------- | ------------------------------------ |
| `created_at` | `int`           | Current timestamp | Unix timestamp of the event creation |
| `event`      | `str`           | Event type value  | The type of event                    |
| `agent_id`   | `str`           | `""`              | ID of the agent generating the event |
| `run_id`     | `Optional[str]` | `None`            | ID of the current run                |
| `session_id` | `Optional[str]` | `None`            | ID of the current session            |
| `content`    | `Optional[Any]` | `None`            | For backwards compatibility          |

### RunResponseStartedEvent

| Attribute        | Type  | Default        | Description               |
| ---------------- | ----- | -------------- | ------------------------- |
| `event`          | `str` | `"RunStarted"` | Event type                |
| `model`          | `str` | `""`           | The model being used      |
| `model_provider` | `str` | `""`           | The provider of the model |

### RunResponseContentEvent

| Attribute        | Type                             | Default                | Description                    |
| ---------------- | -------------------------------- | ---------------------- | ------------------------------ |
| `event`          | `str`                            | `"RunResponseContent"` | Event type                     |
| `content`        | `Optional[Any]`                  | `None`                 | The content of the response    |
| `content_type`   | `str`                            | `"str"`                | Type of the content            |
| `thinking`       | `Optional[str]`                  | `None`                 | Internal thoughts of the model |
| `citations`      | `Optional[Citations]`            | `None`                 | Citations used in the response |
| `response_audio` | `Optional[AudioResponse]`        | `None`                 | Model's audio response         |
| `image`          | `Optional[ImageArtifact]`        | `None`                 | Image attached to the response |
| `extra_data`     | `Optional[RunResponseExtraData]` | `None`                 | Additional response data       |

### RunResponseCompletedEvent

| Attribute           | Type                             | Default          | Description                             |
| ------------------- | -------------------------------- | ---------------- | --------------------------------------- |
| `event`             | `str`                            | `"RunCompleted"` | Event type                              |
| `content`           | `Optional[Any]`                  | `None`           | Final content of the response           |
| `content_type`      | `str`                            | `"str"`          | Type of the content                     |
| `reasoning_content` | `Optional[str]`                  | `None`           | Reasoning content produced              |
| `thinking`          | `Optional[str]`                  | `None`           | Internal thoughts of the model          |
| `citations`         | `Optional[Citations]`            | `None`           | Citations used in the response          |
| `images`            | `Optional[List[ImageArtifact]]`  | `None`           | Images attached to the response         |
| `videos`            | `Optional[List[VideoArtifact]]`  | `None`           | Videos attached to the response         |
| `audio`             | `Optional[List[AudioArtifact]]`  | `None`           | Audio snippets attached to the response |
| `response_audio`    | `Optional[AudioResponse]`        | `None`           | Model's audio response                  |
| `extra_data`        | `Optional[RunResponseExtraData]` | `None`           | Additional response data                |

### RunResponsePausedEvent

| Attribute | Type                            | Default       | Description                     |
| --------- | ------------------------------- | ------------- | ------------------------------- |
| `event`   | `str`                           | `"RunPaused"` | Event type                      |
| `tools`   | `Optional[List[ToolExecution]]` | `None`        | Tools that require confirmation |

### RunResponseContinuedEvent

| Attribute | Type  | Default          | Description |
| --------- | ----- | ---------------- | ----------- |
| `event`   | `str` | `"RunContinued"` | Event type  |

### RunResponseErrorEvent

| Attribute | Type            | Default      | Description   |
| --------- | --------------- | ------------ | ------------- |
| `event`   | `str`           | `"RunError"` | Event type    |
| `content` | `Optional[str]` | `None`       | Error message |

### RunResponseCancelledEvent

| Attribute | Type            | Default          | Description             |
| --------- | --------------- | ---------------- | ----------------------- |
| `event`   | `str`           | `"RunCancelled"` | Event type              |
| `reason`  | `Optional[str]` | `None`           | Reason for cancellation |

### ReasoningStartedEvent

| Attribute | Type  | Default              | Description |
| --------- | ----- | -------------------- | ----------- |
| `event`   | `str` | `"ReasoningStarted"` | Event type  |

### ReasoningStepEvent

| Attribute           | Type            | Default           | Description                   |
| ------------------- | --------------- | ----------------- | ----------------------------- |
| `event`             | `str`           | `"ReasoningStep"` | Event type                    |
| `content`           | `Optional[Any]` | `None`            | Content of the reasoning step |
| `content_type`      | `str`           | `"str"`           | Type of the content           |
| `reasoning_content` | `str`           | `""`              | Detailed reasoning content    |

### ReasoningCompletedEvent

| Attribute      | Type            | Default                | Description                   |
| -------------- | --------------- | ---------------------- | ----------------------------- |
| `event`        | `str`           | `"ReasoningCompleted"` | Event type                    |
| `content`      | `Optional[Any]` | `None`                 | Content of the reasoning step |
| `content_type` | `str`           | `"str"`                | Type of the content           |

### ToolCallStartedEvent

| Attribute | Type                      | Default             | Description           |
| --------- | ------------------------- | ------------------- | --------------------- |
| `event`   | `str`                     | `"ToolCallStarted"` | Event type            |
| `tool`    | `Optional[ToolExecution]` | `None`              | The tool being called |

### ToolCallCompletedEvent

| Attribute | Type                            | Default               | Description                 |
| --------- | ------------------------------- | --------------------- | --------------------------- |
| `event`   | `str`                           | `"ToolCallCompleted"` | Event type                  |
| `tool`    | `Optional[ToolExecution]`       | `None`                | The tool that was called    |
| `content` | `Optional[Any]`                 | `None`                | Result of the tool call     |
| `images`  | `Optional[List[ImageArtifact]]` | `None`                | Images produced by the tool |
| `videos`  | `Optional[List[VideoArtifact]]` | `None`                | Videos produced by the tool |
| `audio`   | `Optional[List[AudioArtifact]]` | `None`                | Audio produced by the tool  |

### MemoryUpdateStartedEvent

| Attribute | Type  | Default                 | Description |
| --------- | ----- | ----------------------- | ----------- |
| `event`   | `str` | `"MemoryUpdateStarted"` | Event type  |

### MemoryUpdateCompletedEvent

| Attribute | Type  | Default                   | Description |
| --------- | ----- | ------------------------- | ----------- |
| `event`   | `str` | `"MemoryUpdateCompleted"` | Event type  |


