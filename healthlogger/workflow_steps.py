# healthlogger/workflow_steps.py
# Deterministic workflow steps for Health Logger v3

from typing import Dict, Any, Optional, Tuple, List
from datetime import datetime, timedelta

try:
    from agno.workflow.v2 import StepInput, StepOutput
    AGNO_WORKFLOW_AVAILABLE = True
except ImportError:
    AGNO_WORKFLOW_AVAILABLE = False
    # Fallback types for development
    class StepInput:
        def __init__(self, previous_step_content=None, workflow_session_state=None):
            self.previous_step_content = previous_step_content
            self.workflow_session_state = workflow_session_state or {}
    
    class StepOutput:
        def __init__(self, content=None):
            self.content = content

from healthlogger.schema_router import RouterOutput, SimpleRouterOutput
from data.schemas.episodes import ProcessingResult, EpisodeCandidate
from core.ontology import CONDITION_FAMILIES, normalize_condition
from data.json_store import (
    fetch_open_episode_candidates, create_episode,
    update_episode, add_intervention, save_observation, append_event, get_episode_by_id
)

# Policy configuration - importing from core.policies
from core.policies import EPISODE_LINKING_WINDOW_HOURS

EPISODE_WINDOW_HOURS = EPISODE_LINKING_WINDOW_HOURS
DAY_BOUNDARY_HOURS = 24
CONFIDENCE_THRESHOLD = 0.6

def resolve_episode_action(
    router_output: RouterOutput,
    candidates: List[EpisodeCandidate], 
    session_episode_id: Optional[str],
    now: datetime
) -> Tuple[str, Optional[str], bool, Optional[Dict[str, Any]]]:
    """
    Deterministic core logic to resolve what action to take.
    
    Args:
        router_output: Structured data from Extractor
        candidates: Available episode candidates 
        session_episode_id: Current session's open episode
        now: Current timestamp
        
    Returns:
        Tuple of (action, episode_id, needs_clarification, clarification_data)
    """
    
    # Handle non-episode intents
    if router_output.intent == "observation":
        return ("observation", None, False, None)
    if router_output.intent == "query":
        return ("query", None, False, None)
    
    condition = router_output.condition
    link_strategy = router_output.episode_link.link_strategy
    suggested_episode_id = router_output.episode_link.episode_id
    confidence = router_output.confidence
    
    # Low confidence triggers clarification
    if confidence < CONFIDENCE_THRESHOLD:
        if candidates:
            clarification = _create_clarification(candidates, condition)
            return ("clarify", None, True, clarification)
        else:
            # No candidates, just create new
            return ("create", None, False, None)
    
    # Find best candidate match
    best_candidate = _find_best_candidate(
        condition, candidates, suggested_episode_id, session_episode_id, now
    )
    
    # Handle intervention-only messages
    if router_output.intent == "intervention":
        if best_candidate:
            return ("update", best_candidate.episode_id, False, None)
        elif condition:
            return ("create", None, False, None)  # Create minimal episode for intervention
        else:
            return ("observation", None, False, None)  # Generic intervention
    
    # Main episode logic
    if link_strategy == "same_episode":
        if best_candidate and _is_episode_recent(best_candidate, now, EPISODE_WINDOW_HOURS):
            return ("update", best_candidate.episode_id, False, None)
        elif best_candidate:
            # LLM suggested same but episode is stale - might need clarification
            if len(candidates) > 1:
                clarification = _create_clarification(candidates, condition)
                return ("clarify", None, True, clarification)
            else:
                return ("create", None, False, None)
        else:
            return ("create", None, False, None)
    
    elif link_strategy == "new_episode":
        return ("create", None, False, None)
    
    else:  # unknown strategy
        if best_candidate and _is_episode_recent(best_candidate, now, EPISODE_WINDOW_HOURS):
            # Check for continuity signals in text
            if _has_continuity_signals(router_output.fields.notes or ""):
                return ("update", best_candidate.episode_id, False, None)
            elif len(candidates) > 1:
                # Multiple candidates - ask for clarification
                clarification = _create_clarification(candidates, condition)
                return ("clarify", None, True, clarification)
        
        return ("create", None, False, None)

