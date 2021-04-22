from dotenv import load_dotenv
import os


class Config:
    load_dotenv(".env")

    TELEGRAM_TOKEN: str = os.getenv("TELEGRAM_TOKEN")
    CHAT_ID: int = os.getenv("TELEGRAM_ID")
    RSS_URL: str = "http://xml2.corriereobjects.it/rss/homepage.xml"
    HTML_TEMPLATE: str = """
        <html>
          <head>
           
          </head>
          <body>
            <p>
                {}
            </p>
          </body>
        </html>
    """
