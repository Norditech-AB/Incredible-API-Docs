#!/usr/bin/env python3
"""
File Upload Agent Example
Demonstrates uploading a file and using it with the Incredible Agent API.

Install: pip install incredible-python
"""

import os
import sys
from incredible_python import Incredible

# Configuration
API_KEY = os.environ.get("INCREDIBLE_API_KEY", "")


def upload_file(client: Incredible, file_path: str) -> str:
    """
    Upload a file using the Incredible Python SDK.
    Returns the file_id for use in agent requests.
    """
    filename = os.path.basename(file_path)
    print(f"📄 Uploading: {filename}")
    
    # Upload using the SDK - handles all 3 steps automatically
    with open(file_path, "rb") as f:
        file = client.files.upload(file=f)
    
    print(f"✅ File uploaded successfully! file_id: {file.file_id}")
    return file.file_id


# Define tools for file analysis
ANALYZE_TOOL = {
    "name": "analyze_file",
    "description": "Analyze data from the uploaded file. Use this to extract insights, summarize content, or perform calculations on the file data.",
    "input_schema": {
        "type": "object",
        "properties": {
            "analysis_type": {
                "type": "string",
                "description": "Type of analysis to perform",
                "enum": ["summary", "statistics", "key_points", "custom"]
            },
            "focus_area": {
                "type": "string",
                "description": "Specific aspect to focus on (e.g., 'sales', 'trends', 'revenue')"
            }
        },
        "required": ["analysis_type"]
    }
}

SEARCH_TOOL = {
    "name": "search_file",
    "description": "Search for specific information within the uploaded file.",
    "input_schema": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "What to search for in the file"
            }
        },
        "required": ["query"]
    }
}


def execute_tool(name: str, inputs: dict) -> str:
    """Execute a tool by name with given inputs."""
    if name == "analyze_file":
        analysis_type = inputs.get("analysis_type", "summary")
        focus_area = inputs.get("focus_area", "general")
        return f"Analysis performed: {analysis_type} on {focus_area}. The file has been analyzed and insights extracted."
    
    if name == "search_file":
        query = inputs.get("query", "")
        return f"Searched for '{query}' in the file. Results found based on file content."
    
    return f"Unknown tool: {name}"


def run_file_agent(client: Incredible, file_id: str, user_query: str, messages: list) -> tuple[str, list]:
    """
    Run the agent with file context and handle tool calls.
    Returns (response_text, updated_messages).
    """
    # Add user message with file_id
    messages.append({
        "role": "user",
        "content": user_query,
        "file_ids": [file_id]
    })
    
    # Call the Agent API
    response = client.agent(
        system_prompt="You are a helpful file analysis assistant. You can analyze uploaded files, extract insights, and answer questions about their content. Use the available tools when needed to provide detailed analysis.",
        messages=messages,
        tools=[ANALYZE_TOOL, SEARCH_TOOL],
    )
    
    # Check if there are tool calls to execute
    if response.tool_calls:
        tool_results = []
        
        for call in response.tool_calls:
            print(f"\n🔧 Tool Call: {call.name}")
            print(f"   Inputs: {call.inputs}")
            result = execute_tool(call.name, call.inputs)
            print(f"   Result: {result}")
            tool_results.append({
                "tool_call_id": call.id,
                "result": result
            })
        
        # Add assistant's response to messages
        if response.response:
            messages.append({"role": "assistant", "content": response.response})
        
        # Add tool results as user message
        result_text = "\n".join([f"Tool result: {r['result']}" for r in tool_results])
        messages.append({"role": "user", "content": result_text})
        
        # Get follow-up response with tool results
        follow_up = client.agent(
            system_prompt="You are a helpful file analysis assistant. Analyze files and provide insights.",
            messages=messages,
            tools=[ANALYZE_TOOL, SEARCH_TOOL],
        )
        
        # Handle nested tool calls recursively
        if follow_up.tool_calls:
            return run_file_agent(client, file_id, "", messages)
        
        return follow_up.response, messages
    
    # No tool calls - return response directly
    return response.response, messages


def main():
    """Main interactive loop."""
    print("=" * 60)
    print("📁 File Upload Agent Example")
    print("=" * 60)
    
    if not API_KEY:
        print("\n⚠️  Error: INCREDIBLE_API_KEY not set.")
        print("   Set it with: export INCREDIBLE_API_KEY='your-key'")
        sys.exit(1)
    
    # Get file path from command line or prompt
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        print("\nUsage: python file_upload_agent.py <file_path>")
        print("\nSupported file types: PDF, CSV, Excel, JSON, TXT, images")
        print("\nExample:")
        print("  python file_upload_agent.py report.pdf")
        print("  python file_upload_agent.py data.csv")
        file_path = input("\nEnter file path (or 'quit' to exit): ").strip()
        if file_path.lower() in ["quit", "exit", "q"]:
            print("Goodbye! 👋")
            sys.exit(0)
    
    # Check if file exists
    if not os.path.exists(file_path):
        print(f"\n❌ Error: File not found: {file_path}")
        sys.exit(1)
    
    # Initialize client
    client = Incredible(api_key=API_KEY)
    
    try:
        # Upload the file
        print("\n" + "-" * 40)
        file_id = upload_file(client, file_path)
        print("-" * 40 + "\n")
        
        print("File is ready! You can now ask questions about it.")
        print("Commands: 'quit' to exit\n")
        
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
                
                # Run agent with file context
                assistant_reply, messages = run_file_agent(client, file_id, user_input, messages)
                
                # Add assistant response to history
                messages.append({"role": "assistant", "content": assistant_reply})
                
                print(f"\nAssistant: {assistant_reply}\n")
                
            except KeyboardInterrupt:
                print("\n\nGoodbye! 👋")
                break
                
    except Exception as e:
        import traceback
        traceback.print_exc()
        print(f"\n❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
