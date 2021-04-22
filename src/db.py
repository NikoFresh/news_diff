from pony.orm import commit, db_session, select

from .models import Articles


@db_session
def get_article_data(id: str) -> bool or tuple[str]:
    """Check if the article is already in the DB. If so return the data"""
    entry_exists = select(c for c in Articles if c.article_id == id).exists()
    if entry_exists:
        data = select(c for c in Articles if c.article_id == id).first()
        return (data.title, data.summary)


@db_session
def add_to_db(id: str, pub_date, link: str, title: str, summary: str) -> None:
    """Add the article to the db"""
    new_article = Articles(
        article_id=id, pub_date=pub_date, link=link, title=title, summary=summary
    )
    commit()


@db_session
def update_data(id: str, title: str, summary: str) -> None:
    """Update the data in the DB"""
    data = select(c for c in Articles if c.article_id == id).first()
    data.title = title
    data.summary = summary
    commit()