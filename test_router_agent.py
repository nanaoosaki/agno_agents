# test_router_agent.py
# Test script for Router Agent and MasterAgent implementation

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_router_implementation():
    """Test Router Agent and MasterAgent functionality"""
    print("🧪 Testing Router Agent Implementation...")
    
    try:
        # Test schema import
        print("\n1. Testing schema import...")
        from health_advisor.router.schema import RouterDecision
        print("✅ RouterDecision schema imported successfully")
        
        # Test router agent import
        print("\n2. Testing router agent import...")
        from health_advisor.router.agent import router_agent
        print(f"✅ Router agent created: {router_agent.name}")
        print(f"   Model: {router_agent.model.id}")
        print(f"   Response Model: {router_agent.response_model.__name__}")
        print(f"   History enabled: {router_agent.add_history_to_messages}")
        
        # Test MasterAgent import
        print("\n3. Testing MasterAgent import...")
        from agents import AGENTS, master_agent
        if master_agent:
            print(f"✅ MasterAgent created: {master_agent.name}")
            print(f"   Description: {master_agent.description}")
        else:
            print("❌ MasterAgent not available")
            return False
        
        # Test agent registry
        print("\n4. Testing agent registry...")
        if "Health Companion (Auto-Router)" in AGENTS:
            companion = AGENTS["Health Companion (Auto-Router)"]
            print(f"✅ Health Companion in registry: {companion.name}")
        else:
            print("❌ Health Companion not found in registry")
        
        # Test available specialist agents
        print("\n5. Checking specialist agents availability...")
        specialists = {
            "Health Logger (v3)": "health logging",
            "Recall Agent": "historical data analysis", 
            "Coach Agent": "health guidance"
        }
        
        for agent_name, purpose in specialists.items():
            if agent_name in AGENTS:
                print(f"   ✅ {agent_name} available for {purpose}")
            else:
                print(f"   ⚠️ {agent_name} not available")
        
        # Test basic router decision (if API key available)
        print("\n6. Testing router decision...")
        if os.getenv("OPENAI_API_KEY"):
            try:
                # Test a simple routing decision
                test_prompts = [
                    "I have a headache",  # Should be "log"
                    "Show me my recent episodes",  # Should be "recall"
                    "What should I do for this pain?",  # Should be "coach"
                    "I have a migraine, what should I do?"  # Should be "log" + "coach" secondary
                ]
                
                for prompt in test_prompts:
                    print(f"\n   Testing: '{prompt}'")
                    try:
                        response = router_agent.run(prompt)
                        if hasattr(response, 'content') and isinstance(response.content, RouterDecision):
                            decision = response.content
                            print(f"   🧠 Primary: {decision.primary_intent}, Secondary: {decision.secondary_intent}")
                            print(f"   📊 Confidence: {decision.confidence:.2f}")
                            print(f"   💭 Rationale: {decision.rationale}")
                        else:
                            print(f"   ⚠️ Unexpected response format: {type(response.content)}")
                    except Exception as e:
                        print(f"   ❌ Router test failed: {e}")
                        
                print("\n   ✅ Router decision tests completed")
                
            except Exception as e:
                print(f"   ⚠️ Router API test failed: {e}")
        else:
            print("   ⚠️ No OPENAI_API_KEY - skipping live router tests")
        
        print("\n🎉 Router Agent implementation tests completed!")
        print("\n📝 Next steps:")
        print("   1. Start the Gradio app: python app.py")
        print("   2. Select 'Health Companion (Auto-Router)' as your agent")
        print("   3. Test different types of messages:")
        print("      • 'I have a headache' (logging)")
        print("      • 'Show me my history' (recall)")  
        print("      • 'What should I do?' (coaching)")
        print("      • 'I have a migraine, what should I do?' (multi-intent)")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    test_router_implementation()