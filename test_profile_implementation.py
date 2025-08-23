# test_profile_implementation.py
"""
Test script for Profile & Onboarding implementation
"""

def test_imports():
    """Test that all modules import correctly"""
    print("Testing imports...")
    
    try:
        # Test schema imports
        from profile_and_onboarding.schema import (
            UserProfile, ProfileEvent, Condition, Medication, Routine,
            OnboardConditionsResponse, OnboardMedicationsResponse, OnboardingPreviewResponse
        )
        print("✅ Schema imports successful")
    except Exception as e:
        print(f"❌ Schema imports failed: {e}")
        return False
    
    try:
        # Test storage imports
        from profile_and_onboarding.storage import (
            ProfileStorageInterface, JsonProfileStore, get_profile_store
        )
        print("✅ Storage imports successful")
    except Exception as e:
        print(f"❌ Storage imports failed: {e}")
        return False
    
    try:
        # Test workflow imports
        from profile_and_onboarding.onboarding_workflow import ProfileOnboardingWrapper
        print("✅ Workflow imports successful")
    except Exception as e:
        print(f"❌ Workflow imports failed: {e}")
        return False
        
    try:
        # Test updater imports
        from profile_and_onboarding.updater_agent import handle_profile_update, commit_profile_changes
        print("✅ Updater imports successful")
    except Exception as e:
        print(f"❌ Updater imports failed: {e}")
        return False
        
    return True

def test_storage_functionality():
    """Test basic storage functionality"""
    print("\nTesting storage functionality...")
    
    try:
        from profile_and_onboarding.storage import get_profile_store
        from profile_and_onboarding.schema import UserProfile, Condition, Medication
        
        # Get storage instance
        storage = get_profile_store()
        print("✅ Storage instance created")
        
        # Create test profile
        profile = UserProfile(
            user_id="test_user",
            conditions=[
                Condition(name="Test Condition", source="user")
            ],
            medications=[
                Medication(name="Test Med", type="other", source="user")
            ]
        )
        
        # Test save
        storage.save_profile(profile, source="test")
        print("✅ Profile saved")
        
        # Test retrieve
        retrieved = storage.get_profile("test_user")
        if retrieved and retrieved.user_id == "test_user":
            print("✅ Profile retrieved successfully")
            print(f"   - Conditions: {len(retrieved.conditions)}")
            print(f"   - Medications: {len(retrieved.medications)}")
        else:
            print("❌ Profile retrieval failed")
            return False
            
    except Exception as e:
        print(f"❌ Storage functionality test failed: {e}")
        return False
        
    return True

def test_router_integration():
    """Test router schema updates"""
    print("\nTesting router integration...")
    
    try:
        from health_advisor.router.schema import RouterDecision
        
        # Test creating RouterDecision with profile intents
        decision = RouterDecision(
            primary_intent="profile_update",
            secondary_intent=None,
            profile_action="update_profile",
            confidence=0.9,
            rationale="User wants to update medication"
        )
        print("✅ RouterDecision with profile intents created")
        print(f"   - Primary intent: {decision.primary_intent}")
        print(f"   - Profile action: {decision.profile_action}")
        
    except Exception as e:
        print(f"❌ Router integration test failed: {e}")
        return False
        
    return True

def test_agent_integration():
    """Test agent registry integration"""
    print("\nTesting agent integration...")
    
    try:
        from agents import AGENTS
        
        # Check if profile agent is in registry
        if "Profile & Onboarding" in AGENTS:
            print("✅ Profile & Onboarding agent in registry")
            
            # Test creating the agent
            agent = AGENTS["Profile & Onboarding"]
            print(f"   - Agent name: {agent.name}")
            print(f"   - Agent description: {agent.description}")
            
        else:
            print("❌ Profile & Onboarding agent not found in registry")
            print(f"Available agents: {list(AGENTS.keys())}")
            return False
            
    except Exception as e:
        print(f"❌ Agent integration test failed: {e}")
        return False
        
    return True

def run_all_tests():
    """Run all tests"""
    print("Running Profile & Onboarding Implementation Tests\n")
    
    tests = [
        ("Import Tests", test_imports),
        ("Storage Functionality", test_storage_functionality), 
        ("Router Integration", test_router_integration),
        ("Agent Integration", test_agent_integration)
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n{'='*60}")
        print(f"🔍 {test_name}")
        print('='*60)
        
        try:
            success = test_func()
            results.append((test_name, success))
        except Exception as e:
            print(f"❌ {test_name} failed with exception: {e}")
            results.append((test_name, False))
    
    # Print summary
    print(f"\n{'='*60}")
    print("📊 TEST SUMMARY")
    print('='*60)
    
    passed = 0
    for test_name, success in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status} - {test_name}")
        if success:
            passed += 1
    
    print(f"\n🎯 Results: {passed}/{len(results)} tests passed")
    
    if passed == len(results):
        print("🎉 All tests passed! Profile & Onboarding implementation is ready.")
    else:
        print("⚠️ Some tests failed. Please check the errors above.")
    
    return passed == len(results)

if __name__ == "__main__":
    run_all_tests()