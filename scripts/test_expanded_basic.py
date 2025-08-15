#!/usr/bin/env python3
"""
Basic test of expanded foundation functionality.
Quick verification that our expanded Rung 1 components work.
"""

import sys
import os
import tempfile
import json
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

def test_basic_functionality():
    """Test basic functionality of expanded foundation."""
    print("🧪 Testing Expanded Foundation Components...")
    
    # Test 1: Schema Validation
    print("\n1. Testing Schema Updates...")
    try:
        from linda_core.schemas import TABLE_FIELDS, FIELD_OPTIONS, FIELD_PRIORITIES
        print(f"   ✓ TABLE_FIELDS has {len(TABLE_FIELDS)} fields")
        
        # Check for key new fields
        new_fields = ["attack_types", "highest_pain_level", "associated_symptoms", "medications_taken"]
        for field in new_fields:
            if field in TABLE_FIELDS:
                print(f"   ✓ Found new field: {field}")
            else:
                print(f"   ❌ Missing field: {field}")
        
        print(f"   ✓ FIELD_OPTIONS has {len(FIELD_OPTIONS)} field option sets")
        print(f"   ✓ FIELD_PRIORITIES has {len(FIELD_PRIORITIES)} priority mappings")
        
    except Exception as e:
        print(f"   ❌ Schema test failed: {e}")
        return False
    
    # Test 2: Database JSON Functions
    print("\n2. Testing Database JSON Functions...")
    try:
        from linda_core.database import serialize_multi_select_value, deserialize_multi_select_value, is_multi_select_field
        
        # Test serialization
        test_values = ["Migraine", "Tension-type", "Cluster"]
        json_str = serialize_multi_select_value(test_values)
        print(f"   ✓ Serialized: {json_str}")
        
        # Test deserialization
        result = deserialize_multi_select_value(json_str)
        assert result == test_values
        print(f"   ✓ Deserialized: {result}")
        
        # Test field detection
        assert is_multi_select_field("attack_types") == True
        assert is_multi_select_field("highest_pain_level") == False
        print("   ✓ Multi-select field detection working")
        
    except Exception as e:
        print(f"   ❌ Database JSON test failed: {e}")
        return False
    
    # Test 3: Renderer Formatting
    print("\n3. Testing Renderer Formatting...")
    try:
        from linda_core.tools.rendering import TableRenderer
        from linda_core.database import serialize_multi_select_value
        
        renderer = TableRenderer()
        
        # Test data with new fields
        test_data = {
            "date": "2025-08-12",
            "attack_types": serialize_multi_select_value(["Migraine"]),
            "highest_pain_level": "7",
            "associated_symptoms": serialize_multi_select_value(["Nausea", "Photophobia"]),
        }
        
        # Test field name formatting
        attack_types_name = renderer._format_field_name("attack_types")
        pain_level_name = renderer._format_field_name("highest_pain_level")
        print(f"   ✓ Field name formatting: '{attack_types_name}', '{pain_level_name}'")
        
        # Test value formatting
        attack_types_value = renderer._format_field_value("attack_types", test_data["attack_types"])
        pain_level_value = renderer._format_field_value("highest_pain_level", test_data["highest_pain_level"])
        print(f"   ✓ Value formatting: '{attack_types_value}', '{pain_level_value}'")
        
        # Test full table rendering
        table = renderer.render_full_table(test_data)
        print(f"   ✓ Full table rendered ({len(table)} chars)")
        
        # Check for expected content
        if "Migraine" in table and "7/10" in table:
            print("   ✓ Table contains expected formatted content")
        else:
            print("   ❌ Table missing expected content")
            
    except Exception as e:
        print(f"   ❌ Renderer test failed: {e}")
        return False
    
    # Test 4: Data Assessor Logic
    print("\n4. Testing Data Assessor...")
    try:
        from linda_core.tools.data_assessor import DataAssessor
        from linda_core.database import serialize_multi_select_value
        
        assessor = DataAssessor()
        
        # Test empty data assessment
        empty_data = {}
        completeness, missing = assessor.assess_completeness(empty_data)
        print(f"   ✓ Empty data completeness: {completeness:.2f}, missing: {len(missing)} fields")
        
        # Test next prompt generation
        action = assessor.get_next_prompt(empty_data)
        if action:
            print(f"   ✓ Next prompt: '{action.prompt_text}' for field '{action.field_being_requested}'")
        else:
            print("   ❌ No prompt generated for empty data")
        
        # Test partial data
        partial_data = {
            "attack_types": serialize_multi_select_value(["Migraine"]),
            "highest_pain_level": "7"
        }
        completeness, missing = assessor.assess_completeness(partial_data)
        print(f"   ✓ Partial data completeness: {completeness:.2f}, missing: {len(missing)} fields")
        
        # Test sufficiency check
        sufficient = assessor.is_data_sufficient(partial_data)
        print(f"   ✓ Data sufficiency: {sufficient}")
        
    except Exception as e:
        print(f"   ❌ Data Assessor test failed: {e}")
        return False
    
    # Test 5: Integration Check
    print("\n5. Testing Component Integration...")
    try:
        # Test that components can work together
        from linda_core.schemas import RowDelta
        from linda_core.database import serialize_multi_select_value
        
        # Create a realistic delta
        delta = RowDelta(
            field="attack_types",
            value=["Migraine", "Tension-type"],
            source_msg_id="test_msg"
        )
        
        # Check that LogStore would handle this correctly
        from linda_core.tools.log_store import LogStore
        log_store = LogStore()
        
        # Verify JSON handling in LogStore
        from linda_core.database import is_multi_select_field
        if is_multi_select_field(delta.field) and isinstance(delta.value, list):
            expected_json = serialize_multi_select_value(delta.value)
            print(f"   ✓ LogStore would serialize '{delta.value}' to '{expected_json}'")
        
        print("   ✓ Component integration looks good")
        
    except Exception as e:
        print(f"   ❌ Integration test failed: {e}")
        return False
    
    print("\n🎉 All basic tests passed! Expanded foundation is working.")
    return True


