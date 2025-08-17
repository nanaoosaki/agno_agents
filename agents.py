# agents.py
# Following docs/agno/core/running_your_agent.md and docs/agno/misc/basic_agents.md
import os
from dataclasses import dataclass
from typing import Dict, Any, Optional, List
from dotenv import load_dotenv

# Agno imports
try:
    from agno.agent import Agent, RunResponse
    from agno.models.openai import OpenAIChat
    from agno.tools.duckduckgo import DuckDuckGoTools
    from agno.tools.website import WebsiteTools
except ImportError as e:
    print(f"Warning: Agno imports failed: {e}")
    # Fallback for development/testing
    Agent = object
    RunResponse = object
    OpenAIChat = object
    DuckDuckGoTools = object
    WebsiteTools = object

load_dotenv()

@dataclass
class ChatResult:
    text: str
    meta: Optional[Dict[str, Any]] = None

# --- Example 1: Echo Agent (no external calls, for testing) ---
class EchoAgent:
    name = "EchoAgent"
    description = "Simple echo agent for testing - repeats your input"

    def run(self, prompt: str, files: Optional[List[str]] = None) -> ChatResult:
        suffix = ""
        if files:
            suffix = f"\n\n📁 **Files received:** {len(files)} file(s)"
            for file in files[:3]:  # Show first 3 files
                suffix += f"\n  - {os.path.basename(file)}"
            if len(files) > 3:
                suffix += f"\n  - ... and {len(files) - 3} more"
        
        response_text = f"🔄 **Echo:** {prompt}{suffix}"
        return ChatResult(text=response_text)

# --- Example 2: Research Agent with Agno integration ---
class ResearchAgent:
    name = "ResearchAgent"
    description = "AI research agent powered by Agno with web search capabilities"

    def __init__(self):
        try:
            # Following docs/agno/misc/basic_agents.md pattern
            self.agent = Agent(
                name="Research Assistant",
                model=OpenAIChat(id="gpt-4o-mini-2024-07-18"),  # Using correct model ID from workspace rules
                instructions="""You are a helpful research assistant. When asked questions:
1. Search for current information using available tools
2. Provide comprehensive, well-structured answers
3. Include sources and references when possible
4. If files are attached, analyze them in context of the question""",
                tools=[DuckDuckGoTools(), WebsiteTools()],
                add_history_to_messages=True,
                markdown=True,
                stream=True
            )
        except Exception as e:
            print(f"Warning: Could not initialize ResearchAgent: {e}")
            self.agent = None

    def run(self, prompt: str, files: Optional[List[str]] = None) -> ChatResult:
        if not self.agent:
            return ChatResult(
                text="❌ ResearchAgent is not available. Please check your Agno installation and API keys.",
                meta={"error": "agent_not_initialized"}
            )

        try:
            # Add file context to prompt if files are provided
            enhanced_prompt = prompt
            if files:
                file_info = f"\n\nAttached files: {', '.join([os.path.basename(f) for f in files])}"
                enhanced_prompt = f"{prompt}{file_info}"

            # Following docs/agno/core/running_your_agent.md
            response = self.agent.run(enhanced_prompt)
            
            # Extract text content from RunResponse
            response_text = getattr(response, 'content', str(response))
            
            return ChatResult(
                text=response_text,
                meta={
                    "model": getattr(response, 'model', None),
                    "metrics": getattr(response, 'metrics', None)
                }
            )
        except Exception as e:
            return ChatResult(
                text=f"❌ Error running research agent: {str(e)}",
                meta={"error": str(e)}
            )

