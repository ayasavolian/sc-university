from flask import Flask, render_template, redirect, jsonify, request, url_for, session
import httplib2
import json
from urllib import urlencode
from logic import run_class
import string
import random

app = Flask(__name__)

def sumSessionCounter():
  if 'counter' in session:
    session['counter'] += 1
  else:
    session['counter'] = 1
    session['id'] = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(15))

@app.route('/')
def main():
  sumSessionCounter()
  if 'username' in session:
    return render_template('home.html',
                           user = session['username'])
  else:
    return redirect(url_for('login'))

@app.route('/login')
def login():
  sumSessionCounter()
  if 'username' in session:
    return redirect(url_for('main'))
  else:
    return render_template('login.html',
                           id = session['id'])

@app.route('/creds', methods=['POST'])
def creds():
  print "this is a test"
  if request.method == 'POST':
    data = request.json
    if data['valueAdd'] == session['id']:
      login = run_class('Check_Login', data)
    value_pass = {
      'resp' : "fail"
    }
    if login == "false":
      return json.dumps(value_pass)
    else: 
      value_pass['resp'] = "success"
      session['username'] = login['username']
      return json.dumps(value_pass)

@app.route('/clear')
def clearsession():
  session.clear()
  return redirect(url_for('login'))

if __name__ == '__main__':
    app.secret_key = "F8u15h9hgd09hgaw4nogo23i188"
    app.run()