import feedparser

from .db import add_to_db, is_already_present
from .utils import check_diff, parse


def start(link: str) -> None:
    posts = feedparser.parse(link).entries
    for post in posts:
        try:
            article_id, pub_date, article_link, title, summary, content = parse(post=post)
            already_saved = is_already_present(id=article_id)
            print(already_saved)
            if already_saved:
                # check_diff()
                pass
            else:
                add_to_db(id=article_id,
                          pub_date=pub_date,
                          link=article_link,
                          title=title,
                          summary=summary,
                          content=content)
        except:
            pass
