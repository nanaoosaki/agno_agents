#!/usr/bin/env python3
# scripts/routecheck.py
# Route checking script for testing router accuracy against labeled examples

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.agent_manifests import get_routing_examples_for_testing
from core.shadow_routing import ShadowRouter
from health_advisor.router.agent import MasterAgent

def test_router_accuracy():
    """Test router accuracy against labeled examples."""
    
    # Get test examples
    examples = get_routing_examples_for_testing()
    
    # Initialize router and shadow system
    try:
        master_agent = MasterAgent()
        router_agent = master_agent.router_agent
    except Exception as e:
        print(f"❌ Failed to initialize router: {e}")
        return
    
    shadow_router = ShadowRouter("data/routecheck_results.jsonl")
    
    print("🧪 **Router Accuracy Test**")
    print("=" * 40)
    print(f"📋 Testing {len(examples)} labeled examples...")
    print()
    
    correct = 0
    total = 0
    results = []
    
    for example in examples:
        input_text = example["input"]
        expected_intent = example["expected_intent"]
        
        try:
            # Test the router
            router_result = router_agent.run(input_text)
            router_intent = getattr(router_result, 'primary', getattr(router_result, 'primary_intent', 'unknown'))
            confidence = getattr(router_result, 'confidence', 0.0)
            rationale = getattr(router_result, 'rationale', '')
            
            # Check if correct
            is_correct = expected_intent == router_intent
            if is_correct:
                correct += 1
            
            total += 1
            
            # Log result
            shadow_router.log_routing_decision(
                input_text=input_text,
                gold_intent=expected_intent,
                router_result={
                    "primary": router_intent,
                    "confidence": confidence,
                    "rationale": rationale
                },
                agent_used="routecheck"
            )
            
            # Store for detailed output
            results.append({
                "input": input_text,
                "expected": expected_intent,
                "predicted": router_intent,
                "confidence": confidence,
                "correct": is_correct,
                "rationale": rationale
            })
            
            # Print result
            status = "✅" if is_correct else "❌"
            print(f"{status} {input_text[:40]:40} | Expected: {expected_intent:8} | Got: {router_intent:8} | Conf: {confidence:.3f}")
            
        except Exception as e:
            print(f"❌ Error testing '{input_text}': {e}")
            total += 1
    
    print()
    print("📊 **Results Summary**")
    print("=" * 40)
    print(f"🎯 **Accuracy**: {correct}/{total} = {correct/total:.3f}")
    print()
    
    # Show errors in detail
    errors = [r for r in results if not r["correct"]]
    if errors:
        print("❌ **Routing Errors**:")
        for error in errors:
            print(f"  Input: \"{error['input']}\"")
            print(f"  Expected: {error['expected']}, Got: {error['predicted']} (conf: {error['confidence']:.3f})")
            print(f"  Rationale: {error['rationale']}")
            print()
    
    # Generate confusion matrix if we have enough data
    if total > 5:
        print("🎯 **Performance by Intent**:")
        from collections import defaultdict
        
        by_intent = defaultdict(lambda: {"correct": 0, "total": 0})
        for result in results:
            intent = result["expected"]
            by_intent[intent]["total"] += 1
            if result["correct"]:
                by_intent[intent]["correct"] += 1
        
        for intent, stats in by_intent.items():
            if intent != "control":  # Skip control examples
                accuracy = stats["correct"] / stats["total"]
                print(f"  {intent:10}: {stats['correct']:2}/{stats['total']:2} = {accuracy:.3f}")
    
    print()
    
    # Threshold check
    threshold = 0.8
    if correct / total >= threshold:
        print(f"🎉 **PASS**: Router accuracy {correct/total:.3f} meets threshold {threshold}")
        return True
    else:
        print(f"⚠️ **FAIL**: Router accuracy {correct/total:.3f} below threshold {threshold}")
        return False

if __name__ == "__main__":
    success = test_router_accuracy()
    sys.exit(0 if success else 1)