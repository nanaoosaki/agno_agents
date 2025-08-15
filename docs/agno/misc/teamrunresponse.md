---
title: TeamRunResponse
category: misc
source_lines: 68202-68391
line_count: 189
---

# TeamRunResponse
Source: https://docs.agno.com/reference/teams/team-response



The `TeamRunResponse` class represents the response from a team run, containing both the team's overall response and individual member responses. It supports streaming and provides real-time events throughout the execution of a team.

## TeamRunResponse Attributes

| Attribute           | Type                                        | Default           | Description                                                                                                                     |
| ------------------- | ------------------------------------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `content`           | `Any`                                       | `None`            | Content of the response                                                                                                         |
| `content_type`      | `str`                                       | `"str"`           | Specifies the data type of the content                                                                                          |
| `thinking`          | `str`                                       | `None`            | Any thinking content the model produced (used by Anthropic models)                                                              |
| `messages`          | `List[Message]`                             | `None`            | A list of messages included in the response                                                                                     |
| `metrics`           | `Dict[str, Any]`                            | `None`            | Usage metrics of the run                                                                                                        |
| `model`             | `str`                                       | `None`            | The model used in the run                                                                                                       |
| `model_provider`    | `str`                                       | `None`            | The model provider used in the run                                                                                              |
| `member_responses`  | `List[Union[TeamRunResponse, RunResponse]]` | `[]`              | Responses from individual team members                                                                                          |
| `run_id`            | `str`                                       | `None`            | Run Id                                                                                                                          |
| `team_id`           | `str`                                       | `None`            | Team Id for the run                                                                                                             |
| `session_id`        | `str`                                       | `None`            | Session Id for the run                                                                                                          |
| `tools`             | `List[Dict[str, Any]]`                      | `None`            | List of tools provided to the model                                                                                             |
| `images`            | `List[Image]`                               | `None`            | List of images from member runs                                                                                                 |
| `videos`            | `List[Video]`                               | `None`            | List of videos from member runs                                                                                                 |
| `audio`             | `List[Audio]`                               | `None`            | List of audio snippets from member runs                                                                                         |
| `response_audio`    | `ModelResponseAudio`                        | `None`            | The model's raw response in audio                                                                                               |
| `reasoning_content` | `str`                                       | `None`            | Any reasoning content the model produced                                                                                        |
| `citations`         | `Citations`                                 | `None`            | Any citations used in the response                                                                                              |
| `created_at`        | `int`                                       | Current timestamp | Unix timestamp of the response creation                                                                                         |
| `extra_data`        | `RunResponseExtraData`                      | `None`            | Extra data containing optional fields like `references`, `add_messages`, `history`, `reasoning_steps`, and `reasoning_messages` |

## TeamRunResponseEvent Types

The following events are sent by the `Team.run()` function depending on the team's configuration:

### Core Events

| Event Type               | Description                                             |
| ------------------------ | ------------------------------------------------------- |
| `TeamRunStarted`         | Indicates the start of a team run                       |
| `TeamRunResponseContent` | Contains the model's response text as individual chunks |
| `TeamRunCompleted`       | Signals successful completion of the team run           |
| `TeamRunError`           | Indicates an error occurred during the team run         |
| `TeamRunCancelled`       | Signals that the team run was cancelled                 |

### Tool Events

| Event Type              | Description                                                    |
| ----------------------- | -------------------------------------------------------------- |
| `TeamToolCallStarted`   | Indicates the start of a tool call                             |
| `TeamToolCallCompleted` | Signals completion of a tool call, including tool call results |

### Reasoning Events

| Event Type               | Description                                         |
| ------------------------ | --------------------------------------------------- |
| `TeamReasoningStarted`   | Indicates the start of the team's reasoning process |
| `TeamReasoningStep`      | Contains a single step in the reasoning process     |
| `TeamReasoningCompleted` | Signals completion of the reasoning process         |

### Memory Events

| Event Type                  | Description                                    |
| --------------------------- | ---------------------------------------------- |
| `TeamMemoryUpdateStarted`   | Indicates that the team is updating its memory |
| `TeamMemoryUpdateCompleted` | Signals completion of a memory update          |

## Event Attributes

### Base TeamRunResponseEvent

All events inherit from `BaseTeamRunResponseEvent` which provides these common attributes:

| Attribute    | Type            | Default           | Description                          |
| ------------ | --------------- | ----------------- | ------------------------------------ |
| `created_at` | `int`           | Current timestamp | Unix timestamp of the event creation |
| `event`      | `str`           | Event type value  | The type of event                    |
| `team_id`    | `str`           | `""`              | ID of the team generating the event  |
| `run_id`     | `Optional[str]` | `None`            | ID of the current run                |
| `session_id` | `Optional[str]` | `None`            | ID of the current session            |
| `content`    | `Optional[Any]` | `None`            | For backwards compatibility          |

### RunResponseStartedEvent

| Attribute        | Type  | Default            | Description               |
| ---------------- | ----- | ------------------ | ------------------------- |
| `event`          | `str` | `"TeamRunStarted"` | Event type                |
| `model`          | `str` | `""`               | The model being used      |
| `model_provider` | `str` | `""`               | The provider of the model |

### RunResponseContentEvent

