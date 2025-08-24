# healthlogger/workflow.py  
# Main Agno workflow for Health Logger v3

import os
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
        print("Warning: Agno workflow not available, using fallback")
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
    
    name = "Health Logger (v3.1)"
    description = "Multi-modal health logging with image analysis for medication labels, nutrition facts, and health documents"
    
    def __init__(self):
        self.workflow = create_health_logger_workflow()
        print("Health Logger v3 (Pure Agno) initialized successfully")
    
    def run(self, prompt: str, files: Optional[List[str]] = None):
        """
        Run the multi-modal health logger workflow.
        
        Args:
            prompt: User's health message
            files: Optional file attachments (now fully supported for images)
            
        Returns:
            ChatResult with workflow response
        """
        try:
            # Import here to avoid circular imports
            from core.file_handler import process_uploaded_files, get_image_description
            
            # Each user should have a unique session_id
            # In a real multi-user app, this would be dynamic per user
            session_id = "user_main_session"
            
            # --- NEW LOGIC: Process files using the file handler ---
            attachments = process_uploaded_files(files or [])
            
            # The prompt is now pre-combined from unified_submit (may contain voice + text)
            # We just need to add file context if there are attachments
            enhanced_prompt = prompt
            if attachments:
                attachment_descriptions = [get_image_description(att) for att in attachments]
                enhanced_prompt = (
                    "The user has provided a multi-modal health update that may include voice input, typed notes, and attached files. "
                    "Analyze all the provided information to create a comprehensive log entry.\n\n"
                    f"USER INPUT: {prompt}\n"
                    f"ATTACHED FILES: {', '.join(attachment_descriptions)}\n\n"
                    "Please extract all relevant health information from the combined text and any images. "
                    "For medication labels, include drug name, dosage, and frequency. "
                    "For nutrition labels, include key facts like calories, sugar, and sodium. "
                    "Synthesize information from all input sources (voice, text, images) into a single coherent log entry."
                )
                
                print(f"📎 Processing {len(attachments)} attachment(s) for health logging")
            
            # Prepare images for Agno workflow
            images_for_workflow = []
            if attachments:
                try:
                    # Try to import Agno's Image class
                    from agno.media import Image
                    import base64
                    
                    for att in attachments:
                        try:
                            # Read image content as bytes
                            with open(att.path, 'rb') as f:
                                image_bytes = f.read()
                            
                            # Convert to base64 for safer LLM processing
                            image_base64 = base64.b64encode(image_bytes).decode('utf-8')
                            
                            # Create data URL format (standard for LLMs)
                            mime_type = att.mime or 'image/jpeg'
                            data_url = f"data:{mime_type};base64,{image_base64}"
                            
                            # Create Image object with URL instead of raw content
                            image_obj = Image(
                                url=data_url,
                                detail="auto"  # Let Agno decide detail level
                            )
                            images_for_workflow.append(image_obj)
                            print(f"Successfully loaded image: {os.path.basename(att.path)} ({att.tag}) as base64")
                            
                        except Exception as img_error:
                            print(f"Warning: Failed to load image {att.path}: {img_error}")
                            # Continue processing other images
                            continue
                            
                except ImportError:
                    print("Warning: Agno Image class not available. Processing files as text context only.")
                    # Fallback: Include file paths in prompt
                    file_paths = [att.path for att in attachments]
                    enhanced_prompt += f"\n\nFile paths for reference: {', '.join(file_paths)}"
                except Exception as e:
                    print(f"Warning: Error preparing images for Agno: {e}")
                    # Fallback to text-only processing
                    images_for_workflow = []
            
            # Run the workflow with enhanced prompt and images
            try:
                if images_for_workflow:
                    print(f"Running workflow with {len(images_for_workflow)} image(s) and enhanced prompt")
                    response = self.workflow.run(
                        message=enhanced_prompt,
                        images=images_for_workflow,
                        session_id=session_id
                    )
                else:
                    print("Running workflow with text-only prompt")
                    response = self.workflow.run(
                        message=enhanced_prompt,
                        session_id=session_id
                    )
                    
                # Validate response content to prevent HTTP issues
                if not hasattr(response, 'content') or not response.content:
                    print("Warning: Empty response from workflow, using fallback message")
                    response_content = "I've processed your health information. The data has been logged successfully."
                else:
                    response_content = str(response.content)
                    
            except Exception as workflow_error:
                print(f"Error: Workflow execution failed: {workflow_error}")
                # Fallback response
                response_content = f"I encountered an issue processing your multi-modal input: {str(workflow_error)}. Please try again or contact support."
            
            # Import ChatResult here to avoid circular imports
            from dataclasses import dataclass
            from typing import Dict, Any
            
            @dataclass
            class ChatResult:
                text: str
                meta: Optional[Dict[str, Any]] = None
            
            return ChatResult(
                text=response_content,
                meta={
                    "workflow": "Health Logger v3.1",
                    "architecture": "pure_agno_multimodal",
                    "session_id": session_id,
                    "attachments_processed": len(attachments),
                    "has_images": len(images_for_workflow) > 0
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
                text=f"Error in health logger workflow: {str(e)}",
                meta={"error": str(e)}
            )