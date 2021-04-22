import feedparser

from .db import add_to_db, get_article_data, update_data
from .utils import check_diff, generate_img, parse, send_img


def start(link: str) -> None:
    print("\n\nstarting...")
    posts = feedparser.parse(link).entries
    for post in posts:
        try:
            article_id, pub_date, article_link, title, summary = parse(post=post)
            data = get_article_data(id=article_id)
            if data != None:
                changes: int = 0
                if data[0] != title:
                    diff: str = check_diff(data[0, title])
                    generate_img(diff)
                    send_img(desc=f"Titolo {article_link}")
                    changes += 1
                if data[1] != summary:
                    diff: str = check_diff(data[1], summary)
                    generate_img(diff)
                    send_img(desc=f"Sottotitolo {article_link}")
                    changes += 1
                if changes > 0:
                    update_data(id=article_id, title=title, summary=summary)
            else:
                print("add")
                add_to_db(
                    id=article_id,
                    pub_date=pub_date,
                    link=article_link,
                    title=title,
                    summary=summary,
                )
        except Exception as e:
            print(e)
    print("\ncompleted")
