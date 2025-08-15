from typing import Iterator
from agno.agent import Agent, RunResponseEvent
from agno.models.openai import OpenAIChat
from agno.utils.pprint import pprint_run_response
# load environment variables
from dotenv import load_dotenv
load_dotenv()
import os

agent = Agent(model=OpenAIChat(id="gpt-4o-mini-2024-07-18", api_key=os.getenv("OPENAI_API_KEY")))

# Run agent and return the response as a stream
response_stream: Iterator[RunResponseEvent] = agent.run(
    "Tell me a 5 second short story about a lion",
    stream=True,
    stream_intermediate_steps=True #doesnt' work for gpt-4o-mini
)

# Print the response stream in markdown format
pprint_run_response(response_stream, markdown=True)