from agno.agent import Agent
from agno.embedder.openai import OpenAIEmbedder
from agno.knowledge.url import UrlKnowledge
from agno.models.anthropic import Claude
from agno.storage.sqlite import SqliteStorage
from agno.vectordb.lancedb import LanceDb, SearchType
from agno.vectordb.chroma import ChromaDb  # ChromaDB for WINDOWS friendly storage
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Now you can access the OPENAI_API_KEY
api_key = os.getenv("OPENAI_API_KEY")

# Replace the LanceDb section with:

# Load Agno documentation in a knowledge base
# You can also use `https://docs.agno.com/llms-full.txt` for the full documentation
knowledge = UrlKnowledge(
    # urls=["https://docs.agno.com/introduction.md"],
    # urls=["https://nbviewer.org/format/script/github/openai/openai-cookbook/blob/main/examples/gpt-5/gpt-5_prompting_guide.ipynb"],
    # urls=["https://img1.wsimg.com/blobby/go/06564960-dbf7-455b-9ea8-137ed61235b0/Migraine%20Headache%20Megahandout.pdf"],
    urls=["https://cookbook.openai.com/examples/gpt-5/gpt-5_prompting_guide"],
    # vector_db=LanceDb(
    #     uri="./lancedb", # change to tmp/lancedb for local storage
    #     table_name="agno_docs",
    #     search_type=SearchType.hybrid,
    #     # Use OpenAI for embeddings
    #     embedder=OpenAIEmbedder(id="text-embedding-ada-002", dimensions=1536, api_key=api_key),
    # ),
    vector_db=ChromaDb(
        collection="agno_docs",
        embedder=OpenAIEmbedder(id="text-embedding-ada-002", dimensions=1536, api_key=api_key),
    )
)
# changed from text-embedding-3-small to text-embedding-ada-002 due to profile tiering issuess

# Store agent sessions in a SQLite database
storage = SqliteStorage(table_name="agent_sessions", db_file="tmp/agent.db")

agent = Agent(
    name="Agno Assist",
    model=Claude(id="claude-sonnet-4-20250514"),
    instructions=[
        "Search your knowledge before answering the question.",
        "Only include the output in your response. No other text.",
    ],
    knowledge=knowledge,
    storage=storage,
    add_datetime_to_instructions=True,
    # Add the chat history to the messages
    add_history_to_messages=True,
    # Number of history runs
    num_history_runs=3,
    markdown=True,
)

if __name__ == "__main__":
    # Load the knowledge base, comment out after first run
    # Set recreate to True to recreate the knowledge base if needed
    agent.knowledge.load(recreate=True) # change to False after first run
    agent.print_response("GPT-5 is more like a model improvement or a product improvement?", stream=True)