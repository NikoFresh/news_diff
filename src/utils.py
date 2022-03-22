from datetime import datetime
from typing import List, Tuple

import arrow
import diff_match_patch as dmp_module
import imgkit
import requests
import telepot
from bs4 import BeautifulSoup
from config import Config
from furl import furl


def get_news_id(url: str) -> int:
    """
    Get the URL of the article and return an article id
    Currently it takes the 9-digits number at the end of the URL
    Eg: link.com/path/a_news-12a3v-45sv6-7sd89 -> return 12a3v45sv67sd89
    """
    f = furl(url)
    path: List[str] = f.path.segments
    article_id: str = "".join(path[-1].split("-")[-5:-1])
    return article_id


def convert_date(date: str) -> datetime:
    """Convert the input string to a valid Arrow object. Also convert the time to UTC"""
    date = arrow.get(date, "ddd, D MMM YYYY HH:mm:ss Z")
    return date.to("utc").naive


def scrape_article(link: str) -> Tuple[str]:
    """Get all the data about the articles"""
    r = requests.get(link).content
    soup = BeautifulSoup(r, features="html.parser")
    title: str = soup.find("h1", attrs={"class": "article-title"}).get_text(strip=True)
    summary: str = soup.find("h2", attrs={"class": "article-subtitle"}).get_text(
        strip=True
    )
    return (title, summary)


def parse(post) -> Tuple[str]:
    """Return the current data of the article"""
    link: str = post.link
    pub_date = convert_date(post.published)
    article_id: str = get_news_id(post.link)
    title, summary = scrape_article(link=link)
    return (article_id, pub_date, link, title, summary)


def check_diff(old_text: str, new_text: str) -> str:
    """Check the differences between the saved version and the current version"""
    dmp = dmp_module.diff_match_patch()
    diff = dmp.diff_main(old_text, new_text)
    dmp.diff_cleanupSemantic(diff)
    return dmp.diff_prettyHtml(diff)


def generate_img(text: str) -> None:
    """Generate an image with the changes and save in a temporary file"""
    options = {"width": 720, "minimum-font-size": 28}
    imgkit.from_string(text, "tmp.png", options=options)


def send_img(desc: str) -> None:
    """Send the image to a Telegram channel"""
    bot = telepot.Bot(Config.TELEGRAM_TOKEN)
    with open("tmp.png", "rb") as img:
        bot.sendPhoto(Config.CHAT_ID, photo=img, caption=desc, parse_mode="HTML")
