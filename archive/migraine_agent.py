from agno.agent import Agent
from agno.embedder.openai import OpenAIEmbedder
from agno.knowledge.url import UrlKnowledge
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory
from agno.models.google import Gemini
from agno.storage.sqlite import SqliteStorage
from agno.tools.reasoning import ReasoningTools
from agno.vectordb.chroma import ChromaDb
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API keys
openai_api_key = os.getenv("OPENAI_API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Load migraine documentation in a knowledge base
knowledge = UrlKnowledge(
    urls=["https://img1.wsimg.com/blobby/go/06564960-dbf7-455b-9ea8-137ed61235b0/Migraine%20Headache%20Megahandout.pdf"],
    vector_db=ChromaDb(
        collection="migraine_docs",
        embedder=OpenAIEmbedder(id="text-embedding-ada-002", dimensions=1536, api_key=openai_api_key),
    )
)

# Memory for storing patient experiences and patterns
memory = Memory(
    # Use Gemini for creating and managing memories
    model=Gemini(id="gemini-2.0-flash", api_key=gemini_api_key),
    # Store memories in a SQLite database
    db=SqliteMemoryDb(table_name="migraine_memories", db_file="tmp/migraine_agent.db"),
    # Enable deletion and clearing for better memory management
    delete_memories=True,
    clear_memories=True,
)

# Store agent sessions in a SQLite database
storage = SqliteStorage(table_name="migraine_sessions", db_file="tmp/migraine_agent.db")

agent = Agent(
    name="Migraine Analysis Assistant",
    model=Gemini(id="gemini-2.0-flash", api_key=gemini_api_key),
    tools=[
        ReasoningTools(add_instructions=True),
    ],
    # User ID for storing memories
    user_id="migraine_patient",
    instructions=[
        "You are a specialized migraine analysis assistant.",
        "Search your knowledge base for medical information about migraines before answering.",
        "Analyze patient experiences stored in memory to identify patterns and triggers.",
        "Provide evidence-based insights about migraine triggers and mechanisms.",
        "Use tables to display data when appropriate.",
        "Include sources from both your knowledge base and patient memory in your responses.",
        "Be thorough in your analysis but present information clearly and accessibly.",
    ],
    knowledge=knowledge,
    memory=memory,
    storage=storage,
    # Let the Agent manage its memories
    enable_agentic_memory=True,
    add_datetime_to_instructions=True,
    add_history_to_messages=True,
    num_history_runs=3,
    markdown=True,
)

if __name__ == "__main__":
    # Load the knowledge base (set recreate=True for first run, then False)
    print("Loading migraine knowledge base...")
    agent.knowledge.load(recreate=True)
    
    # Store the patient's migraine experiences in memory
    print("Storing patient migraine experiences...")
    agent.print_response(
        """Store these migraine episodes in memory:

2025-08-07-1 – Left-temple headache after emotional trigger
Around noon, following a lunch conversation with Jack that brought up personal and corporate-life tensions, you experienced an emotional surge that triggered a mild (0.5–1) left-temple headache. You napped from 12:30–13:30, which likely provided some emotional and physiological recovery, and the pain remained low-level without progression during this period. No medication was taken for this episode, and it gradually blended into the next tension-related headache later in the afternoon.

2025-08-07-2 – Tension headache progressing toward migraine
Around 14:00, you noticed a persistent tension headache, initially mild but with a "tendency to develop into a migraine." Likely linked to residual emotional tension, you used essential oil along the hairline and applied Slumpus patches to both sides of the skull base, which provided partial relief. By 18:10, with pain beginning to rise, you took Ubrelvy (2nd dose this month), and within 30 minutes the headache was fully resolved. The total duration was about 4 hours 40 minutes, and early abortive therapy likely prevented a full migraine episode.""",
        stream=True,
        show_full_reasoning=True,
        stream_intermediate_steps=True,
    )
    
    print("\n" + "="*80 + "\n")
    
    # Analyze the migraine triggers
    agent.print_response(
        "What would you suggest the users to do to prevent migraines?",
        stream=True,
        show_full_reasoning=True,
        stream_intermediate_steps=True,
    )