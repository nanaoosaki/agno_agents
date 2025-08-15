---
title: AWS SES
category: misc
source_lines: 74725-74744
line_count: 19
---

# AWS SES
Source: https://docs.agno.com/tools/toolkits/others/aws_ses



**AWSSESTool** enables an Agent to send emails using Amazon Simple Email Service (SES).

## Prerequisites

The following example requires the `boto3` library and valid AWS credentials. You can install `boto3` via pip:

```shell
pip install boto3
```

You must also configure your AWS credentials so that the SDK can authenticate to SES. The easiest way is via the AWS CLI:

```shell
aws configure
