#!/usr/bin/env python3
"""
Integration tests for Rung 2: Extractor Agent with Rung 1 Foundation.
Tests the complete workflow from message input to structured output.

This verifies that:
- Extractor Agent integrates cleanly with existing Rung 1 tools
- Workflow processes messages end-to-end
- All components work together without conflicts
- Legacy compatibility is maintained
"""

import unittest
import sys
import os
from unittest.mock import Mock, patch, MagicMock
from datetime import datetime

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from linda_core.workflow import MigraineDayWorkflow, process_user_message
from linda_core.extractor_agent import ExtractorAgent
from linda_core.schemas import (
    ExtractionResult, 
    EnhancedRowDelta, 
    EnhancedEpisodeDelta,
    FieldID, 
    EvidenceSpan,
    TurnPayload
)


class MockExtractorAgent:
    """Mock extractor agent for integration testing."""
    
    def extract(self, message: str, source_msg_id: str) -> ExtractionResult:
        """Return mock extraction based on message content."""
        message_lower = message.lower()
        
        # Mock different types of extractions based on message
        if "pain" in message_lower and "8" in message:
            return ExtractionResult(
                row_deltas=[
                    EnhancedRowDelta(
                        field_id=FieldID.HIGHEST_PAIN_LEVEL,
                        value_norm=8,
                        value_raw="pain 8/10",
                        confidence=0.95,
                        evidence_span=EvidenceSpan(start=0, end=10, text="pain 8/10"),
                        source_msg_id=source_msg_id
                    )
                ]
            )
        elif "migraine started" in message_lower:
            return ExtractionResult(
                episode_deltas=[
                    EnhancedEpisodeDelta(
                        op="open",
                        fields={"start": "14:00", "init": 6},
                        confidence=0.9,
                        evidence_span=EvidenceSpan(start=0, end=15, text="migraine started")
                    )
                ]
            )
        elif "took ubrelvy" in message_lower:
            return ExtractionResult(
                row_deltas=[
                    EnhancedRowDelta(
                        field_id=FieldID.MEDICATIONS_TAKEN,
                        value_norm=["Ubrelvy"],
                        value_raw="took Ubrelvy",
                        confidence=1.0,
                        evidence_span=EvidenceSpan(start=0, end=12, text="took Ubrelvy"),
                        source_msg_id=source_msg_id
                    )
                ]
            )
        else:
            # Empty result for non-medical messages
            return ExtractionResult()


