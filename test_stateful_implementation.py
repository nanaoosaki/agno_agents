"""
Test script for the stateful health companion implementation.

This script tests the core functionality of the new architecture including
storage, profiles, and the onboarding workflow.
"""

import os
import sys
from datetime import datetime

# Add current directory to path for imports
sys.path.insert(0, os.getcwd())

def test_core_primitives():
    """Test core ontology and time utilities."""
    print("🧪 Testing Core Primitives...")
    
    from core.ontology import normalize_condition, get_condition_family, normalize_severity
    from core.timeutils import parse_date_range, format_health_date
    
    # Test condition normalization
    assert normalize_condition("headache") == "migraine"
    assert normalize_condition("back pain") == "back_pain"
    assert get_condition_family("migraine") == "neurological"
    
    # Test severity normalization
    assert normalize_severity("mild") == 2
    assert normalize_severity("7") == 7
    
    # Test time parsing
    start, end = parse_date_range("yesterday")
    assert isinstance(start, datetime)
    assert isinstance(end, datetime)
    
    print("✅ Core primitives working correctly")

def test_storage_system():
    """Test the storage abstraction and JSON implementation."""
    print("🧪 Testing Storage System...")
    
    from data import JsonStore
    from data.schemas.user_profile import UserProfile, MedicalCondition
    
    # Initialize storage
    storage = JsonStore(base_path="test_data")
    
    # Test episode creation
    episode_id = storage.create_episode({
        "user_id": "test_user",
        "condition": "migraine",
        "severity": 7,
        "start_time": datetime.now().isoformat()
    })
    
    assert episode_id is not None
    
    # Test episode retrieval
    episode = storage.get_episode(episode_id)
    assert episode is not None
    assert episode["condition"] == "migraine"
    
    # Test user profile
    test_profile = UserProfile(
        user_id="test_user",
        name="Test User",
        conditions=[
            MedicalCondition(
                name="migraine",
                display_name="Migraine",
                family="neurological"
            )
        ]
    )
    
    success = storage.create_user_profile("test_user", test_profile.to_dict())
    assert success is True
    
    retrieved_profile = storage.get_user_profile("test_user")
    assert retrieved_profile is not None
    assert retrieved_profile["name"] == "Test User"
    
    print("✅ Storage system working correctly")

def test_profile_store():
    """Test the profile store with confirmation patterns."""
    print("🧪 Testing Profile Store...")
    
    from data import JsonStore
    from profile_and_onboarding.storage import ProfileStore
    
    storage = JsonStore(base_path="test_data")
    profile_store = ProfileStore(storage)
    
    # Test profile proposal
    proposal = profile_store.propose_new_profile("test_user_2", {
        "name": "Jane Doe",
        "conditions": [
            {
                "name": "anxiety",
                "display_name": "Anxiety",
                "family": "mental_health"
            }
        ]
    })
    
    assert proposal.get("confirmation_required") is True
    assert "Jane Doe" in proposal.get("message", "")
    
    # Test profile confirmation
    result = profile_store.confirm_profile_creation("test_user_2", proposal)
    assert result.get("success") is True
    
    # Verify profile was created
    profile = profile_store.get_profile("test_user_2")
    assert profile is not None
    assert profile.name == "Jane Doe"
    
    print("✅ Profile store working correctly")

def test_onboarding_workflow():
    """Test the onboarding workflow wrapper."""
    print("🧪 Testing Onboarding Workflow...")
    
    from profile_and_onboarding.workflow import OnboardingWorkflowWrapper
    
    # Initialize workflow
    workflow = OnboardingWorkflowWrapper()
    
    # Test start command
    result = workflow.run("start")
    assert "Welcome" in result.text
    assert result.meta.get("workflow") == "Onboarding"
    
    # Test basic user input
    result = workflow.run("My name is John Smith, I'm 35 years old")
    assert result.text is not None
    assert len(result.text) > 0
    
    print("✅ Onboarding workflow initialized correctly")

def cleanup_test_data():
    """Clean up test data files."""
    import shutil
    import os
    
    test_data_path = "test_data"
    if os.path.exists(test_data_path):
        shutil.rmtree(test_data_path)
    print("🧹 Test data cleaned up")

def main():
    """Run all tests."""
    print("🚀 Starting Stateful Health Companion Tests\n")
    
    try:
        test_core_primitives()
        test_storage_system()
        test_profile_store()
        test_onboarding_workflow()
        
        print("\n🎉 All tests passed! The stateful health companion architecture is working correctly.")
        
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    finally:
        cleanup_test_data()
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)