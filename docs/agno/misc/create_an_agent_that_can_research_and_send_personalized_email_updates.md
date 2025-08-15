---
title: Create an agent that can research and send personalized email updates
category: misc
source_lines: 28084-28175
line_count: 91
---

# Create an agent that can research and send personalized email updates
agent = Agent(
    name="Research Newsletter Agent",
    model=OpenAIChat(id="gpt-4o"),
    description="""You are an AI research specialist who creates and sends
    personalized email newsletters about the latest developments in artificial
    intelligence and technology.""",
    instructions=[
        """When given a prompt:,
        1. Extract the recipient's email address carefully. Look for the
        complete email in format 'user@domain.com'.,
        2. Research the latest AI developments using DuckDuckGo,
        3. Compose a concise, engaging email with:
           - A compelling subject line,
           - 3-4 key developments or news items,
           - Brief explanations of why they matter,
           - Links to sources,
        4. Format the content in a clean, readable way,
        5. Send the email using AWS SES. IMPORTANT: The receiver_email parameter
        must be the COMPLETE email address including the @ symbol and domain.""",
    ],
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
)

agent.print_response(
    "Research AI developments in healthcare from the past week with a focus on practical applications in clinical settings. Send the summary via email to johndoe@example.com"
)
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  {" "}

  <Step title="Set up AWS SES">
    ### Verify your email/domain: **For testing:** 1. Go to \[AWS SES

    Console]\([https://console.aws.amazon.com/ses/home](https://console.aws.amazon.com/ses/home)) > Verified Identities >
    Create Identity 2. Choose "Email Address" verification 3. Click verification
    link sent to your email **For production:** 1. Choose "Domain" and follow DNS
    verification steps 2. Add DKIM and SPF records to your domain's DNS **Note:**
    In sandbox mode, both sender and recipient emails must be verified.
  </Step>

  {" "}

  <Step title="Configure AWS credentials">
    ### Create IAM user: 1. Go to IAM Console > Users > Add User 2. Enable

    "Programmatic access" 3. Attach 'AmazonSESFullAccess' policy ### Set
    credentials (choose one method): **Method 1 - Using AWS CLI:** `bash aws
      configure ` **Method 2 - Environment variables:** `bash export
      AWS_ACCESS_KEY_ID=xxx export AWS_SECRET_ACCESS_KEY=xxx export
      AWS_DEFAULT_REGION=us-east-1 export OPENAI_API_KEY=xxx `
  </Step>

  {" "}

  <Step title="Install libraries">
    `bash pip install -U boto3 openai duckduckgo-search agno `
  </Step>

  {" "}

  <Step title="Run Agent">
    `bash python cookbook/tools/aws_ses_tools.py `
  </Step>

  <Step title="Troubleshooting">
    If emails aren't sending, check:

    * Both sender and recipient are verified (in sandbox mode)
    * AWS credentials are correctly configured
    * You're within sending limits
    * Your IAM user has correct SES permissions
    * Use SES Console's 'Send Test Email' feature to verify setup
  </Step>
</Steps>


