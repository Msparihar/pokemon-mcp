import json
import logging
from contextlib import AsyncExitStack
from typing import Any, Dict, List
import nest_asyncio
from dotenv import load_dotenv
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from mcp import ClientSession
from mcp.client.sse import sse_client
from openai import AsyncOpenAI


SYSTEM_PROMPT = """You are a Pokémon Battle Expert and Team Building Specialist. You help trainers build competitive teams and analyze battle strategies using official Pokémon data from the PokeAPI.

Your capabilities include:
1. Type Analysis: Calculate effectiveness of moves and analyze defensive/offensive type coverage
2. Team Building: Create balanced teams considering type synergies, roles, and common threats
3. Battle Analysis: Predict matchup outcomes and suggest counters
4. Pokémon Data: Access detailed information about Pokémon, their moves, and abilities

Tool Usage:
- Combine multiple tools when needed for comprehensive analysis
- For team building: Use type effectiveness + team building tools together
- For matchup analysis: Combine battle analysis with type effectiveness
- For detailed recommendations: Combine Pokémon data with team archetypes
- Always cross-reference findings between tools for accuracy

When responding:
- Always explain your reasoning for team building suggestions
- Break down type effectiveness calculations clearly
- Consider competitive viability and common strategies
- Suggest specific moves and abilities that complement team composition

Format your explanations in clear sections:
1. Analysis: Initial assessment of the request
2. Recommendations: Specific suggestions with explanations
3. Additional Considerations: Coverage, weaknesses, and alternative options"""

WELCOME_MESSAGE = """Welcome to the Pokémon Team Builder and Battle Analyst! 🎮

I can help you with:
• Building competitive teams
• Analyzing type matchups
• Checking move effectiveness
• Predicting battle outcomes
• Finding counters to specific Pokémon

Try asking me things like:
"Build a rain team around Pelipper"
"Check the effectiveness of Fire moves against Ferrothorn"
"Analyze a matchup between my team and my opponent's"
"Suggest counters to Dragapult"

What would you like help with today?"""

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

# Load environment variables
load_dotenv(override=True)

app = FastAPI()

# Global variables to store session state
session = None
exit_stack = AsyncExitStack()
openai_client = AsyncOpenAI()
model = "gpt-4o"


async def connect_to_server(server_script_path: str = "server.py"):
    """Connect to an MCP server.

    Args:
        server_script_path: Path to the server script.
    """
    global session, exit_stack

    logging.info(f"Configuring server with script: {server_script_path}")

    try:
        # Connect to the server
        logging.info("Establishing SSE connection to server")
        stdio_transport = await exit_stack.enter_async_context(sse_client("http://localhost:8050/sse"))
        stdio, write = stdio_transport

        logging.info("Creating client session")
        session = await exit_stack.enter_async_context(ClientSession(stdio, write))

        # Initialize the connection
        logging.info("Initializing session")
        await session.initialize()

        # List available tools
        logging.info("Retrieving available tools")
        tools_result = await session.list_tools()
        logging.info("Available tools:")
        for tool in tools_result.tools:
            logging.info(f"  - {tool.name}: {tool.description}")

        return True
    except Exception as e:
        logging.error(f"Failed to connect to server: {str(e)}", exc_info=True)
        raise


async def get_mcp_tools() -> List[Dict[str, Any]]:
    """Get available tools from the MCP server in OpenAI format.

    Returns:
        A list of tools in OpenAI format.
    """
    global session

    tools_result = await session.list_tools()
    return [
        {
            "type": "function",
            "function": {
                "name": tool.name,
                "description": tool.description,
                "parameters": tool.inputSchema,
            },
        }
        for tool in tools_result.tools
    ]


async def process_query(query: str) -> str:
    """Process a query using OpenAI and available MCP tools.

    Args:
        query: The user query.

    Returns:
        The response from OpenAI.
    """
    global session, openai_client, model

    logging.info("Fetching available MCP tools")
    tools = await get_mcp_tools()
    logging.info(f"Found {len(tools)} available tools")

    # Initial OpenAI API call
    logging.info(f"Sending initial request to OpenAI (model: {model})")
    response = await openai_client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": query}],
        tools=tools,
        tool_choice="auto",
    )

    # Get assistant's response
    assistant_message = response.choices[0].message
    logging.info("Received initial response from OpenAI")

    # Initialize conversation with system prompt, user query and assistant response
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": query},
        assistant_message,
    ]

    # Handle tool calls if present
    if assistant_message.tool_calls:
        logging.info(f"OpenAI requested {len(assistant_message.tool_calls)} tool call(s)")

        # Process each tool call
        for tool_call in assistant_message.tool_calls:
            tool_name = tool_call.function.name
            tool_args = json.loads(tool_call.function.arguments)
            logging.info(f"Executing tool: {tool_name} with arguments: {tool_args}")

            try:
                # Execute tool call
                result = await session.call_tool(tool_name, tool_args)
                logging.info(f"Tool {tool_name} executed successfully")

                # Add tool response to conversation
                messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": result.content[0].text,
                    }
                )
                logging.info("Tool response added to conversation")
            except Exception as e:
                logging.error(f"Error executing tool {tool_name}: {str(e)}", exc_info=True)
                raise

        # Get final response from OpenAI with tool results
        logging.info("Sending final request to OpenAI with tool results")
        final_response = await openai_client.chat.completions.create(
            model=model,
            messages=messages,
            tools=tools,
            tool_choice="none",  # Don't allow more tool calls
        )
        logging.info("Received final response from OpenAI")

        return final_response.choices[0].message.content

    # No tool calls, just return the direct response
    logging.info("No tool calls required, returning direct response")
    return assistant_message.content


