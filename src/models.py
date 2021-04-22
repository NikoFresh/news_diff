from pony.orm import Database, Required, PrimaryKey
from datetime import datetime

db = Database()


class Articles(db.Entity):
    id = PrimaryKey(int, auto=True)
    article_id = Required(str, unique=True)
    pub_date = Required(datetime)
    link = Required(str)
    title = Required(str)
    summary = Required(str)


def db_setup():
    db.bind(provider="sqlite", filename="../news.db", create_db=True)
    db.generate_mapping(create_tables=True)