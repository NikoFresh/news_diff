from typing import List

from .scraper import scrape_article
from .utils import convert_date, get_news_id


def parse(post) -> List[str]:
    link: str = post.link
    pub_date = convert_date(post.published)
    article_id: int = get_news_id(post.link)
    title, summary, content = scrape_article(link=link)
    return article_id, pub_date, link, title, summary, content