
from flask import Flask, request, redirect, session, render_template
from cas import CASClientV2

import sys
sys.path.append('..')

import config

app = Flask(__name__)

app.secret_key = config.SESSION_KEY

cas_client = CASClientV2(
    service_url=config.MY_URL,
    server_url="https://cas-dev.uwaterloo.ca/cas",
)

@app.route("/")
def index():
    if 'username' not in session:
        return redirect(cas_client.get_login_url())
    return render_template('vote.html', user=session['username'])

@app.route("/login")
def login():
    ticket = request.args.get('ticket')
    if ticket:
        user, attrs, pgtiou = cas_client.verify_ticket(ticket)
        session['username'] = user
        session['ticket'] = ticket
        return redirect('/')
    return 'Login failed'

@app.route('/logout')
def logout():
    del session['username']
    del session['ticket']
    return 'Logged out'


