#!/usr/bin/env python3
"""
Test idempotency of database operations.
Writing same delta twice doesn't duplicate.

References: docs/Linda_agentic_framework_human.md (tests section)
"""

import pytest
import tempfile
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from linda_core.database import Base, DayRow
from linda_core.tools.log_store import LogStore
from linda_core.schemas import RowDelta


class TestIdempotency:
    """Test idempotent database operations."""
    
    def setup_method(self):
        """Set up test database for each test."""
        # Create temporary database
        self.db_fd, self.db_path = tempfile.mkstemp(suffix='.db')
        self.engine = create_engine(f'sqlite:///{self.db_path}')
        Base.metadata.create_all(self.engine)
        
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.session = self.SessionLocal()
    
    def teardown_method(self):
        """Clean up test database."""
        self.session.close()
        os.close(self.db_fd)
        os.unlink(self.db_path)
    
    def test_write_same_delta_twice_no_duplicate(self):
        """Test that writing the same delta twice doesn't create duplicates."""
        log_store = LogStore(self.session)
        
        # Create a delta
        delta = RowDelta(
            field="hydration_oz",
            value="64 oz",
            source_msg_id="test_msg_1"
        )
        
        # Write it twice
        log_store.write_rows([delta], "2025-01-15")
        log_store.write_rows([delta], "2025-01-15")
        
        # Should only have one record
        rows = self.session.query(DayRow).filter(
            DayRow.date == "2025-01-15",
            DayRow.field == "hydration_oz",
            DayRow.source_msg_id == "test_msg_1"
        ).all()
        
        assert len(rows) == 1
        assert rows[0].value == "64 oz"
    
    def test_same_field_different_messages_creates_multiple(self):
        """Test that same field from different messages creates multiple records."""
        log_store = LogStore(self.session)
        
        # Two deltas for same field, different messages
        delta1 = RowDelta(
            field="hydration_oz",
            value="32 oz",
            source_msg_id="msg_1"
        )
        delta2 = RowDelta(
            field="hydration_oz", 
            value="64 oz",
            source_msg_id="msg_2"
        )
        
        log_store.write_rows([delta1], "2025-01-15")
        log_store.write_rows([delta2], "2025-01-15")
        
        # Should have two records
        rows = self.session.query(DayRow).filter(
            DayRow.date == "2025-01-15",
            DayRow.field == "hydration_oz"
        ).all()
        
        assert len(rows) == 2
        
        # Reading should return the latest value (by timestamp)
        day_data = log_store.read_rows("2025-01-15")
        assert day_data["hydration_oz"] == "64 oz"  # Latest value
    
    def test_update_existing_record_changes_value(self):
        """Test that updating an existing record changes the value."""
        log_store = LogStore(self.session)
        
        # Initial write
        delta1 = RowDelta(
            field="hydration_oz",
            value="32 oz",
            source_msg_id="msg_1"
        )
        log_store.write_rows([delta1], "2025-01-15")
        
        # Update same record
        delta2 = RowDelta(
            field="hydration_oz",
            value="48 oz",  # Updated value
            source_msg_id="msg_1"  # Same message ID
        )
        log_store.write_rows([delta2], "2025-01-15")
        
        # Should still have only one record, but updated
        rows = self.session.query(DayRow).filter(
            DayRow.date == "2025-01-15",
            DayRow.field == "hydration_oz",
            DayRow.source_msg_id == "msg_1"
        ).all()
        
        assert len(rows) == 1
        assert rows[0].value == "48 oz"
    
    def test_different_dates_create_separate_records(self):
        """Test that same field on different dates creates separate records."""
        log_store = LogStore(self.session)
        
        delta = RowDelta(
            field="hydration_oz",
            value="64 oz", 
            source_msg_id="msg_1"
        )
        
        # Write to two different dates
        log_store.write_rows([delta], "2025-01-15")
        log_store.write_rows([delta], "2025-01-16")
        
        # Should have two records
        rows = self.session.query(DayRow).filter(
            DayRow.field == "hydration_oz",
            DayRow.source_msg_id == "msg_1"
        ).all()
        
        assert len(rows) == 2
        
        dates = {row.date for row in rows}
        assert dates == {"2025-01-15", "2025-01-16"}
    
    def test_complex_idempotency_scenario(self):
        """Test complex scenario with multiple fields and messages."""
        log_store = LogStore(self.session)
        
        # Multiple deltas in same batch
        deltas = [
            RowDelta(field="hydration_oz", value="32 oz", source_msg_id="msg_1"),
            RowDelta(field="left_headache_pain", value="4/10", source_msg_id="msg_1"),
            RowDelta(field="sleep_hours_quality", value="7h, 8/10", source_msg_id="msg_1"),
        ]
        
        # Write twice
        log_store.write_rows(deltas, "2025-01-15")
        log_store.write_rows(deltas, "2025-01-15")
        
        # Should have exactly 3 records (one per field)
        rows = self.session.query(DayRow).filter(
            DayRow.date == "2025-01-15",
            DayRow.source_msg_id == "msg_1"
        ).all()
        
        assert len(rows) == 3
        
        # Verify all fields are present
        fields = {row.field for row in rows}
        assert fields == {"hydration_oz", "left_headache_pain", "sleep_hours_quality"}


if __name__ == "__main__":
    pytest.main([__file__])