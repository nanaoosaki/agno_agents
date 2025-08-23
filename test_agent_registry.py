# test_agent_registry.py
"""
Test if the profile agents are properly registered
"""

def test_agent_registry():
    try:
        from agents import AGENTS
        
        print("Available agents:")
        for name in AGENTS.keys():
            print(f"  - {name}")
        
        if "Profile & Onboarding" in AGENTS:
            print("\nProfile & Onboarding agent found!")
            agent = AGENTS["Profile & Onboarding"] 
            print(f"Agent name: {agent.name}")
            print(f"Agent description: {agent.description}")
            return True
        else:
            print("\nProfile & Onboarding agent NOT found in registry")
            return False
            
    except Exception as e:
        print(f"Error testing agent registry: {e}")
        return False

if __name__ == "__main__":
    test_agent_registry()