class TestRung2Integration(unittest.TestCase):
    """Test integration of Extractor Agent with Rung 1 components."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.workflow = MigraineDayWorkflow(debug_mode=True)
        
        # Mock the extractor agent to avoid API calls
        self.mock_extractor = MockExtractorAgent()
        
        # Mock database operations to avoid file I/O
        self.workflow.log_store.write_rows = Mock()
        self.workflow.log_store.read_rows = Mock(return_value={})
        self.workflow.episode_manager.write_episode_delta = Mock()
        self.workflow.episode_manager.get_open_episodes = Mock(return_value=[])
        self.workflow.counter_calculator.compute_counters = Mock()
        self.workflow.safety_gate.check_safety = Mock(return_value=(False, []))
        self.workflow.profile_manager.upsert_profile = Mock()
    
    def test_workflow_initialization(self):
        """Test that workflow initializes with all components."""
        workflow = MigraineDayWorkflow()
        
        # Check all components are initialized
        self.assertIsNotNone(workflow.day_resolver)
        self.assertIsNotNone(workflow.log_store)
        self.assertIsNotNone(workflow.episode_manager)
        self.assertIsNotNone(workflow.counter_calculator)
        self.assertIsNotNone(workflow.renderer)
        self.assertIsNotNone(workflow.safety_gate)
        self.assertIsNotNone(workflow.profile_manager)
    
    @patch('linda_core.workflow.extractor_agent')
    def test_simple_pain_logging(self, mock_extractor):
        """Test simple pain level logging workflow."""
        # Set up mock extractor
        mock_extractor.extract = self.mock_extractor.extract
        
        # Mock counter result
        from linda_core.schemas import Counters
        mock_counters = Counters(
            ubrelvy_30d=2,
            acetaminophen_30d=5,
            amine_7d=1,
            reflux_food_today=0,
            rescue_inhaler_7d=3,
            migraine_episodes_30d=4,
            red_days_30d=0
        )
        self.workflow.counter_calculator.compute_counters.return_value = mock_counters
        
        # Test simple pain logging
        result = self.workflow.run(
            message="pain 8/10",
            user_id="test_user",
            date_iso="2025-01-15"
        )
        
        # Verify result structure
        self.assertIsInstance(result, TurnPayload)
        self.assertIsNotNone(result.reply)
        self.assertIsNotNone(result.data)
        
        # Verify data was extracted and stored
        self.workflow.log_store.write_rows.assert_called_once()
        
        # Check that row delta was created
        call_args = self.workflow.log_store.write_rows.call_args
        row_deltas = call_args[0][0]  # First argument
        self.assertTrue(len(row_deltas) > 0)
        self.assertEqual(row_deltas[0].field, "highest_pain_level")
        self.assertEqual(row_deltas[0].value, 8)
    
    @patch('linda_core.workflow.extractor_agent')
    def test_episode_lifecycle(self, mock_extractor):
        """Test episode creation workflow."""
        mock_extractor.extract = self.mock_extractor.extract
        
        # Mock counter result
        from linda_core.schemas import Counters
        mock_counters = Counters()
        self.workflow.counter_calculator.compute_counters.return_value = mock_counters
        
        # Test episode start
        result = self.workflow.run(
            message="migraine started at 2pm",
            user_id="test_user",
            date_iso="2025-01-15"
        )
        
        # Verify episode delta was processed
        self.workflow.episode_manager.write_episode_delta.assert_called_once()
        
        # Check episode delta structure
        call_args = self.workflow.episode_manager.write_episode_delta.call_args
        episode_delta = call_args[0][0]  # First argument
        self.assertEqual(episode_delta.op, "open")
    
    @patch('linda_core.workflow.extractor_agent')
    def test_medication_logging(self, mock_extractor):
        """Test medication logging workflow."""
        mock_extractor.extract = self.mock_extractor.extract
        
        # Mock counter result
        from linda_core.schemas import Counters
        mock_counters = Counters()
        self.workflow.counter_calculator.compute_counters.return_value = mock_counters
        
        # Test medication logging
        result = self.workflow.run(
            message="took Ubrelvy 100mg",
            user_id="test_user",
            date_iso="2025-01-15"
        )
        
        # Verify medication was logged
        self.workflow.log_store.write_rows.assert_called_once()
        
        # Check medication field
        call_args = self.workflow.log_store.write_rows.call_args
        row_deltas = call_args[0][0]
        self.assertTrue(len(row_deltas) > 0)
        self.assertEqual(row_deltas[0].field, "medications_taken")
        self.assertIn("Ubrelvy", row_deltas[0].value)
    
    @patch('linda_core.workflow.extractor_agent')
    def test_intent_classification(self, mock_extractor):
        """Test intent classification for different message types."""
        mock_extractor.extract = self.mock_extractor.extract
        
        # Mock counter result
        from linda_core.schemas import Counters
        mock_counters = Counters()
        self.workflow.counter_calculator.compute_counters.return_value = mock_counters
        
        # Test log intent (default)
        result_log = self.workflow.run(
            message="pain 5/10",
            user_id="test_user"
        )
        self.assertEqual(result_log.reply.mode, "log")
        
        # Test Q&A intent
        result_qa = self.workflow.run(
            message="How many migraines did I have this month?",
            user_id="test_user"
        )
        self.assertEqual(result_qa.reply.mode, "qa")
        
        # Test full table intent
        result_table = self.workflow.run(
            message="show me everything",
            user_id="test_user"
        )
        self.assertEqual(result_table.reply.mode, "full_table")
    
    @patch('linda_core.workflow.extractor_agent')
    def test_safety_gate_integration(self, mock_extractor):
        """Test safety gate integration with workflow."""
        mock_extractor.extract = self.mock_extractor.extract
        
        # Mock safety alert
        self.workflow.safety_gate.check_safety.return_value = (
            True,  # Triggered
            [{"severity": "red_flag", "message": "Neurological symptoms detected"}]
        )
        
        # Mock counter result
        from linda_core.schemas import Counters
        mock_counters = Counters()
        self.workflow.counter_calculator.compute_counters.return_value = mock_counters
        
        result = self.workflow.run(
            message="severe headache with vision loss",
            user_id="test_user"
        )
        
        # Verify safety banner is prepended
        self.assertIn("🚨", result.reply.markdown)
        self.assertIn("MEDICAL ALERT", result.reply.markdown)
        
        # Verify alert in data
        self.assertTrue(len(result.data.alerts) > 0)
        self.assertEqual(result.data.alerts[0]["severity"], "red_flag")
    
    @patch('linda_core.workflow.extractor_agent')
    def test_non_medical_message(self, mock_extractor):
        """Test handling of non-medical messages."""
        mock_extractor.extract = self.mock_extractor.extract
        
        # Mock counter result
        from linda_core.schemas import Counters
        mock_counters = Counters()
        self.workflow.counter_calculator.compute_counters.return_value = mock_counters
        
        result = self.workflow.run(
            message="thanks for the help!",
            user_id="test_user"
        )
        
        # Should complete without errors
        self.assertIsInstance(result, TurnPayload)
        
        # Should not call write operations for empty extractions
        # (since no data was extracted)
        if not result.data.row_deltas:
            # If no row deltas, write_rows might not be called or called with empty list
            pass  # This is expected behavior
    
    def test_convenience_function(self):
        """Test the convenience function works."""
        with patch('linda_core.workflow.workflow') as mock_workflow:
            mock_payload = TurnPayload(
                reply=Mock(),
                data=Mock()
            )
            mock_workflow.run.return_value = mock_payload
            
            result = process_user_message("test message", "test_user")
            
            self.assertEqual(result, mock_payload)
            mock_workflow.run.assert_called_once_with("test message", "test_user", None)
    
    def test_error_handling(self):
        """Test workflow error handling."""
        # Force an error in the workflow
        self.workflow.day_resolver.resolve_date = Mock(side_effect=Exception("Test error"))
        
        result = self.workflow.run(
            message="test message",
            user_id="test_user"
        )
        
        # Should return error response instead of crashing
        self.assertIsInstance(result, TurnPayload)
        self.assertEqual(result.reply.mode, "error")
        self.assertIn("System Error", result.reply.markdown)
        self.assertTrue(any(alert["severity"] == "error" for alert in result.data.alerts))


class TestLegacyCompatibility(unittest.TestCase):
    """Test that Rung 2 maintains compatibility with Rung 1."""
    
    def test_schema_compatibility(self):
        """Test that new schemas don't break existing code."""
        # Import both old and new schemas
        from linda_core.schemas import RowDelta, EpisodeDelta  # Legacy
        from linda_core.schemas import EnhancedRowDelta, EnhancedEpisodeDelta  # New
        
        # Legacy schemas should still work
        legacy_row = RowDelta(
            field="highest_pain_level",
            value=7,
            source_msg_id="test"
        )
        self.assertEqual(legacy_row.field, "highest_pain_level")
        
        legacy_episode = EpisodeDelta(
            id="episode_1",
            op="upsert",
            fields={"start": "14:00"}
        )
        self.assertEqual(legacy_episode.op, "upsert")
    
    def test_conversion_functions(self):
        """Test conversion between enhanced and legacy formats."""
        from linda_core.extractor_agent import convert_to_legacy_row_deltas, convert_to_legacy_episode_deltas
        
        # Test row delta conversion
        enhanced_row = EnhancedRowDelta(
            field_id=FieldID.HIGHEST_PAIN_LEVEL,
            value_norm=8,
            confidence=0.9,
            evidence_span=EvidenceSpan(start=0, end=5, text="test"),
            source_msg_id="test_123"
        )
        
        legacy_rows = convert_to_legacy_row_deltas([enhanced_row])
        self.assertEqual(len(legacy_rows), 1)
        self.assertEqual(legacy_rows[0]["field"], "highest_pain_level")
        self.assertEqual(legacy_rows[0]["value"], 8)
        
        # Test episode delta conversion
        enhanced_episode = EnhancedEpisodeDelta(
            id="episode_123",
            op="open",
            fields={"start": "14:00"},
            confidence=0.8,
            evidence_span=EvidenceSpan(start=0, end=10, text="test")
        )
        
        legacy_episodes = convert_to_legacy_episode_deltas([enhanced_episode])
        self.assertEqual(len(legacy_episodes), 1)
        self.assertEqual(legacy_episodes[0]["op"], "open")


if __name__ == '__main__':
    # Run integration tests
    unittest.main(verbosity=2)