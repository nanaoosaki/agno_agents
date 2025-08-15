#!/usr/bin/env python3
"""
Simple test script to verify the agents work correctly.
Run this before starting the full Gradio interface.
"""

import os
import sys

# Add current directory to path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from agents import call_agent, AGENTS, get_agent_info

def test_echo_agent():
    """Test the EchoAgent (should always work)"""
    print("🧪 Testing EchoAgent...")
    result = call_agent("EchoAgent", "Hello, this is a test message!")
    print(f"✅ Response: {result.text}")
    return True

def test_agent_with_files():
    """Test agent with file attachments (simulated)"""
    print("\n🧪 Testing agent with files...")
    test_files = ["test1.txt", "test2.pdf"]
    result = call_agent("EchoAgent", "Process these files", test_files)
    print(f"✅ Response: {result.text}")
    return True

def test_research_agent():
    """Test ResearchAgent (requires API keys)"""
    print("\n🧪 Testing ResearchAgent...")
    result = call_agent("ResearchAgent", "What is the weather like today?")
    
    if "not available" in result.text or "Error" in result.text:
        print(f"⚠️  ResearchAgent not fully functional: {result.text}")
        return False
    else:
        print(f"✅ Response: {result.text[:100]}...")
        return True

def test_general_agent():
    """Test GeneralAgent (requires API keys)"""
    print("\n🧪 Testing GeneralAgent...")
    result = call_agent("GeneralAgent", "Explain what 2+2 equals")
    
    if "not available" in result.text or "Error" in result.text:
        print(f"⚠️  GeneralAgent not fully functional: {result.text}")
        return False
    else:
        print(f"✅ Response: {result.text[:100]}...")
        return True

def main():
    """Run all tests"""
    print("🚀 Testing Agno Chat Interface Components\n")
    
    # Show available agents
    print("📋 Available agents:")
    agent_info = get_agent_info()
    for name, description in agent_info.items():
        print(f"  • {name}: {description}")
    
    print("\n" + "="*50)
    
    # Run tests
    tests = [
        ("EchoAgent", test_echo_agent),
        ("Files", test_agent_with_files),
        ("ResearchAgent", test_research_agent),
        ("GeneralAgent", test_general_agent),
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            success = test_func()
            results.append((test_name, success))
        except Exception as e:
            print(f"❌ {test_name} failed with error: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "="*50)
    print("📊 Test Results:")
    
    passed = 0
    for test_name, success in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"  {test_name}: {status}")
        if success:
            passed += 1
    
    print(f"\n🎯 {passed}/{len(results)} tests passed")
    
    if passed == len(results):
        print("\n🎉 All tests passed! The chat interface should work correctly.")
        print("💡 Run 'python app.py' to start the Gradio interface.")
    else:
        print("\n⚠️  Some tests failed. Check your .env file and API keys.")
        print("💡 The EchoAgent should always work for basic testing.")
    
    return passed == len(results)

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)