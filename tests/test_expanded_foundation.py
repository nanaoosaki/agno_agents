#!/usr/bin/env python3
"""
Test the expanded Rung 1 foundation with MigraineBuddy data integration.
Tests multi-select JSON fields, conversational data capture, and expanded rendering.
"""

import pytest
import sys
import os
import tempfile
import json
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from linda_core.database import (
    init_database, get_db_session, write_day_row, read_day_rows,
    serialize_multi_select_value, deserialize_multi_select_value, is_multi_select_field
)
from linda_core.schemas import RowDelta, TABLE_FIELDS
from linda_core.tools.log_store import LogStore
from linda_core.tools.rendering import TableRenderer
from linda_core.tools.counters import CounterCalculator
from linda_core.tools.data_assessor import DataAssessor


class TestExpandedFoundation:
    """Test expanded Linda foundation with MigraineBuddy integration."""
    
    @pytest.fixture(autouse=True)
    def setup_db(self):
        """Set up test database for each test."""
        # Create temporary database
        self.db_fd, self.db_path = tempfile.mkstemp(suffix='.db')
        os.environ['DATABASE_URL'] = f'sqlite:///{self.db_path}'
        
        # Initialize database
        init_database()
        
        yield
        
        # Cleanup
        os.close(self.db_fd)
        os.unlink(self.db_path)
    
    def test_multi_select_serialization(self):
        """Test JSON serialization/deserialization for multi-select fields."""
        # Test data
        test_values = ["Migraine", "Tension-type", "Cluster"]
        
        # Serialize
        json_str = serialize_multi_select_value(test_values)
        assert isinstance(json_str, str)
        assert "Migraine" in json_str
        
        # Deserialize
        result = deserialize_multi_select_value(json_str)
        assert result == test_values
        
        # Test empty/invalid cases
        assert deserialize_multi_select_value("") == []
        assert deserialize_multi_select_value("invalid json") == []
        assert deserialize_multi_select_value(None) == []
    
    def test_multi_select_field_detection(self):
        """Test detection of multi-select fields."""
        # New multi-select fields should be detected
        assert is_multi_select_field("attack_types") == True
        assert is_multi_select_field("associated_symptoms") == True
        assert is_multi_select_field("medications_taken") == True
        
        # Legacy/single fields should not be detected
        assert is_multi_select_field("highest_pain_level") == False
        assert is_multi_select_field("date") == False
        assert is_multi_select_field("ubrelvy_mg_brand") == False
    
    def test_expanded_table_fields(self):
        """Test that TABLE_FIELDS includes all new MigraineBuddy fields."""
        # Check for key new fields
        new_fields = [
            "attack_types", "highest_pain_level", "associated_symptoms",
            "potential_triggers", "medications_taken", "relief_methods_tried",
            "activity_impact", "location_at_attack_start"
        ]
        
        for field in new_fields:
            assert field in TABLE_FIELDS, f"Missing field: {field}"
        
        # Should have significantly more fields now
        assert len(TABLE_FIELDS) > 30, f"Expected >30 fields, got {len(TABLE_FIELDS)}"
    
    def test_json_field_storage_and_retrieval(self):
        """Test storing and retrieving multi-select data."""
        test_date = "2025-08-12"
        source_msg_id = "test_msg_001"
        
        # Store multi-select attack types
        attack_types = ["Migraine", "Tension-type"]
        json_value = serialize_multi_select_value(attack_types)
        
        write_day_row(test_date, "attack_types", json_value, source_msg_id)
        
        # Store single-select pain level
        write_day_row(test_date, "highest_pain_level", "7", source_msg_id)
        
        # Retrieve and verify
        day_data = read_day_rows(test_date)
        
        assert "attack_types" in day_data
        assert "highest_pain_level" in day_data
        
        # Verify multi-select deserialization
        retrieved_types = deserialize_multi_select_value(day_data["attack_types"])
        assert retrieved_types == attack_types
        
        # Verify single value
        assert day_data["highest_pain_level"] == "7"
    
    def test_log_store_with_json_fields(self):
        """Test LogStore handling of JSON multi-select fields."""
        log_store = LogStore()
        test_date = "2025-08-12"
        
        # Create deltas with mixed field types
        deltas = [
            RowDelta(field="attack_types", value=["Migraine", "Cluster"], source_msg_id="msg1"),
            RowDelta(field="highest_pain_level", value="8", source_msg_id="msg1"),
            RowDelta(field="associated_symptoms", value=["Nausea", "Photophobia"], source_msg_id="msg1"),
        ]
        
        # Write through LogStore (it should handle JSON serialization)
        log_store.write_rows(deltas, test_date)
        
        # Read back
        day_data = log_store.read_rows(test_date)
        
        # Verify data
        assert "attack_types" in day_data
        assert "highest_pain_level" in day_data
        assert "associated_symptoms" in day_data
        
        # The LogStore should have serialized lists to JSON strings
        assert isinstance(day_data["attack_types"], str)
        assert isinstance(day_data["highest_pain_level"], str)
    
    def test_expanded_renderer_formatting(self):
        """Test TableRenderer with new fields and JSON formatting."""
        renderer = TableRenderer()
        
        # Test data with both legacy and new fields
        test_data = {
            "date": "2025-08-12",
            "attack_types": serialize_multi_select_value(["Migraine", "Tension-type"]),
            "highest_pain_level": "7",
            "associated_symptoms": serialize_multi_select_value(["Nausea", "Photophobia", "Phonophobia"]),
            "medications_taken": serialize_multi_select_value(["Ubrelvy", "Ibuprofen"]),
            "ubrelvy_mg_brand": "50mg Ubrelvy",  # Legacy field
        }
        
        # Render full table
        table = renderer.render_full_table(test_data)
        
        # Check that table contains properly formatted fields
        assert "Attack type(s) [REQUIRED]" in table
        assert "Migraine, Tension-type" in table  # JSON should be formatted as comma-separated
        assert "7/10 (Very severe)" in table  # Pain level should be formatted with descriptor
        assert "Nausea, Photophobia, Phonophobia" in table
        assert "Ubrelvy, Ibuprofen" in table
        
        # Check field order preservation
        lines = table.split('\n')
        field_lines = [line for line in lines if '|' in line and not line.startswith('|---')]
        
        # Date should come first
        assert "Date" in field_lines[1]
        # Attack types should come after basic fields but before legacy pain fields
        attack_types_idx = next(i for i, line in enumerate(field_lines) if "Attack type(s)" in line)
        left_pain_idx = next(i for i, line in enumerate(field_lines) if "Left-headache pain" in line)
        assert attack_types_idx < left_pain_idx
    
    def test_expanded_counters_with_json(self):
        """Test CounterCalculator with new JSON fields."""
        calculator = CounterCalculator()
        test_date = "2025-08-12"
        
        # Create test data spanning multiple days with both legacy and new format
        log_store = LogStore()
        
        # Day 1: Legacy format
        deltas_day1 = [
            RowDelta(field="ubrelvy_mg_brand", value="50mg", source_msg_id="msg1"),
            RowDelta(field="acetaminophen_mg_brand", value="500mg", source_msg_id="msg1"),
        ]
        log_store.write_rows(deltas_day1, "2025-08-10")
        
        # Day 2: New format
        deltas_day2 = [
            RowDelta(field="medications_taken", value=["Ubrelvy", "Acetaminophen"], source_msg_id="msg2"),
            RowDelta(field="potential_triggers", value=["Stress", "Aged cheese"], source_msg_id="msg2"),
        ]
        log_store.write_rows(deltas_day2, "2025-08-11")
        
        # Day 3: Mixed
        deltas_day3 = [
            RowDelta(field="medications_taken", value=["Ubrelvy"], source_msg_id="msg3"),
            RowDelta(field="ubrelvy_mg_brand", value="100mg", source_msg_id="msg3"),  # Should not double-count
        ]
        log_store.write_rows(deltas_day3, test_date)
        
        # Calculate counters
        counters = calculator.compute_counters(test_date)
        
        # Should count Ubrelvy from both legacy and new fields
        assert counters.ubrelvy_30d >= 2  # At least day 2 and day 3
        assert counters.acetaminophen_30d >= 1  # At least day 2
        
        # Test new analysis methods
        from linda_core.tools.counters import CounterCalculator
        rows = calculator._get_rows_in_range(test_date, 30)
        
        # Test trigger frequency
        trigger_freq = calculator.get_field_frequency("potential_triggers", rows)
        assert "Stress" in trigger_freq
        assert "Aged cheese" in trigger_freq
        
        # Test medication patterns
        med_patterns = calculator.get_medication_usage_pattern(rows)
        assert "Ubrelvy" in med_patterns
        assert "Acetaminophen" in med_patterns
    
    def test_data_assessor_conversational_logic(self):
        """Test DataAssessor for conversational data capture."""
        assessor = DataAssessor()
        
        # Test 1: Empty data should prompt for required fields
        empty_data = {}
        completeness, missing = assessor.assess_completeness(empty_data)
        
        assert completeness < 0.5  # Should be low completeness
        assert len(missing) > 0
        assert any(f.field == "attack_types" for f in missing)  # Should be missing required field
        
        # Test next prompt
        action = assessor.get_next_prompt(empty_data)
        assert action is not None
        assert action.action == "prompt_user"
        assert action.field_being_requested == "attack_types"  # Should ask for required field first
        
        # Test 2: Partial data should unlock contingent fields
        partial_data = {
            "attack_types": serialize_multi_select_value(["Migraine"]),
        }
        
        completeness, missing = assessor.assess_completeness(partial_data)
        assert completeness > 0.1  # Should be higher than empty
        
        action = assessor.get_next_prompt(partial_data)
        assert action is not None
        assert action.field_being_requested in ["highest_pain_level", "attack_start_time", "associated_symptoms"]
        
        # Test 3: Good data should indicate sufficiency
        complete_data = {
            "attack_types": serialize_multi_select_value(["Migraine"]),
            "highest_pain_level": "7",
            "attack_start_time": "2 hours ago",
            "associated_symptoms": serialize_multi_select_value(["Nausea", "Photophobia"]),
            "potential_triggers": serialize_multi_select_value(["Stress"]),
        }
        
        completeness, missing = assessor.assess_completeness(complete_data)
        assert completeness >= 0.6  # Should meet threshold
        
        # Should indicate sufficiency
        assert assessor.is_data_sufficient(complete_data) == True
        
        # Should not prompt for more
        action = assessor.get_next_prompt(complete_data)
        assert action is None  # No more prompting needed
    
    def test_full_workflow_simulation(self):
        """Test a complete multi-turn conversation workflow."""
        log_store = LogStore()
        renderer = TableRenderer()
        assessor = DataAssessor()
        test_date = "2025-08-12"
        
        # Turn 1: User reports migraine
        turn1_deltas = [
            RowDelta(field="attack_types", value=["Migraine"], source_msg_id="turn1"),
            RowDelta(field="highest_pain_level", value="6", source_msg_id="turn1"),
        ]
        log_store.write_rows(turn1_deltas, test_date)
        
        # Check if more data needed
        day_data = log_store.read_rows(test_date)
        action = assessor.get_next_prompt(day_data)
        
        assert action is not None
        assert action.action == "prompt_user"
        # Should ask for time or symptoms next
        assert action.field_being_requested in ["attack_start_time", "associated_symptoms"]
        
        # Turn 2: User provides symptoms
        turn2_deltas = [
            RowDelta(field="associated_symptoms", value=["Nausea", "Photophobia"], source_msg_id="turn2"),
            RowDelta(field="attack_start_time", value="2 hours ago", source_msg_id="turn2"),
        ]
        log_store.write_rows(turn2_deltas, test_date)
        
        # Check again
        day_data = log_store.read_rows(test_date)
        action = assessor.get_next_prompt(day_data)
        
        # Should still want more data (triggers, meds, etc.)
        assert action is not None
        assert action.field_being_requested in ["potential_triggers", "medications_taken", "location_at_attack_start"]
        
        # Turn 3: User provides trigger and medication
        turn3_deltas = [
            RowDelta(field="potential_triggers", value=["Stress", "Lack of sleep"], source_msg_id="turn3"),
            RowDelta(field="medications_taken", value=["Ubrelvy"], source_msg_id="turn3"),
        ]
        log_store.write_rows(turn3_deltas, test_date)
        
        # Check final state
        day_data = log_store.read_rows(test_date)
        
        # Should now have sufficient data
        assert assessor.is_data_sufficient(day_data) == True
        
        # Should not prompt for more
        action = assessor.get_next_prompt(day_data)
        assert action is None
        
        # Should be able to render final reply
        table = renderer.render_delta_table([
            RowDelta(field=field, value=value, source_msg_id="summary") 
            for field, value in day_data.items() if value
        ], test_date)
        
        # Check that final table contains all the data properly formatted
        assert "Migraine" in table
        assert "6/10 (Severe)" in table
        assert "Nausea, Photophobia" in table
        assert "Stress, Lack of sleep" in table
        assert "Ubrelvy" in table


def run_tests():
    """Run all tests and print results."""
    print("Testing Expanded Rung 1 Foundation...")
    print("=" * 50)
    
    # Run pytest programmatically
    test_file = __file__
    exit_code = pytest.main([test_file, "-v", "--tb=short"])
    
    return exit_code == 0


if __name__ == "__main__":
    success = run_tests()
    if success:
        print("\n✅ All tests passed! Expanded foundation is working correctly.")
    else:
        print("\n❌ Some tests failed. Check output above.")
    
    exit(0 if success else 1)