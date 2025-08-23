# test_direct_profile.py
"""
Test profile functionality directly without loading agents.py
"""

def test_onboarding_workflow():
    try:
        from profile_and_onboarding.onboarding_workflow import ProfileOnboardingWrapper
        
        print("Creating ProfileOnboardingWrapper...")
        wrapper = ProfileOnboardingWrapper()
        print(f"Agent name: {wrapper.name}")
        print(f"Agent description: {wrapper.description}")
        
        # Test basic run method
        result = wrapper.run("Hello, I'm new here", session_id="test_user")
        print(f"Response type: {type(result)}")
        if isinstance(result, dict) and "content" in result:
            print(f"Response content preview: {result['content'][:100]}...")
        
        print("ProfileOnboardingWrapper test PASSED")
        return True
        
    except Exception as e:
        print(f"ProfileOnboardingWrapper test FAILED: {e}")
        return False

def test_updater_agent():
    try:
        from profile_and_onboarding.updater_agent import handle_profile_update
        
        print("\nTesting profile update handler...")
        result = handle_profile_update("I need to add a new medication", "test_user")
        print(f"Update result type: {type(result)}")
        if isinstance(result, dict):
            print("Profile update handler test PASSED")
        else:
            print("Profile update handler test FAILED - wrong return type")
            return False
        
        return True
        
    except Exception as e:
        print(f"Profile update handler test FAILED: {e}")
        return False

def main():
    print("Direct Profile System Tests")
    print("="*40)
    
    tests = [
        test_onboarding_workflow,
        test_updater_agent
    ]
    
    passed = 0
    for test in tests:
        if test():
            passed += 1
    
    print(f"\nResults: {passed}/{len(tests)} tests passed")
    
if __name__ == "__main__":
    main()