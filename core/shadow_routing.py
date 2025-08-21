# core/shadow_routing.py
# Shadow routing system for testing and improving router accuracy

import json
import os
from datetime import datetime
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict
from pathlib import Path

@dataclass
class RoutingTestResult:
    """Results of a routing test."""
    input_text: str
    gold_intent: str
    router_intent: str
    confidence: float
    timestamp: str
    agent_used: str
    is_correct: bool
    rationale: str

class ShadowRouter:
    """Shadow routing system for collecting training data and monitoring accuracy."""
    
    def __init__(self, log_file: str = "data/shadow_routing.jsonl"):
        self.log_file = Path(log_file)
        self.log_file.parent.mkdir(exist_ok=True)
        
    def log_routing_decision(self, 
                           input_text: str, 
                           gold_intent: str, 
                           router_result: Dict[str, Any],
                           agent_used: str):
        """Log a shadow routing decision for analysis."""
        
        router_intent = router_result.get("primary", router_result.get("primary_intent", "unknown"))
        confidence = router_result.get("confidence", 0.0)
        rationale = router_result.get("rationale", "")
        
        result = RoutingTestResult(
            input_text=input_text,
            gold_intent=gold_intent,
            router_intent=router_intent,
            confidence=confidence,
            timestamp=datetime.now().isoformat(),
            agent_used=agent_used,
            is_correct=gold_intent == router_intent,
            rationale=rationale
        )
        
        # Append to JSONL log file
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(json.dumps(asdict(result)) + '\n')
    
    def run_shadow_test(self, input_text: str, agent_used: str, router_func) -> Optional[str]:
        """Run a shadow test and log the result."""
        try:
            # Infer gold intent from agent used
            gold_intent = self._infer_intent_from_agent(agent_used)
            
            if gold_intent != "unknown":
                # Run router on the input
                router_result = router_func(input_text)
                
                # Log the comparison
                self.log_routing_decision(input_text, gold_intent, router_result, agent_used)
                
                return router_result.get("primary", router_result.get("primary_intent", "unknown"))
        except Exception as e:
            print(f"Shadow routing error: {e}")
        
        return None
    
    def _infer_intent_from_agent(self, agent_name: str) -> str:
        """Infer the gold intent from the agent name used."""
        intent_mapping = {
            "Health Logger (v3.1 Multi-Modal)": "log",
            "Recall Agent (v2.1)": "recall", 
            "Coach Agent (v2.0)": "coach",
            "Profile & Onboarding (v3.3 Structured)": "profile",
            "Health Companion (Auto-Router)": "auto",  # Skip shadow testing for auto-router
        }
        
        return intent_mapping.get(agent_name, "unknown")
    
    def load_routing_history(self) -> List[RoutingTestResult]:
        """Load routing test history."""
        results = []
        
        if self.log_file.exists():
            with open(self.log_file, 'r', encoding='utf-8') as f:
                for line in f:
                    try:
                        data = json.loads(line.strip())
                        results.append(RoutingTestResult(**data))
                    except json.JSONDecodeError:
                        continue
        
        return results
    
    def generate_confusion_matrix(self) -> Dict[str, Dict[str, int]]:
        """Generate confusion matrix from routing history."""
        results = self.load_routing_history()
        
        # Get all unique intents
        all_intents = set()
        for result in results:
            all_intents.add(result.gold_intent)
            all_intents.add(result.router_intent)
        
        # Initialize confusion matrix
        matrix = {}
        for gold in all_intents:
            matrix[gold] = {}
            for router in all_intents:
                matrix[gold][router] = 0
        
        # Fill confusion matrix
        for result in results:
            matrix[result.gold_intent][result.router_intent] += 1
        
        return matrix
    
    def calculate_metrics(self) -> Dict[str, float]:
        """Calculate precision, recall, and F1 for each intent."""
        results = self.load_routing_history()
        confusion = self.generate_confusion_matrix()
        
        metrics = {}
        all_intents = set(confusion.keys())
        
        for intent in all_intents:
            if intent == "auto":  # Skip auto-router entries
                continue
                
            # True positives
            tp = confusion.get(intent, {}).get(intent, 0)
            
            # False positives (router predicted this intent incorrectly)
            fp = sum(confusion.get(other_intent, {}).get(intent, 0) 
                    for other_intent in all_intents if other_intent != intent)
            
            # False negatives (router missed this intent)
            fn = sum(confusion.get(intent, {}).get(other_intent, 0)
                    for other_intent in all_intents if other_intent != intent)
            
            # Calculate metrics
            precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
            recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
            f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0.0
            
            metrics[intent] = {
                "precision": precision,
                "recall": recall,
                "f1": f1,
                "support": tp + fn
            }
        
        # Overall accuracy
        correct = sum(1 for r in results if r.is_correct and r.agent_used != "Health Companion (Auto-Router)")
        total = sum(1 for r in results if r.agent_used != "Health Companion (Auto-Router)")
        
        metrics["overall"] = {
            "accuracy": correct / total if total > 0 else 0.0,
            "total_tests": total
        }
        
        return metrics
    
    def print_routing_report(self):
        """Print a comprehensive routing performance report."""
        metrics = self.calculate_metrics()
        confusion = self.generate_confusion_matrix()
        
        print("🔍 **Shadow Routing Performance Report**")
        print("=" * 50)
        
        # Overall metrics
        overall = metrics.get("overall", {})
        print(f"📊 **Overall Accuracy**: {overall.get('accuracy', 0.0):.3f}")
        print(f"📈 **Total Tests**: {overall.get('total_tests', 0)}")
        print()
        
        # Per-intent metrics
        print("📋 **Per-Intent Performance**:")
        for intent, scores in metrics.items():
            if intent == "overall":
                continue
            print(f"  **{intent.title()}**: P={scores['precision']:.3f}, R={scores['recall']:.3f}, F1={scores['f1']:.3f} (n={scores['support']})")
        print()
        
        # Confusion matrix
        print("🎯 **Confusion Matrix**:")
        intents = [i for i in confusion.keys() if i != "auto"]
        
        # Header
        print("Gold\\Router".ljust(12), end="")
        for intent in intents:
            print(f"{intent[:8]:>8}", end="")
        print()
        
        # Rows
        for gold in intents:
            print(f"{gold[:11]:11}", end=" ")
            for router in intents:
                count = confusion.get(gold, {}).get(router, 0)
                print(f"{count:8}", end="")
            print()
        print()
        
        # Recent errors
        results = self.load_routing_history()
        recent_errors = [r for r in results[-20:] if not r.is_correct and r.agent_used != "Health Companion (Auto-Router)"]
        
        if recent_errors:
            print("❌ **Recent Routing Errors**:")
            for error in recent_errors[-5:]:  # Show last 5 errors
                print(f"  Input: \"{error.input_text[:50]}...\"")
                print(f"  Expected: {error.gold_intent}, Got: {error.router_intent} (conf: {error.confidence:.3f})")
                print(f"  Rationale: {error.rationale}")
                print()

# Global shadow router instance
shadow_router = ShadowRouter()