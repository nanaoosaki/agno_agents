# health_advisor/coach/tools.py
# Following docs/agno/tools/writing_your_own_tools.md pattern

from agno.tools import tool
from typing import Optional, Dict, Any, List

# Import from the correct layers - following refactored architecture
from data.json_store import fetch_open_episode_candidates

def _fetch_active_episode_snapshot_core(window_hours: int = 72) -> Optional[Dict[str, Any]]:
    """
    Fetches a compact summary of the user's most recent open health episode
    for a specific condition to provide immediate context for coaching.
    Returns episode details including condition, severity, and recent interventions.
    """
    # Note: In a real app, the condition would be dynamically determined.
    # For MVP, we can hardcode or infer from the agent's context.
    condition = "migraine"  # This can be made dynamic later
    
    try:
        # Use existing storage function to find open episodes
        episode_candidates = fetch_open_episode_candidates(window_hours)
        
        # Filter candidates by condition if specified
        episodes = []
        for candidate in episode_candidates:
            # Convert EpisodeCandidate to dict for compatibility
            episode_data = {
                "episode_id": candidate.episode_id,
                "condition": candidate.condition,
                "started_at": candidate.started_at,
                "current_severity": candidate.current_severity,
                "salient": candidate.salient
            }
            # Filter by condition if needed
            if condition.lower() in candidate.condition.lower():
                episodes.append(episode_data)
        
        # If no specific condition match, return all recent episodes
        if not episodes and episode_candidates:
            episodes = [{
                "episode_id": candidate.episode_id,
                "condition": candidate.condition,
                "started_at": candidate.started_at,
                "current_severity": candidate.current_severity,
                "salient": candidate.salient
            } for candidate in episode_candidates]
        
        if episodes:
            # Get the most recent open episode
            latest_episode = episodes[0]  # Episodes are ordered by recency
            
            return {
                "condition": latest_episode.get("condition"),
                "current_severity": latest_episode.get("current_severity"),
                "started_at": latest_episode.get("started_at"),
                "episode_id": latest_episode.get("episode_id"),
                "salient_info": latest_episode.get("salient", "")
            }
        return None
    except Exception as e:
        print(f"Error fetching episode snapshot: {e}")
        return None

@tool
def fetch_active_episode_snapshot(window_hours: int = 72) -> Optional[Dict[str, Any]]:
    """
    Fetches a compact summary of the user's most recent open health episode.
    This tool provides context for coaching by retrieving details about ongoing episodes.
    """
    return _fetch_active_episode_snapshot_core(window_hours)

@tool
def get_coaching_snippets(topic: str, num_snippets: int = 2) -> List[str]:
    """
    Searches the Migraine Handout knowledge base for actionable, non-medication advice
    on a specific topic like 'lifestyle', 'triggers', 'stress', or 'hydration'.
    Returns practical tips from the migraine megahandout.
    """
    try:
        # Lazy import to avoid initialization issues
        from health_advisor.knowledge.loader import get_migraine_knowledge_base
        
        # Get the knowledge base with proper error handling
        migraine_knowledge_base = get_migraine_knowledge_base()
        if not migraine_knowledge_base:
            raise Exception("Knowledge base not available")
        
        # Search the knowledge base using the topic (handle different API versions)
        try:
            results = migraine_knowledge_base.search(query=topic, limit=num_snippets)
        except TypeError:
            # Fallback if limit parameter not supported
            results = migraine_knowledge_base.search(query=topic)
            if isinstance(results, list) and len(results) > num_snippets:
                results = results[:num_snippets]
        
        # Extract content from search results - handle Document objects
        snippets = []
        for result in results:
            # Handle different result formats (Document objects vs dicts)
            if hasattr(result, 'content'):
                content = result.content
            elif isinstance(result, dict):
                content = result.get("content", "")
            else:
                content = str(result)
                
            if content and len(content) > 50:  # Ensure we have meaningful content
                # Take first paragraph or first 300 characters for concise advice
                snippet = content.split('\n')[0] if '\n' in content else content
                snippet = snippet[:300] + "..." if len(snippet) > 300 else snippet
                snippets.append(snippet)
        
        return snippets if snippets else ["Focus on rest, hydration, and a dark quiet environment."]
    
    except Exception as e:
        print(f"Error searching knowledge base: {e}")
        # Return fallback advice if knowledge base is not available
        fallback_advice = {
            "stress": ["Practice deep breathing exercises for 5-10 minutes.", "Try gentle neck stretches to relieve tension."],
            "lifestyle": ["Maintain regular sleep schedule and meals.", "Stay hydrated with small sips of water throughout the day."],
            "triggers": ["Keep a quiet, dark environment.", "Avoid bright lights and loud sounds."],
            "hydration": ["Sip water slowly and regularly.", "Consider electrolyte replacement if needed."],
            "sleep": ["Maintain consistent sleep and wake times.", "Create a calm bedtime routine."]
        }
        
        # Try to match topic to fallback advice
        for key, advice_list in fallback_advice.items():
            if key in topic.lower():
                return advice_list[:num_snippets]
        
        return ["Focus on rest, hydration, and a dark quiet environment."]

@tool
def apply_safety_guardrails(proposed_advice: str) -> str:
    """
    Reviews a proposed piece of advice to ensure it is safe and non-prescriptive.
    It removes specific medical advice, dosage, or diagnoses and adds medication overuse warnings.
    """
    # Simple rule-based filter for MVP. Can be replaced with a dedicated safety agent later.
    unsafe_keywords = ["dosage", "mg", "prescription", "diagnose", "prescribe", "take medication", "increase dose"]
    
    # Check for specific medication instructions
    if any(keyword in proposed_advice.lower() for keyword in unsafe_keywords):
        return ("Based on general wellness principles, focusing on lifestyle factors like hydration, rest, "
                "and stress management can be beneficial. For specific medical advice, please consult a healthcare professional.")
    
    # Check for medication overuse mentions and add appropriate warnings
    medication_overuse_terms = ["frequent medication", "daily pain meds", "medication more than", "taking pills daily"]
    if any(term in proposed_advice.lower() for term in medication_overuse_terms):
        proposed_advice += ("\n\n⚠️ *Note: Frequent use of pain medication (more than 2-3 days per week) can sometimes "
                          "lead to medication overuse headaches. It's always a good idea to track usage and discuss "
                          "patterns with your doctor.*")
    
    # Ensure advice ends with a supportive note
    if not proposed_advice.strip().endswith((".", "!", "?")):
        proposed_advice += "."
    
    # Add general medical disclaimer if not present
    if "healthcare professional" not in proposed_advice.lower():
        proposed_advice += "\n\n*Always consult with a healthcare professional for persistent or severe symptoms.*"
    
    return proposed_advice