import os

import requests
from fastmcp import FastMCP

token = os.getenv('TELEGRAM_BOT_TOKEN')
chat_id = os.getenv('TELEGRAM_CHAT_ID')
mcp = FastMCP("Simple Telegram Bot MCP")
url = f"https://api.telegram.org/bot{token}/sendMessage"

@mcp.tool
def send_telegram_message(text: str) -> str:
    """Send a message to a Telegram chat using the simple send_message function"""
    try:
        requests.get(url, params={'chat_id': chat_id, 'text': text})
        return 'success'
    except Exception as e:
        return f"Error sending message: {str(e)}"

if __name__ == "__main__":
    mcp.run()