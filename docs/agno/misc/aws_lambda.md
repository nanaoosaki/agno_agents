---
title: AWS Lambda
category: misc
source_lines: 74669-74692
line_count: 23
---

# AWS Lambda
Source: https://docs.agno.com/tools/toolkits/others/aws_lambda



## Prerequisites

The following example requires the `boto3` library.

```shell
pip install openai boto3
```

## Example

The following agent will use AWS Lambda to list all Lambda functions in our AWS account and invoke a specific Lambda function.

```python cookbook/tools/aws_lambda_tools.py

from agno.agent import Agent
from agno.tools.aws_lambda import AWSLambdaTools


