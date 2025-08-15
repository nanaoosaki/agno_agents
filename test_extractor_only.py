# test_extractor_only.py
# Test ONLY the extractor agent to isolate issues

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

print("🧪 Testing EXTRACTOR AGENT ONLY")
print("=" * 50)

# Test 1: Import and create extractor agent
print("\n1️⃣ Testing Extractor Agent Creation...")
try:
    from healthlogger.agents import create_extractor_agent
    extractor = create_extractor_agent()
    print("✅ Extractor agent created successfully")
    print(f"   Name: {extractor.name}")
    print(f"   Model: {extractor.model}")
    print(f"   Response model: {extractor.response_model}")
    print(f"   History enabled: {extractor.add_history_to_messages}")
    print(f"   History runs: {extractor.num_history_runs}")
except Exception as e:
    print(f"❌ Extractor agent creation failed: {e}")
    exit(1)

# Test 2: Test schema compatibility
print("\n2️⃣ Testing SimpleRouterOutput Schema...")
try:
    from healthlogger.schema import SimpleRouterOutput
    
    # Test schema generation (what OpenAI will see)
    schema = SimpleRouterOutput.model_json_schema()
    print("✅ Schema generation successful")
    
    # Check for the problematic patterns
    schema_str = str(schema)
    has_nested_ref = '"$ref"' in schema_str and '"description"' in schema_str
    
    print(f"   Properties count: {len(schema.get('properties', {}))}")
    print(f"   Required fields: {schema.get('required', [])}")
    print(f"   Has problematic $ref+description: {has_nested_ref}")
    
    if not has_nested_ref:
        print("✅ Schema should work with OpenAI structured output")
    else:
        print("⚠️ Schema may still have issues")
        
except Exception as e:
    print(f"❌ Schema test failed: {e}")

# Test 3: Test direct agent run (without workflow)
print("\n3️⃣ Testing Direct Agent Run...")
try:
    # Simple test message
    test_message = "I have a headache, severity 7/10"
    
    print(f"   Testing with message: '{test_message}'")
    
    # Try to run the agent directly
    response = extractor.run(test_message)
    print("✅ Agent run successful")
    print(f"   Response type: {type(response)}")
    
    # Check if we got structured output
    if hasattr(response, 'content'):
        content = response.content
        print(f"   Content type: {type(content)}")
        
        if isinstance(content, dict):
            print(f"   Keys: {list(content.keys())}")
        elif hasattr(content, 'intent'):
            print(f"   Intent: {content.intent}")
            print(f"   Condition: {content.condition}")
            print(f"   Confidence: {content.confidence}")
        else:
            print(f"   Content: {str(content)[:100]}...")
    else:
        print(f"   Response: {str(response)[:100]}...")
        
except Exception as e:
    print(f"⚠️ Agent run failed (expected without API key): {e}")
    
    # Check if it's an API key issue vs structural issue
    error_str = str(e)
    if "api" in error_str.lower() or "key" in error_str.lower():
        print("   → This is likely an API key issue, not a structural problem")
    elif "schema" in error_str.lower() or "$ref" in error_str.lower():
        print("   → This is likely our schema issue!")
    else:
        print("   → This might be a different structural issue")

print("\n" + "=" * 50)
print("🎯 EXTRACTOR AGENT ANALYSIS")
print("=" * 50)

print("""
🔍 KEY FINDINGS:
1. Focus on extractor agent only
2. Check if SimpleRouterOutput resolves OpenAI schema issues
3. Verify agent can be created and configured properly
4. Test direct agent.run() before testing in workflow

📋 NEXT STEPS:
1. Fix any schema issues found
2. Test with actual API key to verify OpenAI compatibility  
3. Only then move to workflow integration
4. Test deterministic core separately
5. Finally test full workflow

⚠️ WORKFLOW ISSUES TO ADDRESS LATER:
- StepInput.workflow_session_state attribute access
- Session state management in Agno v2 workflows
- Proper step input/output handling
""")

if __name__ == "__main__":
    print("✨ Extractor-only test completed!")