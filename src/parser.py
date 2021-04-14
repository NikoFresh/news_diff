from typing import List, Dict

import feedparser

from .utils import get_news_id, add_to_db

def parse(link: str) -> List[Dict[str, str]]:
    '''Parse the RSS data and add it to the db'''
    data = feedparser.parse(link)
    posts = data.entries
    for post in posts:
        title: str = post.title
        link: str = post.link
        author: str = post.author
        pubDate = post.published
        id: int = get_news_id(post.link)
        add_to_db(id=id, pub_date=pubDate, title=title, link=link)