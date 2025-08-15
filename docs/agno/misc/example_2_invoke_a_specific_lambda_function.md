---
title: Example 2: Invoke a specific Lambda function
category: misc
source_lines: 74702-74725
line_count: 23
---

# Example 2: Invoke a specific Lambda function
agent.print_response("Invoke the 'hello-world' Lambda function with an empty payload", markdown=True)
```

## Toolkit Params

| Parameter     | Type  | Default       | Description                                         |
| ------------- | ----- | ------------- | --------------------------------------------------- |
| `region_name` | `str` | `"us-east-1"` | AWS region name where Lambda functions are located. |

## Toolkit Functions

| Function          | Description                                                                                                           |
| ----------------- | --------------------------------------------------------------------------------------------------------------------- |
| `list_functions`  | Lists all Lambda functions available in the AWS account.                                                              |
| `invoke_function` | Invokes a specific Lambda function with an optional payload. Takes `function_name` and optional `payload` parameters. |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/aws_lambda.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/aws_lambda_tools.py)


