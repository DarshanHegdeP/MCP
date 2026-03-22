import asyncio
from urllib import response
from dotenv import load_dotenv
from mcp_use import MCPClient,MCPAgent
from langchain_groq import ChatGroq
import os


async def run_memory_chat():
    load_dotenv()
    groq_api_key = os.getenv("GROQ_API_KEY")
    if groq_api_key:
        os.environ["GROQ_API_KEY"] = groq_api_key
    
    config_file="browser_mcp.json"
    print("Initilizing chat....")
    
    client = MCPClient.from_config_file(config_file)   
    llm = ChatGroq(model="llama-3.3-70b-versatile")
    agent = MCPAgent(
        llm=llm,
        client=client,
        max_steps=15,
        memory_enabled=True
    )
    print("Chat initialized. Starting conversation...")
    
    try:
        while True:
            user_input = input("\nYou: ")
            if user_input.lower() in ["exit", "quit"]:
                print("Exiting chat. Goodbye!")
                break
            
            if user_input.lower() == "clear":
                agent.clear_conversation_history()
                print("Conversation history cleared.")
                continue
            
            print("\n Assistant: ", end="", flush=True)

            try:
                
                response =await agent.run(user_input)
                print("\nResponse: ", response)
            except Exception as e:
                print(f"\nAn error occurred: {e}")
                
    finally:
        
        if client and client.sessions:
            await client.close_all_sessions()
            
if __name__ == "__main__":
    asyncio.run(run_memory_chat())