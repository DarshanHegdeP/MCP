# 🚀 MCP Agent & Server Ecosystem

A state-of-the-art demonstration of the **Model Context Protocol (MCP)**, featuring autonomous agents, browser automation, and multi-server orchestration. This ecosystem leverage's Groq's high-performance inference to provide a seamless agentic experience.

---

## 🏗️ Architecture Overview

The system operates in two modes: an interactive **CLI Agent** and a standalone **MCP Server**. Both modes utilize the same core logic but differ in their entry points and orchestration.

### 1. CLI Agent Flow (`app.py`)

In this mode, the user interacts directly with a terminal-based agent.

```mermaid
graph TD
    subgraph "MCP Host Region (Application Space)"
        User["👤 User"] -->|Inputs| App["🖥️ app.py / CLI"]
        App -->|Initializes| Agent["🤖 MCPAgent"]
        Agent -->|Reasons with| LLM["🧠 Groq LLM"]
        Agent -->|Instantiates| Client["🔌 MCP Client"]
    end

    subgraph "Registry Region"
        Client -.->|Reads Registry Config| Config["📄 browser_mcp.json"]
    end

    subgraph "MCP Server Region (Child Processes)"
        Client -->|Connects To| PW["🌐 Playwright"]
        Client -->|Connects To| AB["🏠 Airbnb"]
        Client -->|Connects To| GA["⚙️ server.py (FastMCP)"]
    end
```

### 2. Prompting/Server Flow (`server.py`)

In this mode, the project acts as an MCP server itself, exposing a `run_task` tool to external clients.

```mermaid
graph TD
    subgraph "External Region"
        Ext["🌐 External MCP Client"] -->|Calls 'run_task'| GA["⚙️ server.py (FastMCP)"]
    end

    subgraph "MCP Host Region"
        GA -->|Initializes| Agent["🤖 MCPAgent"]
        Agent -->|Instantiates| Client["🔌 MCP Client"]
    end

    subgraph "Registry Region"
        Client -.->|Reads Config| Config["📄 browser_mcp.json"]
    end

    subgraph "Secondary MCP Server Region"
        Client -->|Delegates To| PW["🌐 Playwright"]
        Client -->|Delegates To| AB["🏠 Airbnb"]
    end
```

---

## ✨ Key Features

- **⚡ High-Performance Inference**: Powered by Groq's `llama-3.3-70b-versatile` for near-instantaneous reasoning.
- **🌐 Autonomous Browser Control**: Deep integration with Playwright for navigating and interacting with the web.
- **🔌 Flexible Server Protocol**: Connects to any standard MCP server for extensible tool capabilities.
- **📂 State-Aware Memory**: (In `app.py`) Maintains conversation state to handle complex, iterative requests.
- **🛠️ Custom Server Extension**: Includes its own `FastMCP` server for wrapping agentic workflows as reusable tools.

---

## 📂 Project Structure

| Component | Responsibility |
| :--- | :--- |
| `app.py` | The flagship CLI chat interface and agent controller. |
| `server.py` | A `FastMCP` server implementation providing the `run_task` tool. |
| `browser_mcp.json` | The core registry for all connected MCP services. |
| `pyproject.toml` | Project dependencies managed via Python's `uv` tool. |
| `.env` | Secure storage for sensitive API keys. |

---

## 🛠️ Getting Started

### 1. Environment Setup
Ensure you have [uv](https://github.com/astral-sh/uv) installed and a valid Groq API key.

```bash
# Clone the environment variables
echo "GROQ_API_KEY=your_key_here" > .env
```

### 2. Launch the Ecosystem
You can interact with the agent directly or run the custom server.

**Start the Interactive Agent:**
```bash
python app.py
```

**Expose the Custom MCP Server:**
```bash
python server.py
```

---

## 📖 Implementation Notes
The ecosystem is built on the `mcp_use` library, bridging LangChain components with the Model Context Protocol. The `MCPAgent` is configured with safety rails like `max_steps` to prevent infinite loops during autonomous execution.


---

*Note: The previous `mcp.json` was detected as missing or redundant; all core configuration is now consolidated in `browser_mcp.json`.*

---

Made with ❤️ for the MCP Community
