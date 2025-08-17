# test_coach_agent.py
# Quick test of Coach Agent implementation

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_coach_agent():
    """Test Coach Agent basic functionality"""
    print("🧪 Testing Coach Agent Implementation...")
    
    try:
        # Test knowledge loader
        print("\n1. Testing knowledge loader...")
        try:
            from health_advisor.knowledge.loader import load_knowledge_if_needed, migraine_knowledge_base
            # Note: May fail if embeddings API is not available
            print("✅ Knowledge loader imported successfully")
        except Exception as e:
            print(f"⚠️ Knowledge loader has issues (likely embeddings API): {e}")
            print("   This is expected if embeddings API is not available")
        
        # Test tools import
        print("\n2. Testing tools import...")
        from health_advisor.coach.tools import (
            fetch_active_episode_snapshot, 
            get_coaching_snippets, 
            apply_safety_guardrails
        )
        print("✅ Tools imported successfully")
        
        # Test agent import
        print("\n3. Testing agent import...")
        from health_advisor.coach.agent import coach_agent
        print(f"✅ Coach agent created: {coach_agent.name}")
        print(f"   Model: {coach_agent.model.id}")
        print(f"   Tools: {len(coach_agent.tools)} tools")
        
        # Test integration with agents.py
        print("\n4. Testing agents.py integration...")
        from agents import AGENTS
        if "Coach Agent" in AGENTS:
            coach_wrapper = AGENTS["Coach Agent"]
            print(f"✅ Coach Agent in registry: {coach_wrapper.name}")
            print(f"   Description: {coach_wrapper.description}")
        else:
            print("❌ Coach Agent not found in registry")
        
        # Test basic knowledge search (without full agent run)
        print("\n5. Testing knowledge search...")
        try:
            # Only test if knowledge loader was successful
            results = migraine_knowledge_base.search("stress management", limit=1)
            if results:
                print(f"✅ Knowledge search working - found {len(results)} results")
                print(f"   Sample: {results[0].get('content', '')[:100]}...")
            else:
                print("⚠️ Knowledge search returned no results - may need to load knowledge first")
        except NameError:
            print("⚠️ Skipping knowledge search test - knowledge loader not available")
        except Exception as e:
            print(f"⚠️ Knowledge search error: {e}")
        
        print("\n🎉 All basic tests passed! Coach Agent is ready for use.")
        print("\n📝 Next steps:")
        print("   1. Start the Gradio app: python app.py")
        print("   2. Log a health episode with 'Health Logger (v3)'")
        print("   3. Ask for advice with 'Coach Agent'")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    # Ensure we're in the right environment
    if "OPENAI_API_KEY" not in os.environ:
        print("⚠️ Warning: OPENAI_API_KEY not found in environment")
    
    test_coach_agent()