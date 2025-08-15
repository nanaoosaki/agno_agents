---
title: Prompts
category: advanced
source_lines: 1388-1513
line_count: 125
---

# Prompts
Source: https://docs.agno.com/agents/prompts



We prompt Agents using `description` and `instructions` and a number of other settings. These settings are used to build the **system** message that is sent to the language model.

Understanding how these prompts are created will help you build better Agents.

The 2 key parameters are:

1. **Description**: A description that guides the overall behaviour of the agent.
2. **Instructions**: A list of precise, task-specific instructions on how to achieve its goal.

<Note>
  Description and instructions only provide a formatting benefit, we do not alter or abstract any information and you can always set the `system_message` to provide your own system prompt.
</Note>

## System message

The system message is created using `description`, `instructions` and a number of other settings. The `description` is added to the start of the system message and `instructions` are added as a list after `Instructions`. For example:

```python instructions.py
from agno.agent import Agent

agent = Agent(
    description="You are a famous short story writer asked to write for a magazine",
    instructions=["You are a pilot on a plane flying from Hawaii to Japan."],
    markdown=True,
    debug_mode=True,
)
agent.print_response("Tell me a 2 sentence horror story.", stream=True)
```

Will translate to (set `debug_mode=True` to view the logs):

```js
DEBUG    ============== system ==============
DEBUG    You are a famous short story writer asked to write for a magazine

         ## Instructions
         - You are a pilot on a plane flying from Hawaii to Japan.
         - Use markdown to format your answers.
DEBUG    ============== user ==============
DEBUG    Tell me a 2 sentence horror story.
DEBUG    ============== assistant ==============
DEBUG    As the autopilot disengaged inexplicably mid-flight over the Pacific, the pilot glanced at the copilot's seat
         only to find it empty despite his every recall of a full crew boarding. Hands trembling, he looked into the
         cockpit's rearview mirror and found his own reflection grinning back with blood-red eyes, whispering,
         "There's no escape, not at 30,000 feet."
DEBUG    **************** METRICS START ****************
DEBUG    * Time to first token:         0.4518s
DEBUG    * Time to generate response:   1.2594s
DEBUG    * Tokens per second:           63.5243 tokens/s
DEBUG    * Input tokens:                59
DEBUG    * Output tokens:               80
DEBUG    * Total tokens:                139
DEBUG    * Prompt tokens details:       {'cached_tokens': 0}
DEBUG    * Completion tokens details:   {'reasoning_tokens': 0}
DEBUG    **************** METRICS END ******************
```

## Set the system message directly

You can manually set the system message using the `system_message` parameter.

```python
from agno.agent import Agent

agent = Agent(system_message="Share a 2 sentence story about")
agent.print_response("Love in the year 12000.")
```

<Tip>
  Some models via some model providers, like `llama-3.2-11b-vision-preview` on Groq, require no system message with other messages. To remove the system message, set `create_default_system_message=False` and `system_message=None`. Additionally, if `markdown=True` is set, it will add a system message, so either remove it or explicitly disable the system message.
</Tip>

## User message

The input `message` sent to the `Agent.run()` or `Agent.print_response()` functions is used as the user message.

## Default system message

The Agent creates a default system message that can be customized using the following parameters:

| Parameter                       | Type        | Default  | Description                                                                                                                                                             |
| ------------------------------- | ----------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `description`                   | `str`       | `None`   | A description of the Agent that is added to the start of the system message.                                                                                            |
| `goal`                          | `str`       | `None`   | Describe the task the agent should achieve.                                                                                                                             |
| `instructions`                  | `List[str]` | `None`   | List of instructions added to the system prompt in `<instructions>` tags. Default instructions are also created depending on values for `markdown`, `output_model` etc. |
| `additional_context`            | `str`       | `None`   | Additional context added to the end of the system message.                                                                                                              |
| `expected_output`               | `str`       | `None`   | Provide the expected output from the Agent. This is added to the end of the system message.                                                                             |
| `markdown`                      | `bool`      | `False`  | Add an instruction to format the output using markdown.                                                                                                                 |
| `add_datetime_to_instructions`  | `bool`      | `False`  | If True, add the current datetime to the prompt to give the agent a sense of time. This allows for relative times like "tomorrow" to be used in the prompt              |
| `system_message`                | `str`       | `None`   | System prompt: provide the system prompt as a string                                                                                                                    |
| `system_message_role`           | `str`       | `system` | Role for the system message.                                                                                                                                            |
| `create_default_system_message` | `bool`      | `True`   | If True, build a default system prompt using agent settings and use that.                                                                                               |

<Tip>
  Disable the default system message by setting `create_default_system_message=False`.
</Tip>

## Default user message

The Agent creates a default user message, which is either the input message or a message with the `context` if `enable_rag=True`. The default user message can be customized using:

| Parameter                     | Type                      | Default  | Description                                                                                                                  |
| ----------------------------- | ------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `context`                     | `str`                     | `None`   | Additional context added to the end of the user message.                                                                     |
| `add_context`                 | `bool`                    | `False`  | If True, add the context to the user prompt.                                                                                 |
| `resolve_context`             | `bool`                    | `True`   | If True, resolve the context (i.e. call any functions in the context) before adding it to the user prompt.                   |
| `add_references`              | `bool`                    | `False`  | Enable RAG by adding references from the knowledge base to the prompt.                                                       |
| `retriever`                   | `Callable`                | `None`   | Function to get references to add to the user\_message. This function, if provided, is called when `add_references` is True. |
| `references_format`           | `Literal["json", "yaml"]` | `"json"` | Format of the references.                                                                                                    |
| `add_history_to_messages`     | `bool`                    | `False`  | If true, adds the chat history to the messages sent to the Model.                                                            |
| `num_history_responses`       | `int`                     | `3`      | Number of historical responses to add to the messages.                                                                       |
| `user_message`                | `Union[List, Dict, str]`  | `None`   | Provide the user prompt as a string. Note: this will ignore the message sent to the run function.                            |
| `user_message_role`           | `str`                     | `user`   | Role for the user message.                                                                                                   |
| `create_default_user_message` | `bool`                    | `True`   | If True, build a default user prompt using references and chat history.                                                      |

<Tip>
  Disable the default user message by setting `create_default_user_message=False`.
</Tip>


