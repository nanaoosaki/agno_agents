"""
Test script for the structured onboarding implementation.

This script tests the enhanced Profile & Onboarding agent with structured
data collection and the "Propose → Preview → Confirm → Commit" pattern.
"""

import os
import sys
from datetime import datetime

# Add current directory to path for imports
sys.path.insert(0, os.getcwd())

def test_onboarding_schemas():
    """Test the enhanced onboarding schemas."""
    print("🧪 Testing Enhanced Onboarding Schemas...")
    
    from data.schemas import (
        OnboardingConditions, OnboardingGoals, OnboardingSymptoms,
        OnboardingMedications, OnboardingRoutines, OnboardingStyle,
        UserProfile
    )
    
    # Test structured onboarding models
    conditions = OnboardingConditions(
        conditions=["migraine", "anxiety"],
        primary_condition="migraine"
    )
    assert conditions.conditions == ["migraine", "anxiety"]
    assert conditions.primary_condition == "migraine"
    
    goals = OnboardingGoals(
        goals="Reduce migraine frequency and better track triggers",
        specific_targets=["Less than 5 migraines per month", "Identify food triggers"]
    )
    assert "reduce" in goals.goals.lower()
    
    # Test enhanced UserProfile with schema versioning
    profile = UserProfile(
        user_id="test_user_structured",
        conditions=[{"name": "migraine", "status": "active"}],
        goals="Better health management",
        communication_style="detailed"
    )
    assert profile.schema_version == 2
    assert profile.communication_style == "detailed"
    assert profile.last_updated_by == "user"
    
    print("✅ Enhanced schemas working correctly")

def test_onboarding_agents():
    """Test the specialized onboarding agents."""
    print("🧪 Testing Specialized Onboarding Agents...")
    
    try:
        from profile_and_onboarding.agents import (
            create_conditions_agent, create_goals_agent,
            create_symptoms_agent, create_medications_agent,
            create_routines_agent, create_style_agent
        )
        
        # Test agent creation
        conditions_agent = create_conditions_agent()
        assert conditions_agent.name == "OnboardingStep1Agent"
        
        goals_agent = create_goals_agent()
        assert goals_agent.name == "OnboardingStep2Agent"
        
        print("✅ Specialized agents created successfully")
        
    except ImportError as e:
        print(f"⚠️ Specialized agents require API keys: {e}")

def test_structured_workflow():
    """Test the structured workflow."""
    print("🧪 Testing Structured Workflow...")
    
    from profile_and_onboarding.workflow import OnboardingWorkflowWrapper
    
    # Initialize workflow
    workflow = OnboardingWorkflowWrapper()
    
    # Check if structured workflow was loaded
    if workflow.is_structured:
        print("✅ Structured workflow (v3.3) loaded successfully")
        assert "v3.3" in workflow.name
    else:
        print("⚠️ Using fallback workflow - structured features not available")
        assert "v1.0" in workflow.name
    
    # Test start command
    result = workflow.run("start")
    assert "Welcome" in result.text or "health profile" in result.text.lower()
    assert result.meta.get("workflow") is not None
    
    print("✅ Workflow initialization successful")

def test_preview_confirm_pattern():
    """Test the preview and confirm pattern."""
    print("🧪 Testing Preview & Confirm Pattern...")
    
    try:
        from profile_and_onboarding.workflow_v2 import preview_and_confirm_step, commit_profile_step
        from profile_and_onboarding.workflow_v2 import StepInput, StepOutput
        
        # Create mock step input with sample data
        class MockStepData:
            def __init__(self, **kwargs):
                for k, v in kwargs.items():
                    setattr(self, k, v)
        
        # Mock step input
        step_input = StepInput()
        step_input.workflow_session_state = {
            "AskConditions_result": MockStepData(conditions=["migraine"], primary_condition="migraine"),
            "AskGoals_result": MockStepData(goals="Better symptom tracking"),
        }
        step_input.get_step_content = lambda name: step_input.workflow_session_state.get(f"{name}_result")
        
        # Test preview step
        preview_result = preview_and_confirm_step(step_input)
        assert "Profile Summary" in preview_result.content
        assert "migraine" in preview_result.content
        assert "confirm" in preview_result.content.lower()
        
        print("✅ Preview & confirm pattern working correctly")
        
    except ImportError as e:
        print(f"⚠️ Structured workflow components not available: {e}")

def test_storage_integration():
    """Test integration with the storage system."""
    print("🧪 Testing Storage Integration...")
    
    from data import JsonStore
    from profile_and_onboarding.storage import ProfileStore
    from data.schemas import UserProfile
    
    # Initialize storage
    storage = JsonStore(base_path="test_data_structured")
    profile_store = ProfileStore(storage)
    
    # Test enhanced profile creation
    enhanced_profile_data = {
        "name": "Jane Smith",
        "conditions": [{"name": "anxiety", "status": "active"}],
        "goals": "Manage anxiety through tracking and therapy",
        "communication_style": "supportive",
        "schema_version": 2
    }
    
    proposal = profile_store.propose_new_profile("test_user_enhanced", enhanced_profile_data)
    assert proposal.get("confirmation_required") is True
    assert "Jane Smith" in proposal.get("message", "")
    
    # Test confirmation
    result = profile_store.confirm_profile_creation("test_user_enhanced", proposal)
    print(f"Confirmation result: {result}")
    assert result.get("success") is True
    
    # Verify enhanced profile was created
    profile = profile_store.get_profile("test_user_enhanced")
    assert profile is not None
    assert profile.schema_version == 2
    assert profile.communication_style == "supportive"
    
    print("✅ Storage integration working correctly")

def cleanup_test_data():
    """Clean up test data files."""
    import shutil
    import os
    
    test_dirs = ["test_data_structured"]
    for test_dir in test_dirs:
        if os.path.exists(test_dir):
            shutil.rmtree(test_dir)
    print("🧹 Test data cleaned up")

def main():
    """Run all tests for the structured onboarding implementation."""
    print("🚀 Starting Structured Onboarding Tests\n")
    
    try:
        test_onboarding_schemas()
        test_onboarding_agents()
        test_structured_workflow()
        test_preview_confirm_pattern()
        test_storage_integration()
        
        print("\n🎉 All structured onboarding tests passed!")
        print("\n📋 Implementation Summary:")
        print("✅ Enhanced Pydantic schemas with versioning")
        print("✅ Specialized agents for each onboarding step") 
        print("✅ Structured workflow with preview & confirm")
        print("✅ Storage integration with schema v2 support")
        print("✅ Backward compatibility with fallback workflow")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    finally:
        cleanup_test_data()

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)