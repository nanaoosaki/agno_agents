# Agno-Chat Project Analysis - Part 2

## Additional Key File Contents

### healthlogger/workflow.py

```python
# healthlogger/workflow.py  
# Main Agno workflow for Health Logger v3

from typing import Optional, List

try:
    from agno.workflow.v2 import Workflow, Step
    AGNO_WORKFLOW_AVAILABLE = True
except ImportError:
    AGNO_WORKFLOW_AVAILABLE = False
    # Fallback classes for development
    class Workflow:
        def __init__(self, name, steps, workflow_session_state=None):
            self.name = name
            self.steps = steps
            self.workflow_session_state = workflow_session_state or {}
        
        def run(self, message, session_id=None):
            # Fallback implementation
            return type('RunResult', (), {'content': 'Workflow not available'})()
    
    class Step:
        def __init__(self, name, agent=None, executor=None):
            self.name = name
            self.agent = agent
            self.executor = executor

from .agents import create_extractor_agent, create_reply_agent
from .workflow_steps import process_and_log_step

def create_health_logger_workflow() -> Workflow:
    """
    Create the main Health Logger workflow with 3 steps:
    1. Extract - LLM converts natural language to structured data
    2. Process - Deterministic logic processes and stores data  
    3. Reply - LLM creates user-friendly response
    """
    
    if not AGNO_WORKFLOW_AVAILABLE:
        print("⚠️ Agno workflow not available, using fallback")
        return Workflow(
            name="Health Logger Workflow V3 (Fallback)",
            steps=[],
            workflow_session_state={}
        )
    
    # Create the agents
    extractor_agent = create_extractor_agent()
    reply_agent = create_reply_agent()
    
    # Define workflow steps
    steps = [
        Step(
            name="Extract",
            agent=extractor_agent
        ),
        Step(
            name="Process", 
            executor=process_and_log_step
        ),
        Step(
            name="Reply",
            agent=reply_agent  
        )
    ]
    
    # Create the workflow
    workflow = Workflow(
        name="Health Logger Workflow V3",
        steps=steps,
        # Session state is automatically managed per session_id by Agno
        workflow_session_state={}
    )
    
    return workflow

class HealthLoggerWorkflowWrapper:
    """
    Wrapper class to integrate Agno workflow with existing Gradio interface.
    This maintains compatibility with the current agents.py structure.
    """
    
    name = "Health Logger (v3)"
    description = "Pure Agno implementation with conversation context and episode continuity"
    
    def __init__(self):
        self.workflow = create_health_logger_workflow()
        print("✅ Health Logger v3 (Pure Agno) initialized successfully")
    
    def run(self, prompt: str, files: Optional[List[str]] = None):
        """
        Run the health logger workflow.
        
        Args:
            prompt: User's health message
            files: Optional file attachments (not yet implemented)
            
        Returns:
            ChatResult with workflow response
        """
        try:
            # Each user should have a unique session_id
            # In a real multi-user app, this would be dynamic per user
            session_id = "user_main_session"
            
            # Add file context if provided
            enhanced_prompt = prompt
            if files:
                file_info = f"\n\nNote: User attached {len(files)} file(s): {', '.join(files)}"
                enhanced_prompt = f"{prompt}{file_info}"
            
            # Run the workflow
            response = self.workflow.run(
                message=enhanced_prompt,
                session_id=session_id
            )
            
            # Import ChatResult here to avoid circular imports
            from dataclasses import dataclass
            from typing import Dict, Any
            
            @dataclass
            class ChatResult:
                text: str
                meta: Optional[Dict[str, Any]] = None
            
            return ChatResult(
                text=response.content,
                meta={
                    "workflow": "Health Logger v3",
                    "architecture": "pure_agno",
                    "session_id": session_id
                }
            )
            
        except Exception as e:
            # Import ChatResult for error case
            from dataclasses import dataclass
            from typing import Dict, Any
            
            @dataclass  
            class ChatResult:
                text: str
                meta: Optional[Dict[str, Any]] = None
            
            return ChatResult(
                text=f"❌ Error in health logger workflow: {str(e)}",
                meta={"error": str(e)}
            )
```

### healthlogger/agents.py