# --- Example 3: General Purpose Agent ---
class GeneralAgent:
    name = "GeneralAgent"
    description = "General purpose AI assistant for various tasks"

    def __init__(self):
        try:
            self.agent = Agent(
                name="General Assistant",
                model=OpenAIChat(id="gpt-4o-mini-2024-07-18"),
                instructions="""You are a helpful AI assistant. You can:
- Answer questions on various topics
- Help with analysis and problem-solving
- Process and analyze attached files
- Provide explanations and tutorials
- Assist with creative tasks

Always be helpful, accurate, and provide well-structured responses.""",
                add_history_to_messages=True,
                markdown=True,
            )
        except Exception as e:
            print(f"Warning: Could not initialize GeneralAgent: {e}")
            self.agent = None

    def run(self, prompt: str, files: Optional[List[str]] = None) -> ChatResult:
        if not self.agent:
            return ChatResult(
                text="❌ GeneralAgent is not available. Please check your Agno installation and API keys.",
                meta={"error": "agent_not_initialized"}
            )

        try:
            enhanced_prompt = prompt
            if files:
                file_info = f"\n\nNote: User has attached {len(files)} file(s): {', '.join([os.path.basename(f) for f in files])}"
                enhanced_prompt = f"{prompt}{file_info}"

            response = self.agent.run(enhanced_prompt)
            response_text = getattr(response, 'content', str(response))
            
            return ChatResult(
                text=response_text,
                meta={
                    "model": getattr(response, 'model', None),
                    "metrics": getattr(response, 'metrics', None)
                }
            )
        except Exception as e:
            return ChatResult(
                text=f"❌ Error running general agent: {str(e)}",
                meta={"error": str(e)}
            )

# Health Logger v3 import
try:
    from healthlogger.workflow import HealthLoggerWorkflowWrapper
    health_logger_v3 = HealthLoggerWorkflowWrapper()
except ImportError as e:
    print(f"Warning: Health Logger v3 not available: {e}")
    health_logger_v3 = None

# Recall Agent import - Following docs/agno/tools/writing_your_own_tools.md
try:
    from health_advisor.recall.agent import recall_agent
    
    class RecallAgentWrapper:
        name = "Recall Agent"
        description = "Analyzes historical health data patterns and correlations using intelligent querying"
        
        def run(self, prompt: str, files: Optional[List[str]] = None) -> ChatResult:
            """Run the Recall Agent with the user's query"""
            try:
                response = recall_agent.run(prompt)
                return ChatResult(
                    text=response.content,
                    meta={
                        "agent": "RecallAgent",
                        "model": "gpt-4o-mini-2024-07-18",
                        "tool_calls": getattr(response, 'tool_calls', None),
                        "metrics": getattr(response, 'metrics', None)
                    }
                )
            except Exception as e:
                return ChatResult(
                    text=f"❌ Error running recall agent: {str(e)}",
                    meta={"error": str(e), "agent": "RecallAgent"}
                )
    
    recall_agent_wrapper = RecallAgentWrapper()
except ImportError as e:
    print(f"Warning: Recall Agent not available: {e}")
    recall_agent_wrapper = None

# Coach Agent import - Following docs/agno/core/what_are_agents.md
try:
    from health_advisor.coach.agent import coach_agent
    
    class CoachAgentWrapper:
        name = "Coach Agent"
        description = "Provides empathetic, non-medication health guidance based on current episode and migraine knowledge base"
        
        def __init__(self):
            self._knowledge_loaded = False
        
        def _ensure_knowledge_loaded(self):
            """Lazy load knowledge base only when first needed"""
            if not self._knowledge_loaded:
                try:
                    from health_advisor.knowledge.loader import load_knowledge_if_needed
                    load_knowledge_if_needed()
                    self._knowledge_loaded = True
                    print("✅ Coach knowledge base loaded successfully")
                except Exception as e:
                    print(f"Warning: Coach knowledge base could not be loaded: {e}")
                    print("Coach Agent will use fallback advice instead")
                    self._knowledge_loaded = False
        
        def run(self, prompt: str, files: Optional[List[str]] = None) -> ChatResult:
            """Run the Coach Agent with the user's query"""
            try:
                # Try to load knowledge base on first use
                self._ensure_knowledge_loaded()
                
                response = coach_agent.run(prompt)
                return ChatResult(
                    text=response.content,
                    meta={
                        "agent": "CoachAgent",
                        "model": "gpt-4o-mini-2024-07-18",
                        "tool_calls": getattr(response, 'tool_calls', None),
                        "metrics": getattr(response, 'metrics', None),
                        "knowledge_available": self._knowledge_loaded
                    }
                )
            except Exception as e:
                return ChatResult(
                    text=f"❌ Error running coach agent: {str(e)}",
                    meta={"error": str(e), "agent": "CoachAgent"}
                )
    
    coach_agent_wrapper = CoachAgentWrapper()
except ImportError as e:
    print(f"Warning: Coach Agent not available: {e}")
    coach_agent_wrapper = None

