'''
    api.py
    Grace de Benedetti and Nick Pandelakis
    23 February 2021

    Tiny Flask API to support the tiny books web application.
'''
import sys
import argparse
import flask
import api
import psycopg2
import json
from flask import request
from config import user
from config import password
from config import database

api = flask.Blueprint('api', __name__)
def connect_to_database():
 try:
     connection = psycopg2.connect(database=database, user=user, password=password)
     return connection
 except Exception as e:
     print(e)
     exit()

@api.route('/world/')
def get_world():
    start_year = request.args.get('start_year', default = 1960)
    end_year = request.args.get('end_year', default = 2018)
    country_list = get_world_data(start_year, end_year)
    return json.dumps(country_list)

def get_world_data (start_year,end_year):
    connection = connect_to_database()
    cursor = connection.cursor()
    #query = "SELECT country_attacks_per_year.country_id, country_attacks_per_year.year, country_attacks_per_year.number_of_attacks, countries.country_name FROM country_attacks_per_year, countries WHERE country_attacks_per_year.country_id = countries.id;"
    query = '''SELECT country_name, country_id, sum(number_of_attacks)
            FROM country_attacks_per_year AS c JOIN countries ON c.country_id = countries.id
            WHERE countries.id IS NOT NULL AND c.year >= %s  AND c.year <= %s
            GROUP BY (country_name, country_id);'''
    cursor.execute(query, (start_year, end_year))
    country_dict = {}
    for row in cursor:
      country_dict[row[1]] = {'country_name' : row[0], 'number_of_attacks' : int(row[2]), 'fillColor' : '#F48FB1'}
      #one_country['country_code'] = row[1]
      #one_country['number_of_attacks'] = int(row[2])
      #country_list.append(one_country)
    return country_dict
