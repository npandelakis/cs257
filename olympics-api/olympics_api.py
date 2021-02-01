'''
olympics_api.py
An api to query the olympics database that utilizes flask.
Written by Sam Gloss and Nick Pandelakis for cs257
'''

import flask
import psycopg2
import json

app = flask.Flask(__name__)

@app.route('/')
def hello():
    return ''

@app.route('/nocs')








@app.route('/games')
def get_games(cursor):
'''Returns a list of olympics games, as well as where they took place, in order by years'''
    games_dict = {}
    







@app.route('/medalists/games/<games_id>')









