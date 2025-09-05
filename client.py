import  os
SMITHERY_API_KEY = os.getenv('SMITHERY_API_KEY')
SMITHERY_PROFILE = os.getenv('SMITHERY_PROFILE')
url = f'https://server.smithery.ai/@SmartManoj/smithery-fastmcp-example/mcp?api_key={SMITHERY_API_KEY}&profile={SMITHERY_PROFILE}'

import asyncio
from fastmcp import Client

async def main():
    async with Client(url) as client:
        result = await client.list_tools()
        print(result)

if __name__ == '__main__':
    asyncio.run(main())