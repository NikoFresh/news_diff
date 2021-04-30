import os

from dotenv import load_dotenv


class Config:
    load_dotenv(".env")

    sleep_time: int = 300
    LOG_LEVEL: str = os.getenv("LOG_LEVEL")
    DB_URL: str = os.getenv("DATABASE_URL")
    TELEGRAM_TOKEN: str = os.getenv("TELEGRAM_TOKEN")
    CHAT_ID: int = os.getenv("TELEGRAM_ID")
    RSS_URL: str = "http://xml2.corriereobjects.it/rss/homepage.xml"
    DB_HOST: str = os.getenv('DB_HOST')
    DB_USER: str = os.getenv('DB_USER')
    DB_PWD: str = os.getenv('DB_PWD')
    DB: str = os.getenv('DB')