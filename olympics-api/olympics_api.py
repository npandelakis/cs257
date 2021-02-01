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


app = flask.Flask(__name__)



@app.route('/games')

def each_olympics_list():
    olympics_list = []
    ID = flask.request.args.get('id')
    year = flask.request.args.get('year')
    season = flask.request.args.get('season')
    city = flask.request.args.get('city')



@app.route('/nocs')

def each_NOC_list():
    pass


@app.route('/medalists/games/<games_id>?[noc=noc_abbreviation]')

def medalist_list():
  '''
  returns first matching games ID
  '''  
  
  actor_dictionary = {}
  lower_last_name = last_name.lower()
  for actor in actors:
        if actor['last_name'].lower().startswith(lower_last_name):
            actor_dictionary = actor
            break
    return json.dumps(actor_dictionary)
