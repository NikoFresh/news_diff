import asyncio

from src.parser import parse
from config import Config

async def main() -> None:
    while True:
        parse(Config.RSS_URL)
        await asyncio.sleep(5)

if __name__ == '__main__':
    asyncio.run(main())