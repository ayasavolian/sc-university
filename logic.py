from sqlalchemy_declarative import Base, User, Chapter, Test, Question, Response, AEDT
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///sqlalchemy_example.db')
Base.metadata.bind = engine

DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

session.query(User).all()

user = session.query(User).first()
print user.first_name