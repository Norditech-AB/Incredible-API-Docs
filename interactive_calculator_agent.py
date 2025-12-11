#!/usr/bin/env python3
"""
Interactive Tool-Calling Agent with Math Calculator
Uses the Incredible Python SDK Agent API for tool calling.

Install: pip install incredible-python
"""

import os
import math
from incredible_python import Incredible

# Configuration
API_KEY = os.environ.get("INCREDIBLE_API_KEY", "")

# Define the calculator tool (Agent API uses input_schema, not parameters)
CALCULATOR_TOOL = {
    "name": "calculate",
    "description": "Perform mathematical calculations. Supports: add, subtract, multiply, divide, power, sqrt, sin, cos, tan, log, abs, floor, ceil, round",
    "input_schema": {
        "type": "object",
        "properties": {
            "operation": {
                "type": "string",
                "description": "The operation to perform",
                "enum": ["add", "subtract", "multiply", "divide", "power", "sqrt", "sin", "cos", "tan", "log", "abs", "floor", "ceil", "round"]
            },
            "a": {
                "type": "number",
                "description": "First number (required for all operations)"
            },
            "b": {
                "type": "number",
                "description": "Second number (required for add, subtract, multiply, divide, power)"
            }
        },
        "required": ["operation", "a"]
    }
}


def calculate(operation: str, a: float, b: float = None) -> float | str:
    """Execute a math calculation and return the result."""
    try:
        if operation == "add":
            return a + b
        elif operation == "subtract":
            return a - b
        elif operation == "multiply":
            return a * b
        elif operation == "divide":
            if b == 0:
                return "Error: Division by zero"
            return a / b
        elif operation == "power":
            return a ** b
        elif operation == "sqrt":
            if a < 0:
                return "Error: Cannot take square root of negative number"
            return math.sqrt(a)
        elif operation == "sin":
            return math.sin(math.radians(a))
        elif operation == "cos":
            return math.cos(math.radians(a))
        elif operation == "tan":
            return math.tan(math.radians(a))
        elif operation == "log":
            if a <= 0:
                return "Error: Cannot take log of non-positive number"
            return math.log10(a)
        elif operation == "abs":
            return abs(a)
        elif operation == "floor":
            return math.floor(a)
        elif operation == "ceil":
            return math.ceil(a)
        elif operation == "round":
            return round(a)
        else:
            return f"Error: Unknown operation '{operation}'"
    except Exception as e:
        return f"Error: {str(e)}"


def execute_tool(name: str, inputs: dict) -> str:
    """Execute a tool by name with given inputs."""
    if name == "calculate":
        result = calculate(
            operation=inputs.get("operation"),
            a=inputs.get("a"),
            b=inputs.get("b")
        )
        return str(result)
    return f"Unknown tool: {name}"


def run_agent_turn(client: Incredible, messages: list) -> tuple[str, list]:
    """
    Run a single agent turn, handling tool calls if needed.
    Returns (response_text, updated_messages).
    """
    # Call the Agent API
    response = client.agent(
        messages=messages,
        tools=[CALCULATOR_TOOL],
    )
    
    # Check if there are tool calls to execute
    if response.tool_calls:
        tool_results = []
        
        for call in response.tool_calls:
            print(f"\n🔧 Calling: {call.name}({call.inputs})")
            result = execute_tool(call.name, call.inputs)
            print(f"   Result: {result}")
            tool_results.append({
                "tool_call_id": call.id,
                "result": result
            })
        
        # Add assistant's response (with tool calls) to messages
        if response.response:
            messages.append({"role": "assistant", "content": response.response})
        
        # Add tool results as user message
        result_text = "\n".join([f"Tool result: {r['result']}" for r in tool_results])
        messages.append({"role": "user", "content": result_text})
        
        # Get follow-up response with tool results
        follow_up = client.agent(
            messages=messages,
            tools=[CALCULATOR_TOOL],
        )
        
        # Handle nested tool calls recursively
        if follow_up.tool_calls:
            return run_agent_turn(client, messages)
        
        return follow_up.response, messages
    
    # No tool calls - return response directly
    return response.response, messages


def main():
    """Main interactive loop."""
    print("=" * 60)
    print("🧮 Interactive Calculator Agent (Python SDK)")
    print("=" * 60)
    print("Ask me to perform calculations! Examples:")
    print("  • What is 127 + 349?")
    print("  • Calculate 15 * 8 and then divide by 3")
    print("  • What's the square root of 144?")
    print("  • Find sin(45) + cos(45)")
    print("\nCommands: 'quit' to exit, 'clear' to reset conversation\n")
    
    if not API_KEY:
        print("⚠️  Warning: INCREDIBLE_API_KEY not set.")
        print("   Set it with: export INCREDIBLE_API_KEY='your-key'\n")
    
    # Initialize client
    client = Incredible(api_key=API_KEY)
    
    # Conversation history
    messages = []
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() in ["quit", "exit", "q"]:
                print("\nGoodbye! 👋")
                break
            
            if user_input.lower() == "clear":
                messages = []
                print("Conversation cleared.\n")
                continue
            
            # Add user message
            messages.append({"role": "user", "content": user_input})
            
            # Run agent turn
            assistant_reply, messages = run_agent_turn(client, messages)
            
            # Add assistant response to history
            messages.append({"role": "assistant", "content": assistant_reply})
            
            print(f"\nAssistant: {assistant_reply}\n")
            
        except KeyboardInterrupt:
            print("\n\nGoodbye! 👋")
            break
        except Exception as e:
            import traceback
            traceback.print_exc()
            print(f"\n❌ Error: {e}\n")


if __name__ == "__main__":
    main()
