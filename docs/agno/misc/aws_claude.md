---
title: AWS Claude
category: misc
source_lines: 63593-63653
line_count: 60
---

# AWS Claude
Source: https://docs.agno.com/models/aws-claude

Learn how to use AWS Claude models in Agno.

Use Claude models through AWS Bedrock. This provides a native Claude integration optimized for AWS infrastructure.

We recommend experimenting to find the best-suited model for your use-case. Here are some general recommendations:

* `anthropic.claude-3-5-sonnet-20241022-v2:0` model is good for most use-cases and supports image input.
* `anthropic.claude-3-5-haiku-20241022-v2:0` model is their fastest model.

## Authentication

Set your `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` and `AWS_REGION` environment variables.

Get your keys from [here](https://us-east-1.console.aws.amazon.com/iam/home?region=us-east-1#/home).

<CodeGroup>
  ```bash Mac
  export AWS_ACCESS_KEY_ID=***
  export AWS_SECRET_ACCESS_KEY=***
  export AWS_REGION=***
  ```

  ```bash Windows
  setx AWS_ACCESS_KEY_ID ***
  setx AWS_SECRET_ACCESS_KEY ***
  setx AWS_REGION ***
  ```
</CodeGroup>

## Example

Use `Claude` with your `Agent`:

<CodeGroup>
  ```python agent.py
  from agno.agent import Agent
  from agno.models.aws import Claude

  agent = Agent(
      model=Claude(id="anthropic.claude-3-5-sonnet-20240620-v1:0"),
      markdown=True
  )

  # Print the response on the terminal
  agent.print_response("Share a 2 sentence horror story.")
  ```
</CodeGroup>

<Note> View more examples [here](../examples/models/aws/claude). </Note>

## Parameters

<Snippet file="model-aws-claude-params.mdx" />

`Claude` is a subclass of [`AnthropicClaude`](/models/anthropic) and has access to the same params.


