---
title: LM Studio
category: misc
source_lines: 64744-64794
line_count: 50
---

# LM Studio
Source: https://docs.agno.com/models/lmstudio

Learn how to use LM Studio with Agno.

Run Large Language Models locally with LM Studio

[LM Studio](https://lmstudio.ai) is a fantastic tool for running models locally.

LM Studio supports multiple open-source models. See the library [here](https://lmstudio.ai/models).

We recommend experimenting to find the best-suited model for your use-case. Here are some general recommendations:

* `llama3.3` models are good for most basic use-cases.
* `qwen` models perform specifically well with tool use.
* `deepseek-r1` models have strong reasoning capabilities.
* `phi4` models are powerful, while being really small in size.

## Set up a model

Install [LM Studio](https://lmstudio.ai), download the model you want to use, and run it.

## Example

After you have the model locally, use the `LM Studio` model class to access it

<CodeGroup>
  ```python agent.py
  from agno.agent import Agent, RunResponse
  from agno.models.lmstudio import LMStudio

  agent = Agent(
      model=LMStudio(id="qwen2.5-7b-instruct-1m"),
      markdown=True
  )

  # Print the response in the terminal
  agent.print_response("Share a 2 sentence horror story.")
  ```
</CodeGroup>

<Note> View more examples [here](../examples/models/lmstudio). </Note>

## Params

<Snippet file="model-lmstudio-params.mdx" />

`LM Studio` also supports the params of [OpenAI](/reference/models/openai).


