import feedparser
from furl import furl

from .db import add_to_db, get_article_data, update_data
from .utils import check_diff, generate_img, parse, send_img


def start(link: str) -> None:
    print("\n\nstarting...")
    posts = feedparser.parse(link).entries
    for post in posts:
        try:

            # The RSS feed contains some extra links to external parts of the site that don't contains
            # A summary. Do not get the data from them
            # Eg: video.correre.it or corriere.it/economia/..
            f = furl(post.link)
            if any(
                x in f.path.segments
                for x in ["economia", "spettacoli", "motori", "cook", 'lodicoalcorrere', 'scuola']
            ) or any(x in f.host for x in ["motori", "video"]):
                continue

            # Get the current data from the website
            article_id, pub_date, article_link, title, summary = parse(post=post)
            # Check if the articles is already in the DB. If so, get the data
            data = get_article_data(id=article_id)
            if data != None:
                print('check')
                changes: int = 0
                if data[0] != title:
                    diff: str = check_diff(data[0, title])
                    generate_img(diff)
                    send_img(desc=f'Titolo\n<a href="{article_link}">{title}</a>')
                    changes += 1
                if data[1] != summary:
                    diff: str = check_diff(data[1], summary)
                    print(diff)
                    generate_img(diff)
                    send_img(desc=f'Sottotitolo\n<a href="{article_link}">{title}</a>')
                    changes += 1
                # Update the data only if there is any change
                if changes > 0:
                    update_data(id=article_id, title=title, summary=summary)
            else:
                print('add')
                # Add the article to the db
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
