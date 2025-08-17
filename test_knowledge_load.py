# test_knowledge_load.py
# Test script to force load the knowledge base with the corrected file path

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_knowledge_loading():
    """Test loading the knowledge base with the corrected path"""
    print("🧪 Testing Knowledge Base Loading with Corrected Path...")
    
    try:
        print("\n1. Testing knowledge loader...")
        from health_advisor.knowledge.loader import get_migraine_knowledge_base, HANDOUT_PATH
        
        print(f"📁 Expected handout path: {HANDOUT_PATH}")
        print(f"📋 File exists: {HANDOUT_PATH.exists()}")
        
        if not HANDOUT_PATH.exists():
            print("❌ Handout file not found at expected path")
            return False
        
        print("\n2. Attempting to load knowledge base...")
        knowledge_base = get_migraine_knowledge_base()
        
        if knowledge_base is None:
            print("❌ Knowledge base failed to load")
            return False
        
        print("✅ Knowledge base loaded successfully")
        
        print("\n3. Loading/indexing the document...")
        try:
            # Force load the document into the vector database
            knowledge_base.load(recreate=True)
            print("✅ Document loaded and indexed successfully")
        except Exception as e:
            print(f"❌ Document loading failed: {e}")
            return False
        
        print("\n4. Testing search functionality...")
        try:
            # Try different search patterns based on Agno version
            try:
                results = knowledge_base.search("stress management", limit=2)
            except TypeError:
                # Fallback if limit parameter not supported
                results = knowledge_base.search("stress management")
                if isinstance(results, list) and len(results) > 2:
                    results = results[:2]
            
            if results:
                print(f"✅ Search successful - found {len(results)} results")
                for i, result in enumerate(results[:1], 1):
                    # Handle different result formats
                    if hasattr(result, 'content'):
                        content = result.content[:150]
                    elif isinstance(result, dict):
                        content = result.get("content", "")[:150]
                    else:
                        content = str(result)[:150]
                    print(f"   Result {i}: {content}...")
            else:
                print("⚠️ Search returned no results")
        except Exception as e:
            print(f"❌ Search failed: {e}")
            return False
        
        print("\n🎉 Knowledge base setup completed successfully!")
        print("📝 The Coach Agent should now be able to access real migraine guidance.")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    test_knowledge_loading()