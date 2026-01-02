# Personal Assistant MCP Project

A suite of MCP (Model Context Protocol) servers designed to help you manage your time, plan your tasks, and generate high-quality visuals for a more productive and balanced life.

## Project Goals
- **Efficient Planning**: Manage your daily and weekly tasks with a persistent SQLite-backed planning server.
- **Smart Time Management**: Get accurate local time to help schedule tasks effectively.
- **Creative Visuals**: Use state-of-the-art Imagen 4.0 models via Google GenAI to generate calming or motivating visuals.

## Project Structure
- `planning_server.py`: Handles task creation, listing, and updates using SQLite.
- `time_server.py`: Provides current local time tools.
- `image_server.py`: Interfaces with Google Gemini/Imagen for AI image generation.
- `PROJECT.md`: High-level roadmap and feature tracking.
- `.gitignore`: Configured for public repository safety (hiding API keys and local databases).

## Setup Instructions

### 1. Prerequisites
- Python 3.10+
- [Conda](https://docs.conda.io/en/latest/) (Recommended) or `venv`
- A Google Gemini API Key with access to Imagen 4.0.

### 2. Environment Setup
```bash
# Create and activate environment
conda create -n mcp python=3.11
conda activate mcp

# Install dependencies
pip install fastmcp google-genai
```

### 3. API Configuration
Set your Gemini API key as an environment variable:
```bash
export GEMINI_API_KEY="your_api_key_here"
```

## Running the Servers

### Standalone Execution
You can run any server script individually for testing:
```bash
python planning_server.py
```

### MCP Client Integration
To use these with an MCP client (like Gemini Code Assist or Claude Desktop), add them to your `mcp_config.json`:

```json
{
  "mcpServers": {
    "life-ops-planning": {
      "command": "python",
      "args": ["/path/to/planning_server.py"]
    },
    "life-ops-time": {
      "command": "python",
      "args": ["/path/to/time_server.py"]
    },
    "life-ops-image": {
      "command": "python",
      "args": ["/path/to/image_server.py"],
      "env": {
        "GEMINI_API_KEY": "YOUR_KEY"
      }
    }
  }
}
```

## License
MIT
