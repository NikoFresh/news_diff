from sqlalchemy import Column, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.sqltypes import DateTime, Integer, String

Base = declarative_base()

engine = create_engine("sqlite:///news.db")


class Articles(Base):
    __tablename__ = "articles"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    article_id = Column("article_id", Integer, unique=True)
    link = Column("link", String)
    title = Column("title", String)
    summary = Column("summary", String)
    content = Column("content", String)
    pub_date = Column("pub_date", DateTime)


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