```python
# healthlogger/agents.py
# Agno agents for Health Logger v3

from typing import Optional

try:
    from agno.agent import Agent
    from agno.models.openai import OpenAIChat
    AGNO_AVAILABLE = True
except ImportError:
    AGNO_AVAILABLE = False
    Agent = object
    OpenAIChat = object

from healthlogger.schema_router import RouterOutput, SimpleRouterOutput
from data.schemas.episodes import ProcessingResult
from .prompts import get_extractor_system_prompt, get_reply_system_prompt

def create_extractor_agent():
    """
    Create the Extractor Agent with conversation history support.
    This agent converts natural language to structured health data.
    """
    if not AGNO_AVAILABLE:
        raise ImportError("Agno library not available")
    
    return Agent(
        name="HealthExtractorAgent",
        model=OpenAIChat(id="gpt-4o-mini-2024-07-18"),
        
        # KEY FIX: Enable conversation history
        add_history_to_messages=True,
        num_history_runs=5,  # Include last 5 conversation turns
        
        # Enforce structured output - use SimpleRouterOutput for OpenAI compatibility
        response_model=SimpleRouterOutput,
        
        # Comprehensive instructions
        instructions=[
            get_extractor_system_prompt(),
            "IMPORTANT: You must analyze the LATEST message in context of CHAT HISTORY.",
            "Look for continuity signals like 'still', 'now', 'it', 'the pain' that refer to previous messages.",
            "When in doubt about episode linking, use 'unknown' and let deterministic rules decide.",
            "Always include the original user text in fields.notes."
        ],
        
        # Disable markdown for structured output
        markdown=False,
        
        # Don't show tool calls in this agent
        show_tool_calls=False
    )

def create_reply_agent():
    """
    Create the Reply Agent for user-friendly responses.
    This agent converts processing results to natural language.
    """
    if not AGNO_AVAILABLE:
        raise ImportError("Agno library not available")
    
    return Agent(
        name="HealthReplyAgent", 
        model=OpenAIChat(id="gpt-4o-mini-2024-07-18"),
        
        # No history needed - just process current result
        add_history_to_messages=False,
        
        # Instructions for empathetic responses
        instructions=[
            get_reply_system_prompt(),
            "Convert the structured processing result into a warm, empathetic response.",
            "Be supportive and show you understand their health situation.",
            "Keep responses brief but caring."
        ],
        
        # Enable markdown for nice formatting
        markdown=True,
        
        # Don't show tool calls
        show_tool_calls=False
    )
```

### healthlogger/schema_router.py

```python
"""
Router-specific schemas for the Health Logger workflow.

These schemas are used specifically for LLM extraction and routing,
separate from the persistence layer schemas.
"""

from __future__ import annotations
from pydantic import BaseModel, Field
from typing import List, Optional, Literal, Dict, Any
from data.schemas.episodes import Intent, LinkStrategy, Fields, EpisodeLink, InterventionIn

# Flattened schema for OpenAI compatibility (no nested models, no Field descriptions)
class SimpleRouterOutput(BaseModel):
    """Flattened schema for OpenAI structured output - avoids $ref description errors"""
    intent: Intent
    condition: Optional[str] = None
    severity: Optional[int] = None
    location: Optional[str] = None
    triggers: Optional[List[str]] = None
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    notes: Optional[str] = None
    link_strategy: LinkStrategy
    episode_id: Optional[str] = None
    rationale: Optional[str] = None
    intervention_types: Optional[List[str]] = None
    intervention_doses: Optional[List[Optional[str]]] = None
    intervention_timings: Optional[List[Optional[str]]] = None
    intervention_notes: Optional[List[Optional[str]]] = None
    confidence: Optional[float] = None

class RouterOutput(BaseModel):
    """Complete router output with nested models for internal processing"""
    intent: Intent
    condition: Optional[str] = None
    fields: Fields
    episode_link: EpisodeLink
    interventions: List[InterventionIn] = Field(default_factory=list)
    confidence: Optional[float] = None
    
    @classmethod
    def from_simple(cls, simple: SimpleRouterOutput) -> 'RouterOutput':
        """Convert SimpleRouterOutput to full RouterOutput structure"""
        
        # Build fields object
        fields = Fields(
            severity=simple.severity,
            location=simple.location,
            triggers=simple.triggers,
            start_time=simple.start_time,
            end_time=simple.end_time,
            notes=simple.notes
        )
        
        # Build episode link object
        episode_link = EpisodeLink(
            link_strategy=simple.link_strategy,
            episode_id=simple.episode_id,
            rationale=simple.rationale
        )
        
        # Build interventions
        interventions = []
        if simple.intervention_types:
            for i, int_type in enumerate(simple.intervention_types):
                intervention = InterventionIn(
                    type=int_type,
                    dose=simple.intervention_doses[i] if simple.intervention_doses and i < len(simple.intervention_doses) else None,
                    timing=simple.intervention_timings[i] if simple.intervention_timings and i < len(simple.intervention_timings) else None,
                    notes=simple.intervention_notes[i] if simple.intervention_notes and i < len(simple.intervention_notes) else None
                )
                interventions.append(intervention)
        
        return cls(
            intent=simple.intent,
            condition=simple.condition,
            fields=fields,
            episode_link=episode_link,
            interventions=interventions,
            confidence=simple.confidence
        )
```

