from sqlalchemy import Column, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.sqltypes import DateTime, Integer, String

Base = declarative_base()

engine = create_engine('sqlite:///news.db', echo = True)

class Articles(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    link = Column(String)
    title = Column(String)
    description = Column(String)
    pubDate = Column(DateTime)

Base.metadata.create_all(engine)
Session = sessionmaker(bind = engine)
session = Session()