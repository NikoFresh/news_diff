from typing import Dict, List

import feedparser

from .scraper import scrape_article
from .utils import add_to_db, get_news_id


def parse(link: str) -> List[Dict[str, str]]:
    '''Parse the RSS data and add it to the db'''
    data = feedparser.parse(link)
    posts = data.entries
    for post in posts:
        link: str = post.link
        pubDate = post.published
        id: int = get_news_id(post.link)
        title, summary, content = scrape_article(link=link)
        add_to_db(id=id, pub_date=pubDate, link=link, title=title, summary=summary, content=content)
