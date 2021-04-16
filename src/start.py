import feedparser

from .db import add_to_db, get_article_data, update_data
from .utils import check_diff, parse


def start(link: str) -> None:
    posts = feedparser.parse(link).entries
    for post in posts:
        try:
            article_id, pub_date, article_link, title, summary, content = parse(
                post=post
            )
            data = get_article_data(id=article_id)
            if data != None:
                changes: int = 0
                if data[0] != title:
                    diff = check_diff(old_text=data[0], new_text=title)
                    changes += 1
                if data[1] != summary:
                    diff = check_diff(old_text=data[1], new_text=summary)
                    changes += 1
                if data[2] != content:
                    diff = check_diff(old_text=data[2], new_text=content)
                    changes += 1
                if changes > 0:
                    update_data(
                        id=article_id, title=title, summary=summary, content=content
                    )
            else:
                add_to_db(
                    id=article_id,
                    pub_date=pub_date,
                    link=article_link,
                    title=title,
                    summary=summary,
                    content=content,
                )
        except:
            pass