---
title: Configure email settings
category: misc
source_lines: 74766-74819
line_count: 53
---

# Configure email settings
sender_email = "verified-sender@example.com"  # Your verified SES email
sender_name = "Sender Name"
region_name = "us-east-1"

agent = Agent(
    name="Research Newsletter Agent",
    model=OpenAIChat(id="gpt-4o"),
    tools=[
        AWSSESTool(
            sender_email=sender_email,
            sender_name=sender_name,
            region_name=region_name
        ),
        DuckDuckGoTools(),
    ],
    markdown=True,
    show_tool_calls=True,
    instructions=[
        "When given a prompt:",
        "1. Extract the recipient's complete email address (e.g. user@domain.com)",
        "2. Research the latest AI developments using DuckDuckGo",
        "3. Compose a concise, engaging email summarising 3 – 4 key developments",
        "4. Send the email using AWS SES via the send_email tool",
    ],
)

agent.print_response(
    "Research recent AI developments in healthcare and email the summary to johndoe@example.com"
)
```

## Toolkit Params

| Parameter      | Type  | Default       | Description                              |
| -------------- | ----- | ------------- | ---------------------------------------- |
| `sender_email` | `str` | `None`        | Verified SES sender address.             |
| `sender_name`  | `str` | `None`        | Display name that appears to recipients. |
| `region_name`  | `str` | `"us-east-1"` | AWS region where SES is provisioned.     |

## Toolkit Functions

| Function     | Description                                                                          |
| ------------ | ------------------------------------------------------------------------------------ |
| `send_email` | Send a plain-text email. Accepts the arguments: `subject`, `body`, `receiver_email`. |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/aws_ses.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/aws_ses_tools.py)
* [Amazon SES Documentation](https://docs.aws.amazon.com/ses/latest/dg/)