def _find_best_candidate(
    condition: Optional[str],
    candidates: List[EpisodeCandidate],
    suggested_id: Optional[str],
    session_id: Optional[str], 
    now: datetime
) -> Optional[EpisodeCandidate]:
    """Find the best matching episode candidate"""
    
    if not candidates:
        return None
    
    # Try suggested episode ID first
    if suggested_id:
        for candidate in candidates:
            if candidate.episode_id == suggested_id:
                return candidate
    
    # Try session preference
    if session_id:
        for candidate in candidates:
            if candidate.episode_id == session_id:
                return candidate
    
    # Find condition matches
    condition_matches = []
    if condition:
        for candidate in candidates:
            if _conditions_match(condition, candidate.condition):
                condition_matches.append(candidate)
    
    if condition_matches:
        # Return most recent condition match
        return condition_matches[0]  # Already sorted by recency
    
    # Return most recent candidate if no condition match
    return candidates[0] if candidates else None

def _conditions_match(condition1: str, condition2: str) -> bool:
    """Check if two conditions are in the same family"""
    if condition1 == condition2:
        return True
    
    # Check condition families
    for family, conditions in CONDITION_FAMILIES.items():
        if condition1 in conditions and condition2 in conditions:
            return True
    
    return False

def _is_episode_recent(candidate: EpisodeCandidate, now: datetime, window_hours: int) -> bool:
    """Check if episode was updated recently enough"""
    try:
        last_updated = datetime.fromisoformat(candidate.last_updated_at.replace('Z', '+00:00'))
        return (now - last_updated).total_seconds() <= window_hours * 3600
    except ValueError:
        return False

def _has_continuity_signals(text: str) -> bool:
    """Check for signals indicating episode continuation"""
    if not text:
        return False
    
    continuity_words = [
        "still", "ongoing", "continues", "same", "it's", "now", 
        "down to", "up to", "currently", "remains", "persists"
    ]
    
    text_lower = text.lower()
    return any(word in text_lower for word in continuity_words)

def _create_clarification(candidates: List[EpisodeCandidate], condition: Optional[str]) -> Dict[str, Any]:
    """Create clarification options for user"""
    options = []
    
    # Add update options for recent candidates
    for candidate in candidates[:3]:  # Limit to 3 options
        if condition and _conditions_match(condition, candidate.condition):
            options.append({
                "label": f"Update {candidate.condition} from {candidate.started_at[:10]}",
                "action": "update",
                "episode_id": candidate.episode_id,
                "description": candidate.salient
            })
    
    # Add create new option
    options.append({
        "label": f"Create new {condition or 'episode'}",
        "action": "create", 
        "episode_id": None,
        "description": "Start tracking a new episode"
    })
    
    return {
        "message": f"I see you mentioned {condition or 'health information'}. Should I:",
        "options": options
    }

