import feedparser
from sqlalchemy.sql.expression import except_

from .db import add_to_db, get_article_data
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
                if data[0] != title:
                    diff = check_diff(old_text=data[0], new_text=title)
                    print(diff)
                if data[1] != summary:
                    diff = check_diff(old_text=data[1], new_text=summary)
                    print(diff)
                if data[2] != content:
                    diff = check_diff(old_text=data[2], new_text=content)
                    print(diff)
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