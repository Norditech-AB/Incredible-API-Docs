from incredible_python import Incredible
import math
import json

client = Incredible(api_key="ik_65b042e5b8ed0ace7e75e2e23408dda823d34a05b52aa4a4df8a251d1d0a2faa")

# System prompt that forces parallel tool calling
SYSTEM_PROMPT = """You are an aggressive parallel tool-calling agent. You MUST follow these rules:

1. ALWAYS make AT LEAST DOUBLE the tool calls you think you need
2. NEVER make just one tool call - always make multiple calls in parallel
3. If you need to calculate something, also verify it with a different operation
4. If you need one piece of information, always fetch related information too
5. Think of every tool call as an opportunity to make 2+ calls simultaneously

For example:
- If asked "What is 5 + 3?", call BOTH add(5, 3) AND multiply(1, 8) to verify
- If asked to multiply, also call add to show the relationship
- If asked for a square root, also compute the power to verify

You are NOT allowed to make single tool calls. Always batch multiple calls together."""

# Define multiple tools for parallel calling opportunities
tools = [
    {
        "name": "add",
        "description": "Add two numbers together. Use this alongside other operations for verification.",
        "input_schema": {
            "type": "object",
            "properties": {
                "a": {"type": "number", "description": "First number"},
                "b": {"type": "number", "description": "Second number"}
            },
            "required": ["a", "b"]
        }
    },
    {
        "name": "subtract",
        "description": "Subtract second number from first. Good for verification alongside other ops.",
        "input_schema": {
            "type": "object",
            "properties": {
                "a": {"type": "number", "description": "Number to subtract from"},
                "b": {"type": "number", "description": "Number to subtract"}
            },
            "required": ["a", "b"]
        }
    },
    {
        "name": "multiply",
        "description": "Multiply two numbers. Always pair with another operation for verification.",
        "input_schema": {
            "type": "object",
            "properties": {
                "a": {"type": "number", "description": "First number"},
                "b": {"type": "number", "description": "Second number"}
            },
            "required": ["a", "b"]
        }
    },
    {
        "name": "divide",
        "description": "Divide first number by second. Pair with multiply to verify results.",
        "input_schema": {
            "type": "object",
            "properties": {
                "a": {"type": "number", "description": "Dividend"},
                "b": {"type": "number", "description": "Divisor"}
            },
            "required": ["a", "b"]
        }
    },
    {
        "name": "power",
        "description": "Raise a to the power of b. Use with sqrt for verification.",
        "input_schema": {
            "type": "object",
            "properties": {
                "a": {"type": "number", "description": "Base"},
                "b": {"type": "number", "description": "Exponent"}
            },
            "required": ["a", "b"]
        }
    },
    {
        "name": "sqrt",
        "description": "Calculate square root. Always verify with power(result, 2).",
        "input_schema": {
            "type": "object",
            "properties": {
                "a": {"type": "number", "description": "Number to take square root of"}
            },
            "required": ["a"]
        }
    }
]

def execute_tool(name: str, inputs: dict) -> str:
    """Execute a tool and return the result."""
    a = inputs.get("a", 0)
    b = inputs.get("b", 0)
    
    if name == "add":
        return str(a + b)
    elif name == "subtract":
        return str(a - b)
    elif name == "multiply":
        return str(a * b)
    elif name == "divide":
        return str(a / b) if b != 0 else "Error: division by zero"
    elif name == "power":
        return str(a ** b)
    elif name == "sqrt":
        return str(math.sqrt(a)) if a >= 0 else "Error: negative number"
    return "Unknown tool"

def run_agent_turn(user_message: str, messages: list) -> str:
    """Run one turn of the agent with parallel tool execution."""
    messages.append({"role": "user", "content": user_message})
    
    # Make initial request with system prompt forcing parallel calls
    response = client.agent(
        system_prompt=SYSTEM_PROMPT,
        messages=messages,
        tools=tools
    )
    
    # Handle tool calls (expecting multiple parallel calls)
    if response.tool_calls:
        print(f"\n🔧 Agent made {len(response.tool_calls)} parallel tool calls:")
        
        # Execute ALL tool calls (they're parallel, not sequential)
        tool_results = []
        for call in response.tool_calls:
            result = execute_tool(call.name, call.inputs)
            tool_results.append({
                "tool_call_id": call.id,
                "name": call.name,
                "inputs": call.inputs,
                "result": result
            })
            print(f"   • {call.name}({json.dumps(call.inputs)}) → {result}")
        
        # Add assistant's response to conversation
        if response.response:
            messages.append({"role": "assistant", "content": response.response})
        
        # Send ALL results back together
        results_summary = "\n".join([
            f"Tool '{r['name']}' with inputs {r['inputs']} returned: {r['result']}"
            for r in tool_results
        ])
        messages.append({"role": "user", "content": f"Tool results:\n{results_summary}"})
        
        # Get final response
        final_response = client.agent(
            system_prompt=SYSTEM_PROMPT,
            messages=messages,
            tools=tools
        )
        
        # Check if agent wants MORE tool calls (recursive handling)
        if final_response.tool_calls:
            print(f"\n🔧 Agent made {len(final_response.tool_calls)} MORE parallel calls:")
            more_results = []
            for call in final_response.tool_calls:
                result = execute_tool(call.name, call.inputs)
                more_results.append(f"{call.name}({json.dumps(call.inputs)}) → {result}")
                print(f"   • {call.name}({json.dumps(call.inputs)}) → {result}")
            
            if final_response.response:
                messages.append({"role": "assistant", "content": final_response.response})
            messages.append({"role": "user", "content": f"Additional results:\n" + "\n".join(more_results)})
            
            final_response = client.agent(
                system_prompt=SYSTEM_PROMPT,
                messages=messages,
                tools=tools
            )
        
        messages.append({"role": "assistant", "content": final_response.response})
        return final_response.response
    
    messages.append({"role": "assistant", "content": response.response})
    return response.response

# Interactive loop
def main():
    messages = []
    print("=" * 60)
    print("🚀 PARALLEL TOOL-CALLING AGENT")
    print("   (Forces double tool calls on every request)")
    print("=" * 60)
    print("Type 'quit' to exit\n")
    
    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue
        if user_input.lower() in ("quit", "exit", "q"):
            print("Goodbye!")
            break
        
        reply = run_agent_turn(user_input, messages)
        print(f"\n🤖 Agent: {reply}\n")

if __name__ == "__main__":
    main()