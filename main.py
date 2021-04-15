import asyncio

from src.start import start
from config import Config

async def main() -> None:
    while True:
        start(Config.RSS_URL)
        await asyncio.sleep(300)

if __name__ == '__main__':
    asyncio.run(main())