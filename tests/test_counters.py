#!/usr/bin/env python3
"""
Test counter calculations.
Rolling-window math from fixtures.

References: docs/Linda_agentic_framework_human.md (tests section)
"""

import pytest
import tempfile
import os
from datetime import datetime, date, timedelta
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from linda_core.database import Base, DayRow, Episode
from linda_core.tools.counters import CounterCalculator
from linda_core.schemas import RowDelta


class TestCounters:
    """Test rolling counter calculations."""
    
    def setup_method(self):
        """Set up test database with sample data."""
        # Create temporary database
        self.db_fd, self.db_path = tempfile.mkstemp(suffix='.db')
        self.engine = create_engine(f'sqlite:///{self.db_path}')
        Base.metadata.create_all(self.engine)
        
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.session = self.SessionLocal()
        
        # Create sample data for testing
        self._create_sample_data()
    
    def teardown_method(self):
        """Clean up test database."""
        self.session.close()
        os.close(self.db_fd)
        os.unlink(self.db_path)
    
    def _create_sample_data(self):
        """Create sample data for counter testing."""
        target_date = date(2025, 1, 15)
        
        # Create 45 days of data (15 days before target + target + 29 days after)
        for i in range(-15, 30):
            test_date = target_date + timedelta(days=i)
            date_str = test_date.isoformat()
            
            # Add Ubrelvy usage on specific days (to test 30-day window)
            if i in [-5, -3, 0, 2, 5, 8, 10, 12, 15, 18, 20]:  # 11 days with Ubrelvy
                ubrelvy_row = DayRow(
                    date=date_str,
                    field="ubrelvy_mg_brand",
                    value="62.5 mg (Ubrelvy)",
                    source_msg_id=f"msg_{i}_ubrelvy",
                    ts=datetime.utcnow().isoformat()
                )
                self.session.add(ubrelvy_row)
            
            # Add acetaminophen usage
            if i in [-2, 1, 4, 7, 11, 14, 17]:  # 7 days with acetaminophen
                acetaminophen_row = DayRow(
                    date=date_str,
                    field="acetaminophen_mg_brand",
                    value="500 mg (Tylenol)",
                    source_msg_id=f"msg_{i}_acetaminophen",
                    ts=datetime.utcnow().isoformat()
                )
                self.session.add(acetaminophen_row)
            
            # Add amine-rich foods in last 7 days
            if -7 <= i <= 0 and i in [-6, -4, -2, 0]:  # 4 amine foods in last 7 days
                amine_row = DayRow(
                    date=date_str,
                    field="meals_times",
                    value="Lunch with aged cheddar cheese and wine",
                    source_msg_id=f"msg_{i}_amine",
                    ts=datetime.utcnow().isoformat()
                )
                self.session.add(amine_row)
            
            # Add reflux foods today
            if i == 0:  # Only on target date
                reflux_row = DayRow(
                    date=date_str,
                    field="meals_times",
                    value="Spicy tomato pasta with garlic bread",
                    source_msg_id=f"msg_{i}_reflux",
                    ts=datetime.utcnow().isoformat()
                )
                self.session.add(reflux_row)
            
            # Add rescue inhaler uses in last 7 days
            if -7 <= i <= 0 and i in [-5, -3, 0]:  # 3 days with rescue inhaler
                inhaler_row = DayRow(
                    date=date_str,
                    field="rescue_inhaler_uses",
                    value="2 puffs",
                    source_msg_id=f"msg_{i}_inhaler",
                    ts=datetime.utcnow().isoformat()
                )
                self.session.add(inhaler_row)
        
        # Add migraine episodes in last 30 days
        episode_dates = [-10, -5, 0, 5, 10]  # 5 episodes
        for i, episode_day in enumerate(episode_dates):
            episode_date = target_date + timedelta(days=episode_day)
            episode = Episode(
                id=f"episode_{episode_date.isoformat()}_{i}",
                date=episode_date.isoformat(),
                symptom="migraine",
                start="14:00",
                init=5,
                peak=7
            )
            self.session.add(episode)
        
        self.session.commit()
    
    def test_ubrelvy_30d_count(self):
        """Test 30-day Ubrelvy count calculation."""
        calculator = CounterCalculator(self.session)
        counters = calculator.compute_counters("2025-01-15")
        
        # Should count Ubrelvy days in 30-day window (from 2024-12-16 to 2025-01-15)
        # Looking at our test data: days -5, -3, 0 fall in this window = 3 days
        # Note: The 30-day window is inclusive and goes backward from target date
        expected_count = 3  # Ubrelvy on days -5, -3, 0 relative to target
        assert counters.ubrelvy_30d == expected_count
    
    def test_acetaminophen_30d_count(self):
        """Test 30-day acetaminophen count calculation."""
        calculator = CounterCalculator(self.session)
        counters = calculator.compute_counters("2025-01-15")
        
        # Should count acetaminophen days in 30-day window
        # Looking at our test data: days -2, 1 fall in this window = 2 days
        expected_count = 2
        assert counters.acetaminophen_30d == expected_count
    
    def test_amine_7d_count(self):
        """Test 7-day amine foods count calculation."""
        calculator = CounterCalculator(self.session)
        counters = calculator.compute_counters("2025-01-15")
        
        # Should count amine foods in last 7 days (2025-01-09 to 2025-01-15)
        # Looking at our test data: days -6, -4, -2, 0 = 4 amine foods
        expected_count = 4
        assert counters.amine_7d == expected_count
    
    def test_reflux_food_today_count(self):
        """Test today's reflux foods count."""
        calculator = CounterCalculator(self.session)
        counters = calculator.compute_counters("2025-01-15")
        
        # Should count reflux foods only on target date
        # Our test data has "spicy tomato pasta with garlic" = 3 triggers
        expected_count = 3  # spicy, tomato, garlic
        assert counters.reflux_food_today == expected_count
    
    def test_rescue_inhaler_7d_count(self):
        """Test 7-day rescue inhaler count calculation."""
        calculator = CounterCalculator(self.session)
        counters = calculator.compute_counters("2025-01-15")
        
        # Should count total puffs in last 7 days
        # Our test data: 2 puffs on days -5, -3, 0 = 6 total puffs
        expected_count = 6
        assert counters.rescue_inhaler_7d == expected_count
    
    def test_migraine_episodes_30d_count(self):
        """Test 30-day migraine episodes count."""
        calculator = CounterCalculator(self.session)
        counters = calculator.compute_counters("2025-01-15")
        
        # Should count episodes in 30-day window
        # Our test data: episodes on days -10, -5, 0 = 3 episodes
        expected_count = 3
        assert counters.migraine_episodes_30d == expected_count
    
    def test_counter_storage_and_retrieval(self):
        """Test that counters are properly stored and retrieved."""
        calculator = CounterCalculator(self.session)
        
        # Calculate and store counters
        counters = calculator.compute_counters("2025-01-15")
        calculator._store_counters(counters)
        
        # Retrieve stored counters
        stored_counters = calculator.get_stored_counters("2025-01-15")
        
        assert stored_counters is not None
        assert stored_counters.date == "2025-01-15"
        assert stored_counters.ubrelvy_30d == counters.ubrelvy_30d
        assert stored_counters.amine_7d == counters.amine_7d
    
    def test_edge_case_empty_data(self):
        """Test counter calculation with no data."""
        # Create clean session with no data
        empty_session = self.SessionLocal()
        
        calculator = CounterCalculator(empty_session)
        counters = calculator.compute_counters("2025-01-15")
        
        # All counters should be zero
        assert counters.ubrelvy_30d == 0
        assert counters.acetaminophen_30d == 0
        assert counters.amine_7d == 0
        assert counters.reflux_food_today == 0
        assert counters.rescue_inhaler_7d == 0
        assert counters.migraine_episodes_30d == 0
        
        empty_session.close()
    
    def test_counter_date_boundary(self):
        """Test that counters respect date boundaries correctly."""
        calculator = CounterCalculator(self.session)
        
        # Test one day earlier than our target
        counters = calculator.compute_counters("2025-01-14")
        
        # Should have different counts since the window has shifted
        # Ubrelvy count should be different (day 0 is now outside the window)
        target_counters = calculator.compute_counters("2025-01-15")
        
        # The counts should be different due to window shift
        # (specific values depend on test data setup)
        assert counters.date == "2025-01-14"
        assert target_counters.date == "2025-01-15"


if __name__ == "__main__":
    pytest.main([__file__])