# generate_fake_data_simple.py  
# Script to generate realistic fake health data for Recall Agent testing
# Based on patterns from real_user_messages/ directory
# Author: Claude (Anthropic AI Assistant)
# Date: January 16, 2025

import json
import random
from datetime import datetime, timedelta
import os

def generate_fake_episodes():
    """Generate fake episodes with realistic patterns"""
    
    conditions = ["migraine", "neck_pain", "back_pain", "anxiety", "reflux", "sleep"]
    locations = {
        "migraine": ["right temple", "left temple", "behind eyes", "forehead", "back of head"],
        "neck_pain": ["left neck", "right neck", "base of skull", "cervical area"],
        "back_pain": ["lower back", "upper back", "between shoulder blades", "lumbar"]
    }
    
    triggers = [
        ["weather change", "humidity"], ["spicy food", "indian food"], ["stress", "work pressure"],
        ["poor sleep", "late bedtime"], ["new pillow", "poor posture"], ["dehydration", "caffeine"],
        ["bright lights", "screen time"], ["hormone changes"], ["anxiety", "argument"]
    ]
    
    interventions = [
        {"type": "ibuprofen", "dose": "400mg"}, {"type": "salonpas patches", "dose": None},
        {"type": "heat therapy", "dose": None}, {"type": "ubrelvy", "dose": "100mg"},
        {"type": "rest", "dose": None}, {"type": "mint essential oil", "dose": None},
        {"type": "stretching", "dose": None}, {"type": "hydration", "dose": "32oz"}
    ]
    
    episodes = {}
    events = []
    
    print("Generating episodes...")
    
    # Generate 30 episodes over last 60 days
    base_date = datetime.now() - timedelta(days=60)
    
    for i in range(30):
        # Random date
        days_offset = random.randint(0, 60)
        episode_date = base_date + timedelta(days=days_offset)
        episode_date = episode_date.replace(hour=random.randint(8, 20), minute=random.randint(0, 59))
        
        condition = random.choice(conditions)
        severity = random.randint(1, 9) if condition != "sleep" else None
        
        episode_id = f"ep_{episode_date.strftime('%Y-%m-%d')}_{condition}_{random.randint(10000, 99999)}"
        
        # User messages based on real patterns
        user_messages = [
            f"I have a {condition} starting about an hour ago. Pain level is {severity}/10.",
            f"The {condition} is getting worse. It's mainly on my {random.choice(locations.get(condition, ['head']))}.",
            f"I think the {condition} was triggered by {random.choice(random.choice(triggers))}.",
            f"I'm having another {condition} episode. This is the third one this week.",
            f"The pain in my {random.choice(locations.get(condition, ['head']))} is at {severity}/10 now."
        ]
        
        selected_triggers = random.choice(triggers)
        selected_interventions = random.sample(interventions, random.randint(1, 3))
        
        episode = {
            "episode_id": episode_id,
            "condition": condition,
            "started_at": episode_date.isoformat(),
            "ended_at": None,
            "status": random.choice(["open", "closed"]),
            "current_severity": severity,
            "max_severity": severity,
            "severity_points": [{"ts": episode_date.isoformat(), "level": severity}] if severity else [],
            "notes_log": [
                {
                    "ts": episode_date.isoformat(),
                    "text": random.choice(user_messages)
                }
            ],
            "interventions": [
                {
                    "ts": (episode_date + timedelta(minutes=random.randint(30, 180))).isoformat(),
                    "type": interv["type"],
                    "dose": interv["dose"],
                    "notes": f"Applied for {condition}"
                }
                for interv in selected_interventions
            ],
            "last_updated_at": episode_date.isoformat()
        }
        
        episodes[episode_id] = episode
        
        # Generate corresponding event
        event = {
            "event_id": f"evt_{random.randint(10000000, 99999999)}",
            "timestamp": episode_date.isoformat(),
            "user_text": random.choice(user_messages),
            "parsed_data": {
                "intent": "episode_create",
                "condition": condition,
                "fields": {
                    "severity": severity,
                    "location": random.choice(locations.get(condition, ["head"])),
                    "triggers": selected_triggers,
                    "notes": random.choice(user_messages)
                },
                "episode_link": {"link_strategy": "new_episode", "episode_id": episode_id},
                "interventions": [{"type": interv["type"], "dose": interv["dose"]} for interv in selected_interventions],
                "confidence": round(random.uniform(0.8, 0.95), 2)
            },
            "action": "create",
            "model": "gpt-4o-mini-2024-07-18",
            "episode_id": episode_id
        }
        events.append(event)
        
        # 40% chance of follow-up
        if random.random() < 0.4:
            update_date = episode_date + timedelta(hours=random.randint(2, 12))
            new_severity = max(1, severity - random.randint(1, 3)) if severity else None
            
            update_messages = [
                f"The {condition} is better now. Pain down to {new_severity}/10.",
                f"I took {selected_interventions[0]['type']} and it's helping. Now at {new_severity}/10.",
                f"Pain is improving. {new_severity}/10 after treatment.",
                f"The {condition} is almost gone. Just {new_severity}/10 now."
            ]
            
            # Update episode
            episode["current_severity"] = new_severity
            episode["severity_points"].append({"ts": update_date.isoformat(), "level": new_severity})
            episode["notes_log"].append({
                "ts": update_date.isoformat(),
                "text": random.choice(update_messages)
            })
            episode["last_updated_at"] = update_date.isoformat()
            
            # Update event
            update_event = {
                "event_id": f"evt_{random.randint(10000000, 99999999)}",
                "timestamp": update_date.isoformat(),
                "user_text": random.choice(update_messages),
                "parsed_data": {
                    "intent": "episode_update",
                    "condition": condition,
                    "fields": {"severity": new_severity},
                    "episode_link": {"link_strategy": "same_episode", "episode_id": episode_id},
                    "confidence": 0.9
                },
                "action": "update",
                "model": "gpt-4o-mini-2024-07-18",
                "episode_id": episode_id
            }
            events.append(update_event)
    
    return episodes, events