# Router Agent import - Following router_agent_implementation_plan.md
try:
    from health_advisor.router.agent import router_agent
    from health_advisor.router.schema import RouterDecision
    
    # --- THE NEW, STATEFUL MASTER ORCHESTRATOR ---
    class MasterAgent:
        name = "Health Companion"
        description = "Intelligent orchestrator that routes to the right specialist based on your needs"
        
        def __init__(self):
            self.session_storage = {}  # Simple in-memory session storage for MVP
        
        def _get_session_state(self, session_id: str) -> Dict[str, Any]:
            """Get or create session state for a given session ID"""
            if session_id not in self.session_storage:
                self.session_storage[session_id] = {
                    "pending_action": None,
                    "open_episode_id": None,
                    "conversation_context": []
                }
            return self.session_storage[session_id]
        
        def run(self, prompt: str, files: Optional[List[str]] = None) -> ChatResult:
            print(f"\n--- MasterAgent: Routing user prompt: '{prompt}' ---")
            
            # In a real app, session_id would be managed per user conversation.
            # We use a fixed one here for simplicity.
            session_id = "user_main_session"
            session_state = self._get_session_state(session_id)
            
            # 1. HANDLE CONTROL MESSAGES & PENDING ACTIONS (SHORT-CIRCUIT)
            if prompt.startswith("/resolve") and session_state.get("pending_action"):
                print("--> Handling resolved action directly.")
                # For MVP, we'll just clear the pending action
                session_state["pending_action"] = None
                return ChatResult(
                    text="✅ Action resolved successfully.",
                    meta={"action": "control_resolved", "session_id": session_id}
                )
            
            # 2. GET ROUTING DECISION (STATE-AWARE)
            try:
                router_response = router_agent.run(prompt)
                
                # Handle both structured and text responses
                if hasattr(router_response, 'content') and isinstance(router_response.content, RouterDecision):
                    decision = router_response.content
                elif hasattr(router_response, 'content'):
                    # Fallback if structured output fails
                    print("⚠️ Router returned non-structured response. Defaulting to logger.")
                    decision = RouterDecision(
                        primary_intent="log",
                        secondary_intent=None,
                        confidence=0.5,
                        rationale="Router failed to return structured output"
                    )
                else:
                    raise Exception("Invalid router response format")
                    
            except Exception as e:
                print(f"⚠️ Router agent failed: {e}. Defaulting to logger.")
                decision = RouterDecision(
                    primary_intent="log",
                    secondary_intent=None,
                    confidence=0.3,
                    rationale="Router agent error - defaulting to health logging"
                )
            
            print(f"🧠 Router Decision: Primary='{decision.primary_intent}', Secondary='{decision.secondary_intent}', Confidence={decision.confidence:.2f}")
            print(f"📝 Rationale: {decision.rationale}")
            
            # 3. APPLY CONFIDENCE THRESHOLDS & HEURISTICS
            final_intent = decision.primary_intent
            if decision.confidence < 0.7:
                # Simple heuristic fallback
                if any(word in prompt.lower() for word in ["when", "did i", "show me", "history", "last time"]):
                    final_intent = "recall"
                elif any(word in prompt.lower() for word in ["what should i do", "help", "advice", "recommend"]):
                    final_intent = "coach"
                print(f"⚠️ Confidence low ({decision.confidence:.2f}), applying heuristic. Final intent: '{final_intent}'")
            
            # 4. EXECUTE THE WORKFLOW (potentially multi-step)
            primary_result = None
            if final_intent == "recall":
                print("--> Routing to Recall Specialist")
                if recall_agent_wrapper:
                    primary_result = recall_agent_wrapper.run(prompt, files)
                else:
                    primary_result = ChatResult(text="❌ Recall Agent not available", meta={"error": "agent_unavailable"})
            
            elif final_intent == "coach":
                print("--> Routing to Coach Specialist")
                if coach_agent_wrapper:
                    primary_result = coach_agent_wrapper.run(prompt, files)
                else:
                    primary_result = ChatResult(text="❌ Coach Agent not available", meta={"error": "agent_unavailable"})
            
            elif final_intent == "control_action":
                print("--> Handling control action")
                primary_result = ChatResult(
                    text="🤖 Control action received. Use specific commands like '/resolve' for actions.",
                    meta={"action": "control_acknowledged"}
                )
            
            elif final_intent == "unknown":
                print("--> Unknown intent - asking for clarification")
                primary_result = ChatResult(
                    text="I'm not sure what you'd like me to help with. You can:\n• Log health information (e.g., 'I have a headache')\n• Ask about your history (e.g., 'Show me my recent episodes')\n• Get advice (e.g., 'What should I do for this pain?')",
                    meta={"action": "clarification_request"}
                )
            
            else:  # Default to logger (including "log" and "clarify_response")
                print("--> Routing to Logger Workflow")
                if health_logger_v3:
                    primary_result = health_logger_v3.run(prompt, files)
                else:
                    primary_result = ChatResult(text="❌ Health Logger not available", meta={"error": "agent_unavailable"})
            
            # 5. HANDLE SECONDARY INTENT (CHAINING)
            if decision.secondary_intent and primary_result and not primary_result.text.startswith("❌"):
                print(f"--- Handling secondary intent: '{decision.secondary_intent}' ---")
                
                if decision.secondary_intent == "coach" and coach_agent_wrapper:
                    print("--> Chaining to Coach Specialist")
                    secondary_result = coach_agent_wrapper.run(
                        "Given what I just told you, what should I do?", 
                        files=None
                    )
                    # Combine the results
                    combined_text = f"{primary_result.text}\n\n---\n\n**🩺 Health Guidance:**\n{secondary_result.text}"
                    return ChatResult(
                        text=combined_text,
                        meta={
                            "primary_agent": final_intent,
                            "secondary_agent": decision.secondary_intent,
                            "router_confidence": decision.confidence,
                            "chained_response": True
                        }
                    )
                
                elif decision.secondary_intent == "recall" and recall_agent_wrapper:
                    print("--> Chaining to Recall Specialist")
                    secondary_result = recall_agent_wrapper.run(
                        "Show me recent episodes related to what I just mentioned",
                        files=None
                    )
                    combined_text = f"{primary_result.text}\n\n---\n\n**📊 Related History:**\n{secondary_result.text}"
                    return ChatResult(
                        text=combined_text,
                        meta={
                            "primary_agent": final_intent,
                            "secondary_agent": decision.secondary_intent,
                            "router_confidence": decision.confidence,
                            "chained_response": True
                        }
                    )
            
            # Add routing metadata to the response
            if primary_result:
                if not primary_result.meta:
                    primary_result.meta = {}
                primary_result.meta.update({
                    "routed_by": "MasterAgent",
                    "final_intent": final_intent,
                    "router_confidence": decision.confidence,
                    "had_secondary_intent": decision.secondary_intent is not None
                })
            
            return primary_result if primary_result else ChatResult(
                text="❌ Unknown error in routing",
                meta={"error": "routing_failure"}
            )
    
    master_agent = MasterAgent()
    
