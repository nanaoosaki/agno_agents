from agno.agent import Agent
from agno.models.openai import OpenAIChat
# load environment variables 
from dotenv import load_dotenv
load_dotenv()
import os

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini-2024-07-18", api_key=os.getenv("OPENAI_API_KEY")),
    add_state_in_messages=True,
    instructions="Users name is {user_name} and age is {age}",
)

# Sets the session state for the session with the id "user_1_session_1"
agent.print_response("What is my name?", session_id="user_1_session_1", user_id="user_1", session_state={"user_name": "John", "age": 30})

# Will load the session state from the session with the id "user_1_session_1"
agent.print_response("How old am I?", session_id="user_1_session_1", user_id="user_1")

# Sets the session state for the session with the id "user_2_session_1"
agent.print_response("What is my name?", session_id="user_2_session_1", user_id="user_2", session_state={"user_name": "Jane", "age": 25})

# Will load the session state from the session with the id "user_2_session_1"
agent.print_response("How old am I?", session_id="user_2_session_1", user_id="user_2")