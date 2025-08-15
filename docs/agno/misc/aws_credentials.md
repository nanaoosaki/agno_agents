---
title: AWS Credentials
category: misc
source_lines: 68689-68704
line_count: 15
---

# AWS Credentials
AWS_ACCESS_KEY_ID = getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = getenv("AWS_SECRET_ACCESS_KEY")

storage = DynamoDbStorage(
    # store sessions in the ai.sessions table
    table_name="agent_sessions",
    # region_name: DynamoDB region name
    region_name="us-east-1",
    # aws_access_key_id: AWS access key id
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    # aws_secret_access_key: AWS secret access key
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
)

