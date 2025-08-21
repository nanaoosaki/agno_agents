# Remove the tmp db file before running the script
import os

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage
# load enviroinment variables
from dotenv import load_dotenv
load_dotenv()
import os

os.remove("tmp/data.db")

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini-2024-07-18", api_key=os.getenv("OPENAI_API_KEY")),
    user_id="user_1",
    storage=SqliteStorage(table_name="agent_sessions_new", db_file="tmp/data.db"),
    search_previous_sessions_history=True,  # allow searching previous sessions
    num_history_sessions=2,  # only include the last 2 sessions in the search to avoid context length issues
    show_tool_calls=True,
)

session_1_id = "session_1_id"
session_2_id = "session_2_id"
session_3_id = "session_3_id"
session_4_id = "session_4_id"
session_5_id = "session_5_id"

agent.print_response("What is the capital of South Africa?", session_id=session_1_id)
agent.print_response("What is the capital of China?", session_id=session_2_id)
agent.print_response("What is the capital of France?", session_id=session_3_id)
agent.print_response("What is the capital of Japan?", session_id=session_4_id)
agent.print_response(
    "What did I discuss in my previous conversations?", session_id=session_5_id
)  # It should only include the last 2 sessions

# To enable fetching messages from the last N sessions, you need to use the following flags:
# search_previous_sessions_history: Set this to True to allow searching through previous sessions.
# num_history_sessions: Specify the number of past sessions to include in the search. In this example, it is set to 2 to include only the last 2 sessions. It’s advisable to keep this number to 2 or 3 for now, as a larger number might fill up the context length of the model, potentially leading to performance issues.
# These flags help manage the context length and ensure that only relevant session history is included in the conversation.