def generate_fake_observations():
    """Generate fake observations"""
    observations = {}
    
    obs_types = ["sleep", "mood", "exercise", "diet", "stress"]
    obs_messages = {
        "sleep": ["I slept 7 hours but woke up 3 times", "Poor sleep quality last night", "Slept well for 8 hours"],
        "mood": ["Feeling anxious today", "Mood is good", "Stressed about work deadline"],
        "exercise": ["Did 30 min yoga", "Went for a 20 min walk", "No exercise today"],
        "diet": ["Had spicy Indian food for lunch", "Ate cheese and wine", "Healthy meals all day"],
        "stress": ["Work was very stressful", "Relaxing day at home", "Argument with family"]
    }
    
    print("Generating observations...")
    
    base_date = datetime.now() - timedelta(days=60)
    
    for i in range(20):
        days_offset = random.randint(0, 60)
        obs_date = base_date + timedelta(days=days_offset)
        
        obs_type = random.choice(obs_types)
        obs_id = f"obs_{obs_date.strftime('%Y-%m-%d')}_{random.randint(1000, 9999)}"
        
        observation = {
            "observation_id": obs_id,
            "timestamp": obs_date.isoformat(),
            "category": obs_type,
            "notes": random.choice(obs_messages[obs_type]),
            "metadata": {"mood": random.choice(["good", "okay", "stressed", "tired"])}
        }
        
        observations[obs_id] = observation
    
    return observations

def main():
    """Generate and save fake data"""
    print("🚀 Simple Fake Health Data Generator")
    print("=" * 50)
    
    # Load existing data
    data_dir = "data"
    episodes_file = os.path.join(data_dir, "episodes.json")
    observations_file = os.path.join(data_dir, "observations.json")
    events_file = os.path.join(data_dir, "events.jsonl")
    
    # Load existing
    existing_episodes = {}
    if os.path.exists(episodes_file):
        with open(episodes_file, 'r') as f:
            existing_episodes = json.load(f)
    
    existing_observations = []
    if os.path.exists(observations_file):
        with open(observations_file, 'r') as f:
            existing_observations = json.load(f)
    
    # Generate new data
    episodes, events = generate_fake_episodes()
    observations = generate_fake_observations()
    
    # Merge with existing
    all_episodes = {**existing_episodes, **episodes}
    all_observations = existing_observations + list(observations.values())
    
    # Save episodes
    with open(episodes_file, 'w') as f:
        json.dump(all_episodes, f, indent=2)
    
    # Save observations
    with open(observations_file, 'w') as f:
        json.dump(all_observations, f, indent=2)
    
    # Append events
    with open(events_file, 'a') as f:
        for event in events:
            f.write(json.dumps(event) + '\n')
    
    print(f"✅ Generated data saved!")
    print(f"📊 Total episodes: {len(all_episodes)}")
    print(f"📋 Total observations: {len(all_observations)}")
    print(f"📝 New events: {len(events)}")
    
    print("\n🧪 Ready for testing!")
    print("Try these Recall Agent queries:")
    print("• 'Did I have any migraines last week?'")
    print("• 'Show me pain episodes from last month'")
    print("• 'Does spicy food trigger my headaches?'")

if __name__ == "__main__":
    main()