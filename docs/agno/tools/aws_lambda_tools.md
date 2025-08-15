---
title: AWS Lambda Tools
category: tools
source_lines: 28010-28066
line_count: 56
---

# AWS Lambda Tools
Source: https://docs.agno.com/examples/concepts/tools/others/aws_lambda



## Code

```python cookbook/tools/aws_lambda_tools.py
from agno.agent import Agent
from agno.tools.aws_lambda import AWSLambdaTools

agent = Agent(
    tools=[AWSLambdaTools(region_name="us-east-1")],
    name="AWS Lambda Agent",
    show_tool_calls=True,
)

agent.print_response("List all Lambda functions in our AWS account", markdown=True)
agent.print_response(
    "Invoke the 'hello-world' Lambda function with an empty payload", markdown=True
)
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your AWS credentials">
    ```bash
    export AWS_ACCESS_KEY_ID=xxx
    export AWS_SECRET_ACCESS_KEY=xxx
    export OPENAI_API_KEY=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U boto3 openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/tools/aws_lambda_tools.py
      ```

      ```bash Windows
      python cookbook/tools/aws_lambda_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


