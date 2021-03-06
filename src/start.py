import logging

import feedparser
from config import Config
from furl import furl

from .db import add_to_db, get_article_data, update_data
from .utils import check_diff, generate_img, parse, send_img


def start(link: str) -> None:
    logging.info('\nStarting...')
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
                logging.info(f'Checking {article_id}')
                changes: int = 0
                # If there has been a change in either the title or the summary, generate the image 
                # and send it to Telegram
                if data[0] != title:
                    logging.info(f'Change in {article_id} title')
                    diff: str = check_diff(data[0], title)
                    generate_img(diff)
                    send_img(desc=f'Titolo\n<a href="{article_link}">{title}</a>')
                    changes += 1
                if data[1] != summary:
                    logging.info(f'Change in {article_id} summary')
                    diff: str = check_diff(data[1], summary)
                    generate_img(diff)
                    send_img(desc=f'Sottotitolo\n<a href="{article_link}">{title}</a>')
                    changes += 1
                # Update the data only if there is any change
                if changes > 0:
                    update_data(id=article_id, title=title, summary=summary)
            else:
                # Add the article to the db
                logging.info(f'Adding {article_id} to db')
                add_to_db(
                    id=article_id,
                    pub_date=pub_date,
                    link=article_link,
                    title=title,
                    summary=summary,
                )
        except AttributeError:
            logging.debug(f'The page doesn\'t have the content')
        except Exception:
            logging.error('Error, skipping this URL')
    logging.info(f'Completed. Running again in {Config.SLEEP_TIME}s')
