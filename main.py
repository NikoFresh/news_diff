import asyncio

from config import Config
from src.models import db_setup
from src.start import start


async def main() -> None:
    db_setup()
    while True:
        start(Config.RSS_URL)
        await asyncio.sleep(300)


if __name__ == "__main__":
    asyncio.run(main())