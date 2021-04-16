from sqlalchemy import exists

from .models import Articles, Session


def is_already_present(id: int) -> bool:
    """Check if the article is already in the DB"""
    session = Session()
    output = session.query(exists().where(Articles.article_id == id)).scalar()
    session.close()
    return output


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
