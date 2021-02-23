#!/usr/bin/env python3
'''
    app.py
    Grace de Benedetti and Nick Pandelakis
    22 February 2021

    A Flask web application, including API, to be used
    as a template for setting up the rest of our web app.
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

app = flask.Flask(__name__)
#app.register_blueprint(api.api, url_prefix='/api')
def connect_to_database():
 try:
     connection = psycopg2.connect(database=database, user=user, password=password)
     return connection
 except Exception as e:
     print(e)
     exit()

# This route delivers the user your site's home page.
@app.route('/')
def home():
    return flask.render_template('world-map.html')

@app.route('/world')
def get_world():
    start_year = request.args.get('start_year', default = 1960)
    end_year = request.args.get('end_year', default = 2018)
    country_list = get_world_data(start_year, end_year)
    return json.dumps(country_list)

def get_world_data (start_year,end_year):
    connection = connect_to_database()
    cursor = connection.cursor()
    #query = "SELECT country_attacks_per_year.country_id, country_attacks_per_year.year, country_attacks_per_year.number_of_attacks, countries.country_name FROM country_attacks_per_year, countries WHERE country_attacks_per_year.country_id = countries.id;"
    query = '''SELECT country_name, country_codes, sum(number_of_attacks) 
            FROM country_attacks_per_year AS c JOIN countries ON c.country_id = countries.id 
            WHERE countries.country_codes IS NOT NULL AND c.year >= %s  AND c.year <= %s 
            GROUP BY (country_name, country_codes);'''
    cursor.execute(query, (start_year, end_year))
    country_dict = {}
    for row in cursor:
      country_dict[row[1]] = {'country_name' : row[0], 'number_of_attacks' : int(row[2]), 'fillColor' : '#F48FB1'}
      #one_country['country_code'] = row[1]
      #one_country['number_of_attacks'] = int(row[2])
      #country_list.append(one_country)
    return country_dict

if __name__ == '__main__':
    parser = argparse.ArgumentParser('A tiny Flask application, including API')
    parser.add_argument('host', help='the host on which this application is running')
    parser.add_argument('port', type=int, help='the port on which this application is listening')
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port, debug=True)
