import asyncio
import logging

from config import Config
from src.models import db_setup
from src.start import start

logging.basicConfig(
    level=Config.LOG_LEVEL, format="%(name)s - %(levelname)s - %(message)s"
)


async def main() -> None:
    db_setup()
    while True:
        start(Config.RSS_URL)
        await asyncio.sleep(Config.sleep_time)


if __name__ == "__main__":
    asyncio.run(main())