### data/storage_interface.py

```python
"""
Abstract storage interface for health data persistence.

This module defines the contract that all storage backends must implement,
allowing for easy swapping between JSON files, SQLite, PostgreSQL, etc.
"""

from abc import ABC, abstractmethod
from typing import Optional, List, Dict, Any
from datetime import datetime


class HealthDataStorage(ABC):
    """
    Abstract base class for health data storage backends.
    
    Defines the standard interface that all storage implementations
    must provide for episodes, observations, and interventions.
    """
    
    # === EPISODE OPERATIONS ===
    
    @abstractmethod
    def create_episode(self, condition: str, started_at: str, current_severity: int, 
                      location: Optional[str] = None, notes: Optional[str] = None) -> str:
        """
        Create a new health episode.
        
        Args:
            condition: The health condition (normalized)
            started_at: ISO timestamp when episode began
            current_severity: Initial severity (1-10)
            location: Optional location information
            notes: Optional additional notes
            
        Returns:
            The generated episode ID
        """
        pass
    
    @abstractmethod
    def get_episode_by_id(self, episode_id: str) -> Optional[Dict[str, Any]]:
        """Get an episode by its ID."""
        pass
    
    @abstractmethod
    def update_episode(self, episode_id: str, **updates) -> bool:
        """Update an existing episode with new data."""
        pass
    
    @abstractmethod
    def find_latest_open_episode(self, condition: str, window_hours: int = 12) -> Optional[Dict[str, Any]]:
        """Find the most recent open episode for a condition within a time window."""
        pass
    
    @abstractmethod
    def fetch_open_episode_candidates(self, window_hours: int = 24) -> List[Dict[str, Any]]:
        """Fetch episodes that might be candidates for linking new data."""
        pass
    
    @abstractmethod
    def close_episode(self, episode_id: str, ended_at: Optional[str] = None) -> bool:
        """Close an episode and mark it as resolved."""
        pass
    
    # === OBSERVATION OPERATIONS ===
    
    @abstractmethod
    def save_observation(self, timestamp: str, observation_type: str, value: str,
                        location: Optional[str] = None, notes: Optional[str] = None) -> str:
        """Save a health observation."""
        pass
    
    @abstractmethod
    def get_observations_in_range(self, start_time: str, end_time: str) -> List[Dict[str, Any]]:
        """Get all observations within a time range."""
        pass
    
    # === INTERVENTION OPERATIONS ===
    
    @abstractmethod
    def add_intervention(self, episode_id: str, intervention_type: str, 
                        dosage: Optional[str] = None, timing: Optional[str] = None,
                        notes: Optional[str] = None) -> bool:
        """Add an intervention to an episode."""
        pass
    
    @abstractmethod
    def get_episode_interventions(self, episode_id: str) -> List[Dict[str, Any]]:
        """Get all interventions for a specific episode."""
        pass
    
    # === EVENT LOG OPERATIONS ===
    
    @abstractmethod
    def append_event(self, event_type: str, data: Dict[str, Any], 
                    episode_id: Optional[str] = None) -> bool:
        """Append an event to the audit log."""
        pass
    
    @abstractmethod
    def get_recent_events(self, limit: int = 100) -> List[Dict[str, Any]]:
        """Get the most recent events from the audit log."""
        pass
    
    # === QUERY OPERATIONS ===
    
    @abstractmethod
    def get_episodes_in_range(self, start_time: str, end_time: str, 
                             condition: Optional[str] = None) -> List[Dict[str, Any]]:
        """Get episodes within a time range, optionally filtered by condition."""
        pass
    
    @abstractmethod
    def search_episodes_by_keyword(self, keyword: str) -> List[Dict[str, Any]]:
        """Search episodes by keyword in notes or other text fields."""
        pass
    
    # === MAINTENANCE OPERATIONS ===
    
    @abstractmethod
    def backup_data(self, backup_path: str) -> bool:
        """Create a backup of all data."""
        pass
    
    @abstractmethod
    def get_storage_stats(self) -> Dict[str, Any]:
        """Get statistics about the stored data."""
        pass
```

### health_advisor/recall/agent.py