def process_and_log_step(step_input: StepInput) -> StepOutput:
    """
    Main deterministic processing step for the workflow.
    Processes extracted health data and commits to storage.
    """
    
    # Get router output from previous step and convert if needed
    previous_content = step_input.previous_step_content
    
    # Convert SimpleRouterOutput to RouterOutput if needed
    if isinstance(previous_content, SimpleRouterOutput):
        router_output = RouterOutput.from_simple(previous_content)
    elif isinstance(previous_content, dict):
        # Try to parse as SimpleRouterOutput first
        try:
            simple_output = SimpleRouterOutput(**previous_content)
            router_output = RouterOutput.from_simple(simple_output)
        except Exception:
            # Fallback to direct RouterOutput parsing
            router_output = RouterOutput(**previous_content)
    else:
        router_output = previous_content
    
    # TODO: Figure out proper session state access in Agno v2
    # For now, use a simple approach without persistent session state
    session_state = {}
    now = datetime.utcnow()
    
    # Check for pending disambiguation resolution
    if session_state.get("pending_disambiguation"):
        return _handle_disambiguation_resolution(step_input, now)
    
    # Fetch current episode candidates for context
    candidates = fetch_open_episode_candidates(window_hours=24)
    
    # Get session's current episode
    session_episode_id = session_state.get("open_episode_id")
    
    # Resolve what action to take
    action, episode_id, needs_clarification, clarification_data = resolve_episode_action(
        router_output, candidates, session_episode_id, now
    )
    
    # Handle clarification needed
    if needs_clarification:
        session_state["pending_disambiguation"] = {
            "router_output": router_output.dict(),
            "clarification": clarification_data,
            "timestamp": now.isoformat()
        }
        
        result = ProcessingResult(
            action_taken="clarify",
            needs_clarification=True,
            clarification_options=clarification_data["options"],
            details=[clarification_data["message"]]
        )
        return StepOutput(content=result)
    
    # Execute the determined action
    details = []
    final_episode_id = None
    
    try:
        if action == "create":
            final_episode_id = create_episode(
                condition=router_output.condition or "general",
                fields=router_output.fields.dict(),
                now=now.isoformat()
            )
            details.append(f"Created new {router_output.condition} episode")
            session_state["open_episode_id"] = final_episode_id
            
        elif action == "update":
            final_episode_id = episode_id
            success = update_episode(
                episode_id=episode_id,
                fields=router_output.fields.dict(),
                now=now.isoformat()
            )
            if success:
                details.append(f"Updated {router_output.condition} episode")
                if router_output.fields.severity:
                    details.append(f"Severity: {router_output.fields.severity}/10")
                session_state["open_episode_id"] = final_episode_id
            else:
                details.append("Failed to update episode")
                
        elif action == "observation":
            obs_id = save_observation(
                category=router_output.condition or "general",
                fields=router_output.fields.dict(),
                now=now.isoformat()
            )
            details.append(f"Saved {router_output.condition or 'general'} observation")
            
        # Handle interventions
        for intervention in router_output.interventions:
            if final_episode_id:
                int_id = add_intervention(
                    episode_id=final_episode_id,
                    intervention=intervention.dict(),
                    now=now.isoformat()
                )
                details.append(f"Added intervention: {intervention.type}")
            elif action == "observation":
                # Intervention without episode - save as observation
                obs_id = save_observation(
                    category="intervention",
                    fields={"type": intervention.type, "notes": intervention.notes},
                    now=now.isoformat()
                )
                details.append(f"Recorded intervention: {intervention.type}")
        
        # Log event for audit trail
        append_event(
            user_text=router_output.fields.notes or "",
            parsed_data=router_output.dict(),
            action=action,
            model="gpt-4o-mini-2024-07-18",
            confidence=router_output.confidence,
            episode_id=final_episode_id
        )
        
    except Exception as e:
        details.append(f"Error: {str(e)}")
        action = "error"
    
    # Create result
    result = ProcessingResult(
        action_taken=action,
        condition=router_output.condition,
        episode_id=final_episode_id,
        details=details,
        needs_clarification=False
    )
    
    return StepOutput(content=result)

def _handle_disambiguation_resolution(step_input: StepInput, now: datetime) -> StepOutput:
    """Handle user's response to disambiguation prompt"""
    
    session_state = step_input.workflow_session_state
    disambiguation_data = session_state["pending_disambiguation"]
    
    # The user's message should contain their choice
    # In a real implementation, this would parse the user's response
    # For now, we'll clear the disambiguation and proceed with create
    
    # Clear pending disambiguation
    del session_state["pending_disambiguation"]
    
    # Create new episode (default choice)
    router_output = RouterOutput(**disambiguation_data["router_output"])
    
    final_episode_id = create_episode(
        condition=router_output.condition or "general",
        fields=router_output.fields.dict(),
        now=now.isoformat()
    )
    
    session_state["open_episode_id"] = final_episode_id
    
    result = ProcessingResult(
        action_taken="create",
        condition=router_output.condition,
        episode_id=final_episode_id,
        details=[f"Created new {router_output.condition} episode"],
        needs_clarification=False
    )
    
    return StepOutput(content=result)