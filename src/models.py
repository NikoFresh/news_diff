from datetime import datetime

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
    data = Config.DB_URL.split('/')
    database = data[-1]
    credentials = data[2].split('@')
    host, port = credentials[-1].split(':')
    user, password = credentials[0].split(':')

    db.bind(provider="postgres", user=user, password=password, host=host, database=database, port=port, sslmode="require")
    db.generate_mapping(create_tables=True)
