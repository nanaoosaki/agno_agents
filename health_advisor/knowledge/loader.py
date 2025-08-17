# health_advisor/knowledge/loader.py
# Following docs/agno/knowledge/markdown_knowledge_base.md pattern
# Using ChromaDB for Windows compatibility (following level_2_agent.py pattern)

from pathlib import Path
from agno.knowledge.markdown import MarkdownKnowledgeBase
from agno.vectordb.chroma import ChromaDb  # ChromaDB for WINDOWS friendly storage
from agno.embedder.openai import OpenAIEmbedder
import os

# Define paths relative to the project root
PROJECT_ROOT = Path(__file__).parent.parent.parent  # AI_agents_agno/
HANDOUT_PATH = PROJECT_ROOT / "knowledge" / "migraine_handout.md"
CHROMA_PATH = PROJECT_ROOT / "data" / "chroma_coach"

# Configure embedder following level_2_agent.py pattern
api_key = os.getenv("OPENAI_API_KEY")
embedder = OpenAIEmbedder(
    id="text-embedding-ada-002",
    dimensions=1536,
    api_key=api_key
)

# Initialize migraine_knowledge_base as None for lazy loading
migraine_knowledge_base = None

def get_migraine_knowledge_base():
    """Get or create the migraine knowledge base using ChromaDB (Windows-friendly)."""
    global migraine_knowledge_base
    
    if migraine_knowledge_base is None:
        try:
            # Use ChromaDB following level_2_agent.py pattern - Windows friendly
            print("🔄 Initializing ChromaDB knowledge base...")
            migraine_knowledge_base = MarkdownKnowledgeBase(
                path=HANDOUT_PATH,
                embedder=embedder,
                vector_db=ChromaDb(
                    collection="migraine_handout",
                    embedder=embedder
                ),
            )
            print("✅ ChromaDB knowledge base created successfully")
            
            # Automatically load the knowledge base on first access
            try:
                print("🔄 Loading migraine handout into ChromaDB...")
                migraine_knowledge_base.load(recreate=False)
                print("✅ Migraine handout loaded into ChromaDB")
            except Exception as load_error:
                print(f"⚠️ Failed to auto-load knowledge: {load_error}")
                print("   Knowledge base created but content not loaded")
            
            return migraine_knowledge_base
        except Exception as e:
            print(f"❌ ChromaDB knowledge base initialization failed: {e}")
            print("🔄 Attempting fallback to simple file-based knowledge...")
            
            try:
                # Fallback: Create a simpler knowledge base without vector database
                migraine_knowledge_base = MarkdownKnowledgeBase(
                    path=HANDOUT_PATH,
                    embedder=embedder
                    # No vector_db - will use default in-memory or simpler storage
                )
                print("✅ Fallback knowledge base created successfully")
                return migraine_knowledge_base
            except Exception as fallback_error:
                print(f"❌ Fallback knowledge base also failed: {fallback_error}")
                return None
    
    return migraine_knowledge_base

def load_knowledge_if_needed():
    """Function to load the handout into the vector database."""
    knowledge_base = get_migraine_knowledge_base()
    if knowledge_base:
        try:
            print("🔄 Loading migraine handout into vector database...")
            knowledge_base.load(recreate=False)  # Don't recreate unless needed
            print("✅ Knowledge base loaded successfully.")
        except Exception as e:
            print(f"⚠️ Knowledge base loading error: {e}")
    else:
        print("❌ Knowledge base not available.")

def recreate_knowledge_base():
    """Force recreation of the knowledge base with ChromaDB and text-embedding-ada-002."""
    knowledge_base = get_migraine_knowledge_base()
    if knowledge_base:
        try:
            print("🔄 Recreating knowledge base with text-embedding-ada-002 and ChromaDB...")
            knowledge_base.load(recreate=True)
            print("✅ Knowledge base recreated successfully with ada-002 embeddings.")
        except Exception as e:
            print(f"❌ Knowledge base recreation failed: {e}")
    else:
        print("❌ Knowledge base not available for recreation.")

if __name__ == "__main__":
    load_knowledge_if_needed()