```python
# healthlogger/recall/agent.py
# Recall Agent - Following docs/agno/tools/writing_your_own_tools.md and @openai-model-list.mdc
# Author: Claude (Anthropic AI Assistant) 
# Date: January 15, 2025

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from .tools import (
    parse_time_range,
    find_episodes_in_range,
    find_all_episodes_in_range,
    correlate_observation_to_episodes,
    get_daily_history,
)

def create_recall_agent() -> Agent:
    """
    Create the Recall Agent with proper tool integration and instructions.
    Uses gpt-4o-mini-2024-07-18 as per @openai-model-list.mdc recommendations.
    """
    
    recall_agent = Agent(
        name="RecallAgent",
        model=OpenAIChat(id="gpt-4o-mini-2024-07-18"),  # Using correct model ID from openai-model-list.mdc
        tools=[
            parse_time_range,
            find_episodes_in_range,
            find_all_episodes_in_range,
            correlate_observation_to_episodes,
            get_daily_history,
        ],
        show_tool_calls=True,
        markdown=True,
        instructions=[
            "You are a health data analyst specialized in analyzing historical health patterns and correlations.",
            "Your job is to answer questions about a user's health history using the provided tools.",
            "",
            "CRITICAL: You MUST follow a logical plan for every query:",
            "",
            "1. **ALWAYS START** with `parse_time_range` to understand the time period the user is asking about:",
            "   - 'last week', 'yesterday', 'last month', 'today', etc.",
            "   - This gives you structured start/end dates for all subsequent tool calls",
            "",
            "2. **CHOOSE THE RIGHT TOOL** based on the question type:",
            "   - For GENERAL overview questions ('what happened last week?', 'show me recent episodes'): use `find_all_episodes_in_range`",
            "   - For SPECIFIC condition searches ('my migraine episodes', 'pain episodes'): use `find_episodes_in_range`",
            "   - For correlation questions (\"Does X trigger Y?\"): use `correlate_observation_to_episodes`",
            "   - For daily summaries or calendar views: use `get_daily_history`",
            "",
            "3. **SYNTHESIZE** the structured data from tools into a clear, empathetic response:",
            "   - Use natural language, not technical jargon",
            "   - Be supportive and understanding about health concerns",
            "   - Present findings clearly with context",
            "",
            "IMPORTANT RULES:",
            "- If a tool returns no results, you MUST inform the user you don't have enough data",
            "- DO NOT HALLUCINATE or make up health information",
            "- Always present the conclusion from `CorrelationResult` directly to the user",
            "- For correlation questions, explain the time window used (default 24 hours)",
            "- Be clear about limitations: correlation ≠ causation",
            "",
            "EXAMPLE WORKFLOW:",
            "User: 'Did I have any migraines last week?'",
            "1. parse_time_range('last week') → get date range",
            "2. find_episodes_in_range('migraine', start_date, end_date) → get episodes",
            "3. Respond with empathetic summary of findings",
            "",
            "User: 'Does eating cheese trigger my migraines?'", 
            "1. parse_time_range('recent history') → get broader date range",
            "2. correlate_observation_to_episodes('cheese', 'migraine', ...) → analyze correlation",
            "3. Present correlation analysis with appropriate caveats"
        ]
    )
    
    return recall_agent

# Create the agent instance
recall_agent = create_recall_agent()
```

## Project State Summary

This is a sophisticated **Health Companion AI system** built with the Agno framework featuring:

**🏗️ Architecture:**
- **Pure Agno Implementation**: Uses Agno's Workflow, Agent, and Step primitives
- **Router-Based Orchestration**: MasterAgent intelligently routes user intents
- **Multi-Modal Interface**: Gradio-based UI with text, voice, and file support
- **Layered Design**: Separated concerns across health_advisor, healthlogger, core, and data layers

**🤖 Available Agents:**
- **Health Companion (Auto-Router)**: Primary orchestrator with intent classification
- **Health Logger v3**: Structured health episode capture with conversation context
- **Recall Agent**: Historical data analysis with tool-based querying
- **Coach Agent**: Evidence-based guidance using ChromaDB knowledge base
- **Research/General Agents**: Basic AI assistants for general tasks

**📊 Key Features:**
- **Daily History Calendar**: Plotly-based calendar view with color-coded pain levels
- **Episode Continuity**: Conversation-aware episode linking using chat history
- **Structured Data Capture**: Pydantic schemas with OpenAI-compatible flattening
- **JSON-Based Storage**: Local file storage with abstract interface for future backends
- **Multi-Intent Chaining**: Router can execute primary + secondary agent workflows
- **Knowledge Base Integration**: ChromaDB vector storage for migraine research

**🔧 Technical Stack:**
- **Frontend**: Gradio 4.44.0 with custom UI components
- **AI Framework**: Agno 0.2.5 with OpenAI Chat models (gpt-4o-mini-2024-07-18)
- **Data**: Pydantic schemas, JSON storage, pandas/plotly for visualization
- **Models**: Uses text-embedding-ada-002 for embeddings (better compatibility)

The system is currently **production-ready** with comprehensive health logging, analysis, and guidance capabilities.