except ImportError as e:
    print(f"Warning: Router Agent not available: {e}")
    master_agent = None

# Registry of available agents
AGENTS: Dict[str, Any] = {
    "EchoAgent": EchoAgent(),
    "ResearchAgent": ResearchAgent(),
    "GeneralAgent": GeneralAgent(),
}

# Add Health Logger v3 if available
if health_logger_v3:
    AGENTS["Health Logger (v3)"] = health_logger_v3

# Add Recall Agent if available
if recall_agent_wrapper:
    AGENTS["Recall Agent"] = recall_agent_wrapper

# Add Coach Agent if available
if coach_agent_wrapper:
    AGENTS["Coach Agent"] = coach_agent_wrapper

# Add Master Agent (Health Companion) if available - This should be the DEFAULT
if master_agent:
    AGENTS["Health Companion (Auto-Router)"] = master_agent

def call_agent(agent_name: str, user_text: str, filepaths: Optional[List[str]] = None) -> ChatResult:
    """
    Call the specified agent with user input and optional file attachments.
    
    Args:
        agent_name: Name of the agent to use
        user_text: User's text input
        filepaths: List of file paths (optional)
    
    Returns:
        ChatResult with the agent's response
    """
    agent = AGENTS.get(agent_name)
    if not agent:
        return ChatResult(
            text=f"❌ Unknown agent: {agent_name}. Available agents: {', '.join(AGENTS.keys())}",
            meta={"error": "unknown_agent"}
        )
    
    try:
        return agent.run(user_text, files=filepaths)
    except Exception as e:
        return ChatResult(
            text=f"❌ Error calling agent {agent_name}: {str(e)}",
            meta={"error": str(e), "agent": agent_name}
        )

def get_agent_info() -> Dict[str, str]:
    """Get information about all available agents."""
    return {name: getattr(agent, 'description', 'No description available') 
            for name, agent in AGENTS.items()}