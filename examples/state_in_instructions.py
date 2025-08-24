from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat
# load environment variables 
from dotenv import load_dotenv
load_dotenv()
import os


agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini-2024-07-18", api_key=os.getenv("OPENAI_API_KEY")   ),
    # Initialize the session state with a variable
    session_state={"user_name": "John"},
    # You can use variables from the session state in the instructions
    instructions="Users name is {user_name}",
    show_tool_calls=True,
    add_state_in_messages=True,
    markdown=True,
)

agent.print_response("What is my name?", stream=True)

# this can be used for checking the user static profiles 