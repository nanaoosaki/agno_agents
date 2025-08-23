# profile_and_onboarding/updater_agent.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from typing import Dict, Any, List, Optional
from .schema import (
    ProposedProfileChange, ProfileChangeDetail, 
    MedicationChange, ConditionChange, RoutineChange
)
from .storage import get_profile_store
from core.ontology import normalize_condition

# Profile updater agent with confidence thresholds
profile_updater_agent = Agent(
    name="ProfileUpdaterAgent",
    model=OpenAIChat(id="gpt-4o-mini-2024-07-18"),
    response_model=ProposedProfileChange,
    add_history_to_messages=True,  # Context awareness
    num_history_runs=3,
    instructions=[
        "Analyze user messages for profile updates with high confidence.",
        "Only propose changes with confidence >= 0.7 for individual items.",
        "For low confidence items, add clarification questions instead of proposing changes.",
        "Use existing condition families from core.ontology for normalization.",
        "Ensure all medication changes include proper dosage and timing when mentioned.",
        "Be conservative - only propose changes that are clearly stated by the user.",
        "For medication updates: extract name, type (preventative/abortive/supplement/other), dose, schedule.",
        "For condition updates: extract name, severity if mentioned.",
        "For routine updates: extract category (sleep/hydration/exercise/stress/nutrition), pattern, frequency.",
        "If the user mentions stopping a medication, use action='deactivate'.",
        "If unsure about any detail, ask for clarification rather than guessing.",
        "Calculate overall_confidence as the average of all individual change confidences."
    ]
)

class ProfileUpdater:
    """Profile update handler with confidence-based processing"""
    
    def __init__(self):
        self.profile_store = get_profile_store()
    
    def process_update_request(self, message: str, user_id: str = "anonymous") -> dict:
        """Process a profile update request with confidence gating"""
        try:
            # Run the updater agent
            result = profile_updater_agent.run(message)
            
            # Check overall confidence and clarifications
            if result.overall_confidence < 0.7 or result.clarifications:
                # Low confidence or clarifications needed
                clarifications_text = "\n".join([f"• {q}" for q in result.clarifications])
                
                return {
                    "content": f"I need some clarification to update your profile accurately:\n\n{clarifications_text}\n\nPlease provide more specific information.",
                    "metadata": {
                        "requires_clarification": True,
                        "confidence": result.overall_confidence,
                        "clarifications": result.clarifications
                    }
                }
            
            # High confidence - prepare changes for confirmation
            if not result.changes:
                return {
                    "content": "I didn't detect any specific profile changes to make. Could you be more specific about what you'd like to update?",
                    "metadata": {"no_changes_detected": True}
                }
            
            # Format changes for user confirmation
            change_descriptions = []
            for change in result.changes:
                action_verb = {
                    "add": "Add",
                    "update": "Update", 
                    "deactivate": "Remove"
                }.get(change.action, "Modify")
                
                if change.entity == "medication":
                    med_desc = f"{action_verb} medication: {change.data.name}"
                    if hasattr(change.data, 'dose') and change.data.dose:
                        med_desc += f" ({change.data.dose})"
                    change_descriptions.append(med_desc)
                    
                elif change.entity == "condition":
                    cond_desc = f"{action_verb} condition: {change.data.name}"
                    if hasattr(change.data, 'severity') and change.data.severity:
                        cond_desc += f" (severity: {change.data.severity}/10)"
                    change_descriptions.append(cond_desc)
                    
                elif change.entity == "routine":
                    routine_desc = f"{action_verb} routine: {change.data.category} - {change.data.pattern}"
                    change_descriptions.append(routine_desc)
            
            changes_text = "\n".join([f"• {desc}" for desc in change_descriptions])
            
            return {
                "content": f"I'd like to make these changes to your profile:\n\n{changes_text}\n\nType '/resolve profile' to confirm these changes, or tell me what needs to be adjusted.",
                "metadata": {
                    "requires_confirmation": True,
                    "proposed_changes": result.model_dump(),
                    "confidence": result.overall_confidence
                }
            }
            
        except Exception as e:
            return {
                "content": f"Error processing profile update: {str(e)}",
                "metadata": {"error": True}
            }
    
    def commit_changes(
        self, 
        proposed_changes: ProposedProfileChange, 
        user_id: str,
        user_choice: str = "confirm"
    ) -> str:
        """Commit approved profile changes"""
        if user_choice.lower() != "confirm":
            return "Profile update cancelled. No changes made."
        
        try:
            changes_applied = []
            
            for change_detail in proposed_changes.changes:
                try:
                    if change_detail.entity == "medication":
                        if change_detail.action == "deactivate":
                            self.profile_store.deactivate_medication(
                                user_id, 
                                change_detail.data.name, 
                                source="chat"
                            )
                            changes_applied.append(f"Removed medication: {change_detail.data.name}")
                        else:
                            from .schema import Medication
                            medication = Medication(
                                name=change_detail.data.name,
                                type=change_detail.data.type,
                                dose=change_detail.data.dose,
                                schedule=change_detail.data.schedule,
                                prescriber=getattr(change_detail.data, 'prescriber', None),
                                source="chat"
                            )
                            self.profile_store.add_or_update_medication(user_id, medication, source="chat")
                            changes_applied.append(f"Updated medication: {medication.name}")
                    
                    elif change_detail.entity == "condition":
                        if change_detail.action == "deactivate":
                            self.profile_store.deactivate_condition(
                                user_id,
                                change_detail.data.name,
                                source="chat"
                            )
                            changes_applied.append(f"Removed condition: {change_detail.data.name}")
                        else:
                            from .schema import Condition
                            condition = Condition(
                                name=change_detail.data.name,
                                severity=getattr(change_detail.data, 'severity', None),
                                source="chat"
                            )
                            self.profile_store.add_or_update_condition(user_id, condition, source="chat")
                            changes_applied.append(f"Updated condition: {condition.name}")
                    
                    elif change_detail.entity == "routine":
                        from .schema import Routine
                        routine = Routine(
                            category=change_detail.data.category,
                            pattern=change_detail.data.pattern,
                            frequency=getattr(change_detail.data, 'frequency', None)
                        )
                        self.profile_store.add_or_update_routine(user_id, routine, source="chat")
                        changes_applied.append(f"Updated routine: {routine.category} - {routine.pattern}")
                        
                except Exception as e:
                    print(f"Error applying individual change: {e}")
                    continue
            
            if changes_applied:
                changes_text = "\n".join([f"✓ {change}" for change in changes_applied])
                return f"Successfully updated your profile:\n\n{changes_text}"
            else:
                return "No changes could be applied. Please check your profile data and try again."
                
        except Exception as e:
            return f"Error applying changes: {str(e)}"

# Global updater instance
profile_updater = ProfileUpdater()

def handle_profile_update(message: str, user_id: str = "anonymous") -> dict:
    """Handle profile update requests"""
    return profile_updater.process_update_request(message, user_id)

def commit_profile_changes(
    user_id: str,
    proposed_changes: ProposedProfileChange,
    user_choice: str,
) -> str:
    """Commit profile changes - deterministic function for orchestration"""
    return profile_updater.commit_changes(proposed_changes, user_id, user_choice)