| Attribute        | Type                             | Default                    | Description                    |
| ---------------- | -------------------------------- | -------------------------- | ------------------------------ |
| `event`          | `str`                            | `"TeamRunResponseContent"` | Event type                     |
| `content`        | `Optional[Any]`                  | `None`                     | The content of the response    |
| `content_type`   | `str`                            | `"str"`                    | Type of the content            |
| `thinking`       | `Optional[str]`                  | `None`                     | Internal thoughts of the model |
| `citations`      | `Optional[Citations]`            | `None`                     | Citations used in the response |
| `response_audio` | `Optional[AudioResponse]`        | `None`                     | Model's audio response         |
| `image`          | `Optional[ImageArtifact]`        | `None`                     | Image attached to the response |
| `extra_data`     | `Optional[RunResponseExtraData]` | `None`                     | Additional response data       |

### RunResponseCompletedEvent

| Attribute           | Type                                        | Default              | Description                             |
| ------------------- | ------------------------------------------- | -------------------- | --------------------------------------- |
| `event`             | `str`                                       | `"TeamRunCompleted"` | Event type                              |
| `content`           | `Optional[Any]`                             | `None`               | Final content of the response           |
| `content_type`      | `str`                                       | `"str"`              | Type of the content                     |
| `reasoning_content` | `Optional[str]`                             | `None`               | Reasoning content produced              |
| `thinking`          | `Optional[str]`                             | `None`               | Internal thoughts of the model          |
| `citations`         | `Optional[Citations]`                       | `None`               | Citations used in the response          |
| `images`            | `Optional[List[ImageArtifact]]`             | `None`               | Images attached to the response         |
| `videos`            | `Optional[List[VideoArtifact]]`             | `None`               | Videos attached to the response         |
| `audio`             | `Optional[List[AudioArtifact]]`             | `None`               | Audio snippets attached to the response |
| `response_audio`    | `Optional[AudioResponse]`                   | `None`               | Model's audio response                  |
| `extra_data`        | `Optional[RunResponseExtraData]`            | `None`               | Additional response data                |
| `member_responses`  | `List[Union[TeamRunResponse, RunResponse]]` | `[]`                 | Responses from individual team members  |

### RunResponseErrorEvent

| Attribute | Type            | Default          | Description   |
| --------- | --------------- | ---------------- | ------------- |
| `event`   | `str`           | `"TeamRunError"` | Event type    |
| `content` | `Optional[Any]` | `None`           | Error message |

### RunResponseCancelledEvent

| Attribute | Type            | Default              | Description             |
| --------- | --------------- | -------------------- | ----------------------- |
| `event`   | `str`           | `"TeamRunCancelled"` | Event type              |
| `reason`  | `Optional[str]` | `None`               | Reason for cancellation |

### ToolCallStartedEvent

| Attribute | Type                      | Default                 | Description           |
| --------- | ------------------------- | ----------------------- | --------------------- |
| `event`   | `str`                     | `"TeamToolCallStarted"` | Event type            |
| `tool`    | `Optional[ToolExecution]` | `None`                  | The tool being called |

### ToolCallCompletedEvent

| Attribute | Type                            | Default                   | Description                 |
| --------- | ------------------------------- | ------------------------- | --------------------------- |
| `event`   | `str`                           | `"TeamToolCallCompleted"` | Event type                  |
| `tool`    | `Optional[ToolExecution]`       | `None`                    | The tool that was called    |
| `content` | `Optional[Any]`                 | `None`                    | Result of the tool call     |
| `images`  | `Optional[List[ImageArtifact]]` | `None`                    | Images produced by the tool |
| `videos`  | `Optional[List[VideoArtifact]]` | `None`                    | Videos produced by the tool |
| `audio`   | `Optional[List[AudioArtifact]]` | `None`                    | Audio produced by the tool  |

### ReasoningStartedEvent

| Attribute | Type  | Default                  | Description |
| --------- | ----- | ------------------------ | ----------- |
| `event`   | `str` | `"TeamReasoningStarted"` | Event type  |

### ReasoningStepEvent

| Attribute           | Type            | Default               | Description                   |
| ------------------- | --------------- | --------------------- | ----------------------------- |
| `event`             | `str`           | `"TeamReasoningStep"` | Event type                    |
| `content`           | `Optional[Any]` | `None`                | Content of the reasoning step |
| `content_type`      | `str`           | `"str"`               | Type of the content           |
| `reasoning_content` | `str`           | `""`                  | Detailed reasoning content    |

### ReasoningCompletedEvent

| Attribute      | Type            | Default                    | Description                   |
| -------------- | --------------- | -------------------------- | ----------------------------- |
| `event`        | `str`           | `"TeamReasoningCompleted"` | Event type                    |
| `content`      | `Optional[Any]` | `None`                     | Content of the reasoning step |
| `content_type` | `str`           | `"str"`                    | Type of the content           |

### MemoryUpdateStartedEvent

| Attribute | Type  | Default                     | Description |
| --------- | ----- | --------------------------- | ----------- |
| `event`   | `str` | `"TeamMemoryUpdateStarted"` | Event type  |

### MemoryUpdateCompletedEvent

| Attribute | Type  | Default                       | Description |
| --------- | ----- | ----------------------------- | ----------- |
| `event`   | `str` | `"TeamMemoryUpdateCompleted"` | Event type  |


