import asyncio
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
from mcp_use import MCPClient, MCPAgent
from langchain_groq import ChatGroq
import os

load_dotenv()

mcp = FastMCP("groq-agent")

@mcp.tool()
async def run_task(query: str) -> str:
    """Execute tasks like browser automation using MCP"""

    config_file = "browser_mcp.json"

    client = MCPClient.from_config_file(config_file)

    llm = ChatGroq(model="llama-3.3-70b-versatile")

    agent = MCPAgent(
        llm=llm,
        client=client,
        max_steps=10
    )

    try:
        result = await agent.run(query)
    except Exception as e:
        result = str(e)

    await client.close_all_sessions()

    return str(result)


if __name__ == "__main__":
    asyncio.run(mcp.run())