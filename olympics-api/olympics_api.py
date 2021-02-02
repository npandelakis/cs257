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
    '''Connect to the olympics database with specified user and password.'''
    try:
        connection = (psycopg2.connect(database = database, user = user, password = password))
        return connection
    except Exception as e:
        print(e)



@app.route('/')
def get_home_page():
    return 'Hello CS 257'




@app.route('/games')

def get_games_list():
    '''returns a list of dictionaries of each olympic games'''
    try:
        connection = connect_to_database()
        cursor = connection.cursor(cursor_factory = RealDictCursor)
        query = '''SELECT id, year, season, city FROM games ORDER BY year ASC;'''
        cursor.execute(query)
        results = cursor.fetchall()
    except Exception as e:
        print(e)    
    
    connection.close()
    return json.dumps(results)



@app.route('/nocs')

def get_noc_list():
    '''returns a list of dictionaries of nocs and the noc region.'''
    try:
        connection = connect_to_database()
        cursor = connection.cursor(cursor_factory = RealDictCursor)
        query = '''SELECT noc, noc_region FROM nocs;'''
        cursor.execute(query)
        results = cursor.fetchall()
    except Exception as e:
        print(e)    

    connection.close
    return json.dumps(results)

@app.route('/medalists/games/<games_id>')

def get_medalist_list(games_id):
    '''returns medalists for a given games year. Can be optionally filtered for a specific noc.'''
    ID = games_id
    NOC = flask.request.args.get('noc')
    try:
        connection = connect_to_database()
        cursor = connection.cursor(cursor_factory = RealDictCursor)

        if NOC:
            query = '''SELECT athletes.id, athlete_name, sex, sport_name, event_name, medal FROM athletes JOIN athlete_stats ON athletes.id = athlete_stats.athlete_id LEFT JOIN results ON athletes.id = results.athlete_id JOIN nocs ON results.noc_id = nocs.id JOIN games ON results.games_id = games.id LEFT OUTER JOIN sports ON results.sport_id = sports.id JOIN events ON results.event_id = events.id WHERE games.id = %s AND nocs.noc = %s AND results.medal IS NOT NULL;'''
            cursor.execute(query,(ID,NOC))
            results = cursor.fetchall()

        else:
            query = '''SELECT athletes.id, athlete_name, sex, sport_name, event_name, medal FROM athletes JOIN athlete_stats ON athletes.id = athlete_stats.athlete_id LEFT JOIN results ON athletes.id = results.athlete_id JOIN games ON results.games_id = games.id LEFT OUTER JOIN sports ON results.sport_id = sports.id JOIN events ON results.event_id = events.id WHERE games.id = %s AND results.medal IS NOT NULL;'''
            cursor.execute(query, (ID,))
            results = cursor.fetchall()
    except Exception as e:
        print(e)
    
    connection.close()
    return json.dumps(results)
  


if __name__ == '__main__':
    parser = argparse.ArgumentParser('An olympics Flask API')
    parser.add_argument('host', help='the host on which this application is running')
    parser.add_argument('port', type=int, help='the port on which this application is listening')
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port, debug=True)
