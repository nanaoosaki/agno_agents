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