import os

from dotenv import load_dotenv


class Config:
    load_dotenv(".env")

    SLEEP_TIME: int = 300
    LOG_LEVEL: str = os.getenv("LOG_LEVEL")
    DB_URL: str = os.getenv("DATABASE_URL")
    TELEGRAM_TOKEN: str = os.getenv("TELEGRAM_TOKEN")
    CHAT_ID: int = os.getenv("TELEGRAM_ID")
    RSS_URL: str = "http://xml2.corriereobjects.it/rss/homepage.xml"