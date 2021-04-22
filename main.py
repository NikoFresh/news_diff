import asyncio

from src.start import start
from src.models import db_setup
from config import Config


async def main() -> None:
    db_setup()
    while True:
        start(Config.RSS_URL)
        await asyncio.sleep(300)


if __name__ == "__main__":
    asyncio.run(main())