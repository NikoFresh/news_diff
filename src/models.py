from datetime import datetime
from threading import Condition

from config import Config
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
    db.bind(
        provider="mysql",
        host=Config.DB_HOST,
        user=Config.DB_USER,
        passwd=Config.DB_PWD,
        db=Config.DB,
    )
    db.generate_mapping(create_tables=True)
