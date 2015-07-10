from flask import Flask, render_template
import httplib2
from urllib import urlencode
from sqlalchemy import *
from sqlalchemy.sql import *

app = Flask(__name__)
'''
users = Table('users', metadata,
   Column('id', Integer, Sequence('user_id_seq'), primary_key=True),
   Column('name', String(50)),
   Column('fullname', String(50)),
   Column('password', String(12))
)
'''
@app.route('/')
def main():
    return render_template('home.html')

@app.route("/test")
def test():
    connection = engine.connect()
    i = users.insert()
    i.execute({'name': 'Peter', 'password': 'Kim'},
             {'name': 'Gary', 'password': 'Lochhead'},
              {'name': 'Laura', 'password': 'Fanning'})

    #connection = engine.connect()
    return "hello world!"

    '''
    s = select([users.c.name, users.c.password]).where(users.c.name == 'Laura')
    result = connection.execute(s)
    for row in result:
      return "name:", row['name']
    connection.close()
    '''



    '''
    i.execute({'name': 'John', 'password': 'johnpassword'},
            {'name': 'Susan', 'password': 'susanpassword'},
            {'name': 'Carl', 'password': 'carlpassword'})

    s = users.select()
    rs = s.execute()

    row = rs.fetchone()
    print 'Id:', row[0]
    print 'Name:', row['name']
    print 'Password:', row[users.c.password]

    for row in rs:
      print row.name, 'is', row.password, 'is their password'
    '''

if __name__ == '__main__':
    app.run()

##This is related to SQL, get to this after you figure out posting and getting using Python
