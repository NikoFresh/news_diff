import difflib
import asyncio

from src.parser import parse

RSS_URL: str = 'https://www.repubblica.it/rss/cronaca/rss2.0.xml'



async def main() -> None:
    while True:
        parse(RSS_URL)
        await asyncio.sleep(5)
    

if __name__ == '__main__':
    asyncio.run(main())