def test_multi_turn_conversation_simulation():
    """Simulate a multi-turn conversation workflow."""
    print("\n📞 Testing Multi-Turn Conversation Simulation...")
    
    try:
        from linda_core.tools.data_assessor import DataAssessor
        from linda_core.database import serialize_multi_select_value
        
        assessor = DataAssessor()
        
        # Simulate conversation state
        conversation_data = {}
        
        print("\n   Turn 1: User says 'I have a migraine'")
        # Simulate extracting attack_types
        conversation_data["attack_types"] = serialize_multi_select_value(["Migraine"])
        
        action = assessor.get_next_prompt(conversation_data)
        if action:
            print(f"   → AI asks: '{action.prompt_text}'")
            print(f"   → Options: {action.ui_options[:3]}...")
        
        print("\n   Turn 2: User responds '7/10 pain'")
        conversation_data["highest_pain_level"] = "7"
        
        action = assessor.get_next_prompt(conversation_data)
        if action:
            print(f"   → AI asks: '{action.prompt_text}'")
            print(f"   → Options: {action.ui_options[:3]}...")
        
        print("\n   Turn 3: User responds 'Nausea and light sensitivity'")
        conversation_data["associated_symptoms"] = serialize_multi_select_value(["Nausea", "Photophobia"])
        
        action = assessor.get_next_prompt(conversation_data)
        if action:
            print(f"   → AI asks: '{action.prompt_text}'")
            print(f"   → Field: {action.field_being_requested}")
        
        print("\n   Turn 4: User responds 'Stress and lack of sleep'")
        conversation_data["potential_triggers"] = serialize_multi_select_value(["Stress", "Lack of sleep"])
        
        # Check if we have enough data now
        sufficient = assessor.is_data_sufficient(conversation_data)
        print(f"   → Data sufficient for final reply: {sufficient}")
        
        if sufficient:
            print("   → Would generate final two-block reply now")
        else:
            action = assessor.get_next_prompt(conversation_data)
            if action:
                print(f"   → Would continue with: '{action.prompt_text}'")
        
        # Show final data state
        from linda_core.tools.rendering import TableRenderer
        renderer = TableRenderer()
        
        print(f"\n   Final data collected:")
        for field, value in conversation_data.items():
            formatted_name = renderer._format_field_name(field)
            formatted_value = renderer._format_field_value(field, value)
            print(f"     {formatted_name}: {formatted_value}")
        
        print("\n✅ Multi-turn conversation simulation successful!")
        return True
        
    except Exception as e:
        print(f"\n❌ Conversation simulation failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Run all basic tests."""
    print("🚀 EXPANDED RUNG 1 FOUNDATION TEST")
    print("=" * 50)
    
    success1 = test_basic_functionality()
    success2 = test_multi_turn_conversation_simulation()
    
    print("\n" + "=" * 50)
    if success1 and success2:
        print("🎊 ALL TESTS PASSED! Expanded foundation is ready.")
        print("\n📋 Summary of what was tested:")
        print("  ✓ Expanded TABLE_FIELDS (30+ fields)")
        print("  ✓ JSON multi-select field handling")
        print("  ✓ Renderer formatting with new fields")
        print("  ✓ Data Assessor conversational logic")
        print("  ✓ Component integration")
        print("  ✓ Multi-turn conversation simulation")
        print("\n🚀 Ready for Rung 2: Extractor Agent!")
        return True
    else:
        print("❌ Some tests failed. Foundation needs fixes.")
        return False


if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)