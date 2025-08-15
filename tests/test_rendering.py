#!/usr/bin/env python3
"""
Test rendering utilities.
Snapshot testing: exact row order, blanks preserved.

References: docs/Linda_agentic_framework_human.md (tests section)
"""

import pytest
from linda_core.tools.rendering import TableRenderer
from linda_core.schemas import RowDelta, Episode


class TestTableRenderer:
    """Test the table rendering functionality."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.renderer = TableRenderer()
    
    def test_full_table_rendering_preserves_order(self):
        """Test that full table rendering maintains canonical field order."""
        # Sample day data with some fields filled
        day_data = {
            "date": "2025-01-15",
            "hydration_oz": "64 oz",
            "left_headache_pain": "3/10",
            "sleep_hours_quality": "7.5h, 8/10",
            # Intentionally missing other fields to test blank preservation
        }
        
        result = self.renderer.render_full_table(day_data)
        
        # Check that result contains the table structure
        assert "**Full log for 2025-01-15**" in result
        assert "| Field | Details |" in result
        assert "| Date | 2025-01-15 |" in result
        assert "| Hydration (oz) | 64 oz |" in result
        assert "| Left-headache pain (0-10) | 3/10 |" in result
        
        # Check that empty fields are preserved as blank
        lines = result.split('\n')
        field_lines = [line for line in lines if '|' in line and 'Field' not in line and '---' not in line]
        
        # Should have one line for each field in TABLE_FIELDS
        from linda_core.schemas import TABLE_FIELDS
        assert len(field_lines) == len(TABLE_FIELDS)
        
        # Check that empty fields show as blank, not missing
        time_line = next((line for line in field_lines if "| Time |" in line), None)
        assert time_line is not None
        assert "| Time |  |" in time_line  # Empty value
    
    def test_delta_table_rendering(self):
        """Test delta table rendering shows only changed fields."""
        deltas = [
            RowDelta(field="hydration_oz", value="32 oz", source_msg_id="msg_1"),
            RowDelta(field="left_headache_pain", value="5/10", source_msg_id="msg_1"),
        ]
        
        result = self.renderer.render_delta_table(deltas, "2025-01-15")
        
        # Should show log saved header
        assert "**Log saved** – 2025-01-15" in result
        
        # Should only show changed fields
        assert "| Hydration (oz) | 32 oz |" in result
        assert "| Left-headache pain (0-10) | 5/10 |" in result
        
        # Should NOT show unchanged fields like Date, Time, etc.
        assert "| Date |" not in result.split('\n')[3:]  # Skip header lines
        assert "| Time |" not in result.split('\n')[3:]
    
    def test_episode_table_rendering(self):
        """Test episode sub-table rendering."""
        episodes = [
            Episode(
                id="episode_2025-01-15_1",
                date="2025-01-15",
                symptom="left temple headache",
                start="14:30",
                init=4,
                peak=7
            )
        ]
        
        day_data = {"date": "2025-01-15"}
        result = self.renderer.render_full_table(day_data, episodes)
        
        # Should include episode table
        assert "**Episodes**" in result
        assert "| ID | Symptom | Start |" in result
        assert "| episode_2025-01-15_1 | left temple headache | 14:30 |" in result
    
    def test_field_name_formatting(self):
        """Test that field names are properly formatted for display."""
        # Test a few key field name transformations
        assert self.renderer._format_field_name("bed_time") == "Bed time (HH:MM)"
        assert self.renderer._format_field_name("hydration_oz") == "Hydration (oz)"
        assert self.renderer._format_field_name("left_headache_pain") == "Left-headache pain (0-10)"
        assert self.renderer._format_field_name("notes_weather_hormones") == "Notes (weather change, hormones, travel, etc.)"
    
    def test_two_block_reply_structure(self):
        """Test the two-block reply structure."""
        table_content = "**Log saved**\n\n| Field | Details |\n|-------|---------|"
        reflections = "Great hydration today. Consider maintaining this level."
        
        reply = self.renderer.render_two_block_reply(table_content, reflections, "log")
        
        assert reply.mode == "log"
        assert "**Log saved**" in reply.markdown
        assert "**Reflections**" in reply.markdown
        assert reflections in reply.markdown
    
    def test_full_table_mode_no_reflections(self):
        """Test that full_table mode suppresses reflections."""
        table_content = "**Full log for 2025-01-15**\n\n| Field | Details |"
        reflections = "This should not appear"
        
        reply = self.renderer.render_two_block_reply(table_content, reflections, "full_table")
        
        assert reply.mode == "full_table"
        assert "**Reflections**" not in reply.markdown
        assert reflections not in reply.markdown
        assert table_content in reply.markdown
    
    def test_empty_deltas(self):
        """Test handling of empty delta list."""
        result = self.renderer.render_delta_table([], "2025-01-15")
        
        assert "**Log saved** – 2025-01-15" in result
        assert "*No field changes detected.*" in result


if __name__ == "__main__":
    pytest.main([__file__])