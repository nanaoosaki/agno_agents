---
title: Example toolkit for handling emails
category: misc
source_lines: 2911-2960
line_count: 49
---

# Example toolkit for handling emails
class EmailTools(Toolkit):
    def __init__(self, *args, **kwargs):
        super().__init__(
            name="EmailTools", tools=[self.send_email, self.get_emails], *args, **kwargs
        )

    def send_email(self, subject: str, body: str, to_address: str) -> str:
        """Send an email to the given address with the given subject and body.

        Args:
            subject (str): The subject of the email.
            body (str): The body of the email.
            to_address (str): The address to send the email to.
        """
        return f"Sent email to {to_address} with subject {subject} and body {body}"

    def get_emails(self, date_from: str, date_to: str) -> str:
        """Get all emails between the given dates.

        Args:
            date_from (str): The start date.
            date_to (str): The end date.
        """
        return [
            {
                "subject": "Hello",
                "body": "Hello, world!",
                "to_address": "test@test.com",
                "date": date_from,
            },
            {
                "subject": "Random other email",
                "body": "This is a random other email",
                "to_address": "john@doe.com",
                "date": date_to,
            },
        ]


agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[EmailTools(), UserControlFlowTools()],
    markdown=True,
    debug_mode=True,
)

run_response = agent.run("Send an email with the body 'How is it going in Tokyo?'")

