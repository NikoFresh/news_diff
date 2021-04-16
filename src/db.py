from sqlalchemy import exists

from .models import Articles, Session


def get_article_data(id: int) -> bool or tuple[str]:
    """Check if the article is already in the DB. If so return the data"""
    session = Session()
    entry_exists = session.query(exists().where(Articles.article_id == id)).scalar()
    if entry_exists:
        data = session.query(Articles).filter(Articles.article_id == id).one()
        session.close()
        return (data.title, data.summary, data.content)


def add_to_db(
    id: int, pub_date, link: str, title: str, summary: str, content: str
) -> None:
    session = Session()
    new_article = Articles()
    (
        new_article.article_id,
        new_article.link,
        new_article.title,
        new_article.summary,
        new_article.content,
        new_article.pub_date,
    ) = (id, link, title, summary, content, pub_date)
    session.add(new_article)
    session.commit()
    session.close()


def update_data(id: int, title: str, summary: str, content: str) -> None:
    session = Session()
    old = session.query(Articles).filter(Articles.article_id == id).one()
    old.title = title
    old.summary = summary
    old.content = content
    session.commit()
    session.close()