from datetime import datetime

from pony.orm import Database, PrimaryKey, Required

db = Database()


class Articles(db.Entity):
    id = PrimaryKey(int, auto=True)
    article_id = Required(str, unique=True)
    pub_date = Required(datetime)
    link = Required(str)
    title = Required(str)
    summary = Required(str)


def db_setup():
    """Connect to the db and create it if it doesn't already exists"""
    db.bind(provider="sqlite", filename="../news.db", create_db=True)
    db.generate_mapping(create_tables=True)