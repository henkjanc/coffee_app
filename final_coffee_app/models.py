# flask_sqlalchemy/models.py
from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship,
                            backref)
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///database.sqlite3', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
# We will need this for querying
Base.query = db_session.query_property()


class CoffeeBar(Base):
    __tablename__ = 'coffeebar'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    intro = Column(String)
    description = Column(String)
    image = Column(String)
    rating = Column(Integer)

    def __repr__(self):
        return self.name

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    message = Column(String)
    date_created = Column(DateTime, default=func.now())
    coffeebar_id = Column(Integer, ForeignKey('coffeebar.id'))
    coffeebar = relationship(
        CoffeeBar,
        backref=backref('comments',
                        uselist=True,
                        cascade='delete,all'))

    def __repr__(self):
        return self.message
