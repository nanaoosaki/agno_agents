from typing import Iterator
from agno.agent import Agent, RunResponse
from agno.models.openai import OpenAIChat
from agno.utils.pprint import pprint_run_response
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API keys
openai_api_key = os.getenv("OPENAI_API_KEY")


agent = Agent(model=OpenAIChat(id="gpt-4o-mini", api_key=openai_api_key ))

# Run agent and return the response as a variable
response: RunResponse = agent.run("Tell me a 5 second short story about a robot")

# Print the response in markdown format
pprint_run_response(response, markdown=True)