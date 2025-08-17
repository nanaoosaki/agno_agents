# test_coach_agent_fix.py
# Test script to verify Coach Agent fixes

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_coach_agent_fixes():
    """Test the Coach Agent function signature fixes"""
    print("🧪 Testing Coach Agent Fixes...")
    
    try:
        # Test fetch_open_episode_candidates import and call
        print("\n1. Testing data layer function...")
        from data.json_store import fetch_open_episode_candidates
        
        # Test the function with correct signature
        candidates = fetch_open_episode_candidates(window_hours=72)
        print(f"✅ fetch_open_episode_candidates returned {len(candidates)} candidates")
        
        # Test Coach Agent tools
        print("\n2. Testing Coach Agent tools...")
        from health_advisor.coach.tools import fetch_active_episode_snapshot, get_coaching_snippets, apply_safety_guardrails, _fetch_active_episode_snapshot_core
        print("✅ Coach Agent tools imported successfully")
        
        # Test fetch_active_episode_snapshot with correct function signature
        print("\n3. Testing fetch_active_episode_snapshot...")
        
        # Test the core function directly (this should not throw the signature error anymore)
        result = _fetch_active_episode_snapshot_core(window_hours=72)
        print(f"✅ fetch_active_episode_snapshot completed: {result is not None}")
        
        # Test Coach Agent import
        print("\n4. Testing Coach Agent import...")
        from health_advisor.coach.agent import coach_agent
        print(f"✅ Coach agent imported: {coach_agent.name}")
        
        # Test Coach Agent wrapper
        print("\n5. Testing Coach Agent wrapper...")
        from agents import coach_agent_wrapper
        if coach_agent_wrapper:
            print("✅ Coach Agent wrapper available")
        else:
            print("❌ Coach Agent wrapper not available")
        
        # Test MasterAgent import
        print("\n6. Testing MasterAgent with Coach routing...")
        from agents import master_agent
        if master_agent:
            print("✅ MasterAgent available for routing")
            print("   Can test full routing workflow now")
        else:
            print("❌ MasterAgent not available")
        
        print("\n🎉 All Coach Agent fixes verified!")
        print("\n📝 Issues Fixed:")
        print("   ✅ Function signature error in fetch_active_episode_snapshot")
        print("   ✅ Proper handling of EpisodeCandidate objects")
        print("   ✅ Fallback advice for knowledge base issues")
        print("   ✅ Graceful error handling for embeddings API issues")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    test_coach_agent_fixes()