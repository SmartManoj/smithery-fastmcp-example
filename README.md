# FastMCP Demo 🚀

A simple demonstration of [FastMCP](https://github.com/jlowin/fastmcp), the fast, Pythonic way to build MCP servers and clients.

## What is this?

This project demonstrates how to create a basic MCP server using FastMCP. The server provides a simple tool that adds two numbers together.

## Features

- **Simple MCP Server**: Built with FastMCP framework
- **Basic Tool**: `add` function that adds two integers
- **Docker Support**: Containerized for easy deployment
- **Smithery Integration**: Configured for Smithery.ai deployment

## Quick Start

### Prerequisites

- Python 3.11+
- pip

### Local Development

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the server**:
   ```bash
   python server.py
   ```

### Using Docker

1. **Build the image**:
   ```bash
   docker build -t fastmcp-demo .
   ```

2. **Run the container**:
   ```bash
   docker run fastmcp-demo
   ```

## Project Structure

```
smithery-fastmcp-example/
├── server.py          # Main MCP server implementation
├── requirements.txt   # Python dependencies
├── smithery.yaml     # Smithery.ai configuration
├── Dockerfile        # Docker container definition
└── README.md         # This file
```

## Available Tools

### `add(a: int, b: int) -> int`

Adds two integers together.

**Parameters:**
- `a`: First integer
- `b`: Second integer

**Returns:**
- Sum of the two integers

**Example:**
```python
result = add(5, 3)  # Returns 8
```

## Configuration

The project is configured for Smithery.ai deployment with the following settings:

- **Start Command**: `python server.py`
- **Runtime**: Python 3.11
- **Protocol**: stdio

## Development

To extend this demo:

1. Add new tools using the `@mcp.tool` decorator
2. Define your function with proper type hints
3. Add a docstring for the tool description

Example:
```python
@mcp.tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b
```

## Learn More

- [FastMCP GitHub Repository](https://github.com/jlowin/fastmcp) - The official FastMCP project
- [Model Context Protocol](https://modelcontextprotocol.io/) - MCP specification and documentation
- [Smithery.ai](https://smithery.ai/) - MCP deployment platform

## License

This project is open source and available under the MIT License. 
