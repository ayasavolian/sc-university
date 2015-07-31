import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()
 
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    role = Column(String(250), nullable=False)
    username = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

class Chapter(Base):
    __tablename__ = 'chapter'
    id = Column(Integer, primary_key=True)
    user = relationship(User)
    user_id = Column(Integer, ForeignKey('user.id'))
    chapter_name = Column(String(250), nullable=False)
    percent_complete = Column(Integer, default=0)

class Test(Base):
    __tablename__ = "test"
    id = Column(Integer, primary_key=True)
    chapter = relationship(Chapter)
    chapter_id = Column(Integer, ForeignKey('chapter.id'), nullable=False)
    score = Column(Integer, default=0)

class Question(Base):
    __tablename__ = "question"
    id = Column(Integer, primary_key=True)
    test = relationship(Test)
    test_id = Column(Integer, ForeignKey('test.id'))
    question = Column(String(250), nullable=False)

class Response(Base):
    __tablename__ = "response"
    id = Column(Integer, primary_key=True)
    question = relationship(Question)
    question_id = Column(Integer, ForeignKey('question.id'))
    user = relationship(User)
    user_id = Column(Integer, ForeignKey('user.id'))
    response = Column(String(250))

class AEDT(Base):
    __tablename__ = "aedt"
    id = Column(Integer, primary_key=True)
    coach = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User)
    attended = Column(String(250))
    rating = Column(Integer)
    feedback = Column(String(2000))

 
# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///sqlalchemy_example.db')
 
# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)