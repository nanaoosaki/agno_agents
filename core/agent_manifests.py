# core/agent_manifests.py
# Agent Capability Manifest system for dynamic router configuration

from typing import Dict, List, Any
from dataclasses import dataclass

@dataclass
class AgentManifest:
    """Capability manifest for an agent."""
    name: str
    version: str
    intents_supported: List[str]
    cue_patterns: List[str]
    fewshot_examples: List[Dict[str, str]]
    description: str

# Agent Capability Manifests
AGENT_MANIFESTS = {
    "Health Logger (v3.1 Multi-Modal)": AgentManifest(
        name="Health Logger",
        version="3.1",
        intents_supported=["log"],
        cue_patterns=[
            r"I have.*migraine|headache|pain",
            r"feeling.*worse|better|symptoms",
            r"took.*medication|pills|dose",
            r"ate.*trigger|food|meal",
            r"sleep.*hours|tired|exhausted",
            r"stress.*work|family|anxiety"
        ],
        fewshot_examples=[
            {
                "input": "I have a terrible migraine right now, pain level 8",
                "intent": "log",
                "rationale": "User reporting current health episode with severity"
            },
            {
                "input": "Took 2 ibuprofen for my headache an hour ago",
                "intent": "log", 
                "rationale": "User logging intervention/medication taken"
            },
            {
                "input": "Feeling much better today, pain is down to a 3",
                "intent": "log",
                "rationale": "User reporting improvement in health status"
            }
        ],
        description="Logs health episodes, symptoms, medications, and interventions with structured data extraction"
    ),
    
    "Recall Agent (v2.1)": AgentManifest(
        name="Recall Agent", 
        version="2.1",
        intents_supported=["recall"],
        cue_patterns=[
            r"what.*yesterday|last week|last month",
            r"when.*did I|was my last",
            r"how.*often|many times|frequent",
            r"show.*history|pattern|trend",
            r"find.*episodes|data|records",
            r"remember.*what happened|when"
        ],
        fewshot_examples=[
            {
                "input": "What did my pain look like last week?",
                "intent": "recall",
                "rationale": "User requesting historical pain data analysis"
            },
            {
                "input": "When was my last migraine episode?",
                "intent": "recall",
                "rationale": "User asking for specific episode recall"
            },
            {
                "input": "How often do I get headaches?",
                "intent": "recall",
                "rationale": "User requesting frequency analysis"
            }
        ],
        description="Retrieves and analyzes historical health data, episodes, and patterns"
    ),
    
    "Coach Agent (v2.0)": AgentManifest(
        name="Coach Agent",
        version="2.0", 
        intents_supported=["coach"],
        cue_patterns=[
            r"what should I do|what can I do",
            r"help.*manage|cope|deal with",
            r"advice.*pain|migraine|symptoms", 
            r"suggest.*treatment|relief|strategy",
            r"recommend.*action|approach|plan",
            r"how.*prevent|avoid|reduce"
        ],
        fewshot_examples=[
            {
                "input": "What should I do about this migraine?",
                "intent": "coach",
                "rationale": "User seeking actionable advice for current episode"
            },
            {
                "input": "How can I prevent these headaches?",
                "intent": "coach", 
                "rationale": "User requesting prevention strategies"
            },
            {
                "input": "Any suggestions for managing stress-related pain?",
                "intent": "coach",
                "rationale": "User seeking management recommendations"
            }
        ],
        description="Provides personalized health coaching, advice, and management strategies"
    ),
    
    "Profile & Onboarding (v3.3 Structured)": AgentManifest(
        name="Profile & Onboarding",
        version="3.3",
        intents_supported=["profile"],
        cue_patterns=[
            r"add.*medication|supplement|drug",
            r"remove.*stop.*med|medication",
            r"update.*profile|info|details",
            r"change.*routine|schedule|habit",
            r"set.*goal|target|preference",
            r"modify.*communication|style"
        ],
        fewshot_examples=[
            {
                "input": "Add magnesium 400mg daily to my medications",
                "intent": "profile",
                "rationale": "User requesting medication addition to profile"
            },
            {
                "input": "Stop my morning vitamin D supplement",
                "intent": "profile",
                "rationale": "User requesting medication removal from profile"
            },
            {
                "input": "Update my communication style to be more detailed",
                "intent": "profile",
                "rationale": "User requesting profile setting change"
            }
        ],
        description="Manages user profile, medications, goals, and preferences with structured onboarding"
    )
}

def get_agent_manifest(agent_name: str) -> AgentManifest:
    """Get the capability manifest for a specific agent."""
    return AGENT_MANIFESTS.get(agent_name)

def get_all_manifests() -> Dict[str, AgentManifest]:
    """Get all agent capability manifests."""
    return AGENT_MANIFESTS

def generate_router_prompt(manifests: Dict[str, AgentManifest]) -> str:
    """Generate dynamic router prompt from agent manifests."""
    
    prompt_parts = [
        "You are a health companion router that classifies user intents and routes them to specialist agents.",
        "",
        "# Available Specialists:",
        ""
    ]
    
    # Add agent descriptions
    for agent_name, manifest in manifests.items():
        prompt_parts.extend([
            f"## {manifest.name} (v{manifest.version})",
            f"- **Intents**: {', '.join(manifest.intents_supported)}",
            f"- **Description**: {manifest.description}",
            f"- **Cue Patterns**: {'; '.join(manifest.cue_patterns[:3])}...",
            ""
        ])
    
    # Add few-shot examples
    prompt_parts.extend([
        "# Routing Examples:",
        ""
    ])
    
    for agent_name, manifest in manifests.items():
        for example in manifest.fewshot_examples[:2]:  # Limit to 2 examples per agent
            prompt_parts.extend([
                f"**Input**: \"{example['input']}\"",
                f"**Intent**: {example['intent']}",
                f"**Rationale**: {example['rationale']}",
                ""
            ])
    
    prompt_parts.extend([
        "# Routing Rules:",
        "- Return structured JSON with: intent, confidence (0.0-1.0), rationale",
        "- Supported intents: log, recall, coach, profile, unknown",
        "- If confidence < 0.5, use 'unknown' intent and ask for clarification",
        "- For combo utterances (e.g., 'I have a migraine, what should I do?'), choose primary intent",
        "- Control commands (/resolve) bypass normal routing",
        ""
    ])
    
    return "\n".join(prompt_parts)

def get_routing_examples_for_testing() -> List[Dict[str, Any]]:
    """Get labeled examples for router testing."""
    examples = []
    
    for manifest in AGENT_MANIFESTS.values():
        for example in manifest.fewshot_examples:
            examples.append({
                "input": example["input"],
                "expected_intent": example["intent"],
                "agent": manifest.name,
                "rationale": example["rationale"]
            })
    
    # Add some combo and edge case examples
    examples.extend([
        {
            "input": "I have a migraine, what should I do?",
            "expected_intent": "log",  # Primary intent
            "agent": "combo",
            "rationale": "Log first, then coach secondary"
        },
        {
            "input": "/resolve",
            "expected_intent": "control",
            "agent": "control",
            "rationale": "Control command for pending actions"
        },
        {
            "input": "Hello, how are you?",
            "expected_intent": "unknown",
            "agent": "clarification",
            "rationale": "No clear health intent, needs clarification"
        }
    ])
    
    return examples