#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 15:27:18 2021

@author: samuelgloss and nickpandelakis
"""

import sys
import argparse
import flask
import json
import psycopg2
from psycopg2.extras import RealDictCursor
from config import user, database, password

app = flask.Flask(__name__)

def connect_to_database():
    try:
        connection = (psycopg2.connect(database = database, user = user, password = password))
        return connection
    except Exception as e:
        print(e)

@app.route('/games')
def each_olympics_list():
    olympics_list = []
    ID = flask.request.args.get('id')
    year = flask.request.args.get('year')
    season = flask.request.args.get('season')
    city = flask.request.args.get('city')



@app.route('/nocs')
def each_NOC_list(): 
    try:
        connection = connect_to_database()
        cursor = connection.cursor(cursor_factory = RealDictCursor)
        query = '''SELECT noc, noc_region FROM nocs;'''
        cursor.execute(query)
        results = cursor.fetchall()
        return json.dumps(results)
    except Exception as e:
        print(e)    

@app.route('/medalists/games/<games_id>?[noc=noc_abbreviation]')

def medalist_list():
    '''returns first matching games ID'''  
    actor_dictionary = {}
    lower_last_name = last_name.lower()
    for actor in actors:
        if actor['last_name'].lower().startswith(lower_last_name):
            actor_dictionary = actor
            break
    return json.dumps(actor_dictionary)








if __name__ == '__main__':
    app.run(host = 'localhost', port = 5000, debug = True)