async def cleanup():
    """Clean up resources."""
    global exit_stack
    await exit_stack.aclose()


# Root endpoint that serves the chat interface
@app.get("/")
async def get():
    return HTMLResponse("""
    <!DOCTYPE html>
    <html>
        <head>
            <title>OpenAI Chat</title>
            <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                    background-color: #f5f5f5;
                }
                #chat-container {
                    background-color: white;
                    border-radius: 8px;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                    padding: 20px;
                    margin-bottom: 20px;
                }
                #messages {
                    height: 400px;
                    overflow-y: auto;
                    margin-bottom: 20px;
                    padding: 16px;
                    border: 1px solid #ddd;
                    border-radius: 4px;
                    line-height: 1.5;
                }
                .message {
                    margin-bottom: 16px;
                    padding: 12px;
                    border-radius: 4px;
                    overflow-wrap: break-word;
                }
                /* Code blocks */
                .message pre {
                    background: #f6f8fa;
                    padding: 12px;
                    border-radius: 4px;
                    overflow-x: auto;
                }
                .message code {
                    font-family: 'Consolas', monospace;
                    font-size: 0.9em;
                }
                /* Lists */
                .message ul, .message ol {
                    padding-left: 20px;
                    margin: 8px 0;
                }
                /* Tables */
                .message table {
                    border-collapse: collapse;
                    width: 100%;
                    margin: 12px 0;
                }
                .message th, .message td {
                    border: 1px solid #ddd;
                    padding: 8px;
                    text-align: left;
                }
                /* Headings */
                .message h1, .message h2, .message h3 {
                    margin: 16px 0 8px 0;
                }
                /* Blockquotes */
                .message blockquote {
                    border-left: 4px solid #ddd;
                    margin: 8px 0;
                    padding-left: 12px;
                    color: #666;
                }
                .user-message {
                    background-color: #e3f2fd;
                    margin-left: 20%;
                }
                .bot-message {
                    background-color: #f5f5f5;
                    margin-right: 20%;
                }
                #input-container {
                    display: flex;
                    gap: 10px;
                }
                #messageInput {
                    flex-grow: 1;
                    padding: 8px;
                    border: 1px solid #ddd;
                    border-radius: 4px;
                }
                button {
                    padding: 8px 16px;
                    background-color: #2196f3;
                    color: white;
                    border: none;
                    border-radius: 4px;
                    cursor: pointer;
                }
                button:hover {
                    background-color: #1976d2;
                }
            </style>
        </head>
        <body>
            <div id="chat-container">
                <h1>OpenAI Chat</h1>
                <div id="messages"></div>
                <div id="input-container">
                    <input type="text" id="messageInput" placeholder="Type your message...">
                    <button onclick="sendMessage()">Send</button>
                </div>
            </div>

            <script>
                const messagesDiv = document.getElementById('messages');
                const messageInput = document.getElementById('messageInput');
                let ws = new WebSocket(`ws://${window.location.host}/ws`);

                ws.onmessage = function(event) {
                    addMessage('bot', event.data);
                };

                ws.onclose = function() {
                    addMessage('bot', 'Connection closed. Please refresh the page to reconnect.');
                };

                // Configure marked options
                marked.setOptions({
                    sanitize: true,
                    sanitizer: function(html) {
                        return html;
                    }
                });

                function addMessage(sender, content) {
                    const messageDiv = document.createElement('div');
                    messageDiv.className = `message ${sender}-message`;
                    messageDiv.innerHTML = marked.parse(content); // Parse markdown
                    messagesDiv.appendChild(messageDiv);
                    messagesDiv.scrollTop = messagesDiv.scrollHeight;
                }

                function sendMessage() {
                    const message = messageInput.value.trim();
                    if (message) {
                        ws.send(message);
                        addMessage('user', message);
                        messageInput.value = '';
                    }
                }

                messageInput.addEventListener('keypress', function(e) {
                    if (e.key === 'Enter') {
                        sendMessage();
                    }
                });
            </script>
        </body>
    </html>
    """)


# WebSocket endpoint
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    client_id = id(websocket)  # Unique identifier for each connection
    logging.info(f"New WebSocket connection [ID: {client_id}]")

    await websocket.accept()
    logging.info(f"WebSocket connection accepted [ID: {client_id}]")

    try:
        # Initialize server connection
        logging.info(f"Initializing server connection [ID: {client_id}]")
        await connect_to_server("server.py")
        logging.info(f"Server connection established [ID: {client_id}]")

        # Send welcome message
        await websocket.send_text(WELCOME_MESSAGE)
        logging.info(f"Welcome message sent [ID: {client_id}]")

        while True:
            # Receive message from client
            query = await websocket.receive_text()
            logging.info(f"Received query: '{query}' [ID: {client_id}]")

            if query.lower() in ["quit", "exit"]:
                logging.info(f"Exit command received [ID: {client_id}]")
                break

            try:
                # Process the query and get response
                logging.info(f"Processing query with OpenAI [ID: {client_id}]")
                response = await process_query(query)
                logging.info(f"OpenAI response received [ID: {client_id}]")

                await websocket.send_text(response)
                logging.info(f"Response sent to client [ID: {client_id}]")

            except Exception as e:
                error_message = f"Error processing query: {str(e)}"
                logging.error(f"{error_message} [ID: {client_id}]", exc_info=True)
                await websocket.send_text(error_message)

    except Exception as e:
        logging.error(f"WebSocket error: {str(e)} [ID: {client_id}]", exc_info=True)
    finally:
        logging.info(f"Cleaning up resources [ID: {client_id}]")
        await cleanup()
        logging.info(f"WebSocket connection closed [ID: {client_id}]")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
