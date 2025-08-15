---
title: Anthropic Claude
category: misc
source_lines: 63455-63530
line_count: 75
---

# Anthropic Claude
Source: https://docs.agno.com/models/anthropic

Learn how to use Anthropic Claude models in Agno.

Claude is a family of foundational AI models by Anthropic that can be used in a variety of applications.
See their model comparisons [here](https://docs.anthropic.com/en/docs/about-claude/models#model-comparison-table).

We recommend experimenting to find the best-suited model for your use-case. Here are some general recommendations:

* `claude-3-5-sonnet-20241022` model is good for most use-cases and supports image input.
* `claude-3-5-haiku-20241022` model is their fastest model.

Anthropic has rate limits on their APIs. See the [docs](https://docs.anthropic.com/en/api/rate-limits#response-headers) for more information.

## Authentication

Set your `ANTHROPIC_API_KEY` environment. You can get one [from Anthropic here](https://console.anthropic.com/settings/keys).

<CodeGroup>
  ```bash Mac
  export ANTHROPIC_API_KEY=***
  ```

  ```bash Windows
  setx ANTHROPIC_API_KEY ***
  ```
</CodeGroup>

## Example

Use `Claude` with your `Agent`:

<CodeGroup>
  ```python agent.py
  from agno.agent import Agent, RunResponse
  from agno.models.anthropic import Claude

  agent = Agent(
      model=Claude(id="claude-3-5-sonnet-20240620"),
      markdown=True
  )

  # Print the response on the terminal
  agent.print_response("Share a 2 sentence horror story.")
  ```

  ## Prompt caching

  You can enable system prompt caching with our `Claude` model by setting `cache_system_prompt` to `True`:

  ```python
  from agno.agent import Agent
  from agno.models.anthropic import Claude

  agent = Agent(
      model=Claude(
          id="claude-3-5-sonnet-20241022",
          cache_system_prompt=True,
      ),
  )
  ```

  Read more about prompt caching with Agno's `Claude` model [here](https://docs.agno.com/examples/models/anthropic/prompt_caching).
</CodeGroup>

<Note> View more examples [here](../examples/models/anthropic). </Note>

## Params

<Snippet file="model-claude-params.mdx" />

`Claude` is a subclass of the [Model](/reference/models/model) class and has access to the same params.


