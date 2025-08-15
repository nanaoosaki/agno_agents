---
title: OpenAI Responses
category: misc
source_lines: 65194-65251
line_count: 57
---

# OpenAI Responses
Source: https://docs.agno.com/models/openai-responses

Learn how to use OpenAI Responses with Agno.

`OpenAIResponses` is a class for interacting with OpenAI models using the Responses API. This class provides a streamlined interface for working with OpenAI's newer Responses API, which is distinct from the traditional Chat API. It supports advanced features like tool use, file processing, and knowledge retrieval.

## Authentication

Set your `OPENAI_API_KEY` environment variable. You can get one [from OpenAI here](https://platform.openai.com/account/api-keys).

<CodeGroup>
  ```bash Mac
  export OPENAI_API_KEY=sk-***
  ```

  ```bash Windows
  setx OPENAI_API_KEY sk-***
  ```
</CodeGroup>

## Example

Use `OpenAIResponses` with your `Agent`:

<CodeGroup>
  ```python agent.py

  from agno.agent import Agent
  from agno.media import File
  from agno.models.openai.responses import OpenAIResponses

  agent = Agent(
      model=OpenAIResponses(id="gpt-4o-mini"),
      tools=[{"type": "file_search"}, {"type": "web_search_preview"}],
      markdown=True,
  )

  agent.print_response(
      "Summarize the contents of the attached file and search the web for more information.",
      files=[File(url="https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf")],
  )

  ```
</CodeGroup>

<Note> View more examples [here](../examples/models/openai/responses). </Note>

## Params

For more information, please refer to the [OpenAI Responses docs](https://platform.openai.com/docs/api-reference/responses) as well.

<Snippet file="model-openai-responses-params.mdx" />

`OpenAIResponses` is a subclass of the [Model](/reference/models/model) class and has access to the same params.


