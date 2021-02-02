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
    '''creates a dictionary of lists of each olympic games'''
    try:
        connection = connect_to_database()
        cursor = connection.cursor(cursor_factory = RealDictCursor)
        query = '''SELECT id, year, season, city FROM games;'''
        cursor.execute(query)
        results = cursor.fetchall()
        return json.dumps(results)
    except Exception as e:
        print(e)    
    



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
  '''
  returns first matching games ID
  '''  
  ID = flask.request.args.get('id')
  NOC = flask.request.args.get('noc')
  results = make_dictionaries(ID, 'Gold', NOC)
  results += make_dictionaries(ID, 'Silver', NOC)
  results += make_dictionaries(ID, 'Bronze', NOC)
  return json.dumps(results)
  
  
def make_dictionaries(ID, medal, noc):
    '''
    makes the dictionaires where athlete_id, athlete_name, athlete_sex, sport, event, medal
    '''
    try:
        connection = connect_to_database()
        cursor = connection.cursor(cursor_factory = RealDictCursor)
        query = '''SELECT results.athlete_id, , athletes.athlete_name, athlete_stats.sex, sports.sport_name, events.events_name, results.medal FROM results, athletes, athlete_stats, sports, events WHERE events.event_id = {} AND results.medal = {} AND teams.team_name = {}'''.format(ID,medal,noc)
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except Exception as e:
        print(e)    