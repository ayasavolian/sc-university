from sqlalchemy_declarative import Base, User, Chapter, Test, Question, Response, AEDT
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///sqlalchemy_example.db')
Base.metadata.bind = engine

DBSession = sessionmaker()
DBSession.bind = engine

class Check_Login(object):
  def __init__(self, creds, session):
    self.username = creds.get("username")
    self.password = creds.get("password")
    self.session = session;
  def check_existence(self):
    user = self.session.query(User).\
            filter(User.username == self.username) 
    person = "false"
    for single in user:
      person = {
        'username' : single.username,
      }
    return person

def run_class(value, data):
    session = DBSession()
    if value == "Check_Login":
      try:
          login = Check_Login(data, session)
          person = login.check_existence()
          session.commit()
          return person
      except:
          session.rollback()
          raise
      finally:
          session.close()