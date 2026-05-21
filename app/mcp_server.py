from fastmcp import FastMCP

mcp = FastMCP("test-fastapi-complex")

@mcp.tool()
def ping(message: str) -> str:
    """Echo a message back."""
    return f"pong: {message}"

if __name__ == "__main__":
    mcp.run()
