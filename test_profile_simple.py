# test_profile_simple.py
"""
Simple test script for Profile & Onboarding implementation
"""

def test_imports():
    """Test that all modules import correctly"""
    print("Testing imports...")
    
    try:
        # Test schema imports
        from profile_and_onboarding.schema import UserProfile, ProfileEvent
        print("PASS - Schema imports successful")
        return True
    except Exception as e:
        print(f"FAIL - Schema imports failed: {e}")
        return False

def test_storage():
    """Test storage functionality"""
    print("\nTesting storage...")
    
    try:
        from profile_and_onboarding.storage import get_profile_store
        from profile_and_onboarding.schema import UserProfile
        
        storage = get_profile_store()
        profile = UserProfile(user_id="test_user")
        storage.save_profile(profile, source="system")
        
        retrieved = storage.get_profile("test_user")
        if retrieved and retrieved.user_id == "test_user":
            print("PASS - Storage functionality working")
            return True
        else:
            print("FAIL - Profile retrieval failed")
            return False
            
    except Exception as e:
        print(f"FAIL - Storage test failed: {e}")
        return False

def test_router():
    """Test router integration"""
    print("\nTesting router integration...")
    
    try:
        from health_advisor.router.schema import RouterDecision
        
        decision = RouterDecision(
            primary_intent="profile_update",
            profile_action="update_profile", 
            confidence=0.9,
            rationale="Test decision"
        )
        print("PASS - Router integration working")
        return True
        
    except Exception as e:
        print(f"FAIL - Router test failed: {e}")
        return False

def main():
    print("Profile & Onboarding Implementation Tests")
    print("="*50)
    
    tests = [
        test_imports,
        test_storage,
        test_router
    ]
    
    passed = 0
    for test in tests:
        if test():
            passed += 1
    
    print(f"\nSummary: {passed}/{len(tests)} tests passed")
    return passed == len(tests)

if __name__ == "__main__":
    main()