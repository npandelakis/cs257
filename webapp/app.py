#!/usr/bin/env python3
'''
    webapp.py
    Grace de Benedetti and Nick Pandelakis
    6 November 2020

    A tiny Flask web application, including API, to be used
    as a template for setting up your web app assignment.
'''
import sys
import argparse
import flask
import api
import psycopg2
import json
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

# This route supports relative links among your web pages, assuming those pages
# are stored in the templates/ directory or one of its descendant directories,
# without requiring you to have specific routes for each page.
def get_world_data ():
    connection = connect_to_database()
    cursor = connection.cursor()
    query = "SELECT country_attacks_per_year.country_id, country_attacks_per_year.year, country_attacks_per_year.number_of_attacks, countries.country_name FROM country_attacks_per_year, countries WHERE country_attacks_per_year.country_id = countries.id;"
    cursor.execute(query)
    country_list = []
    for row in cursor:
      one_country = {}
      one_country['id'] = int(row[0])
      one_country['year'] = int(row[1])
      one_country['number_of_attacks'] = row[2]
      one_country['country_name'] = row[3]
      country_list.append(one_country)
    return country_list

@app.route('/world')
def get_world():
    country_list = get_world_data()
    return json.dumps(country_list)

if __name__ == '__main__':
    parser = argparse.ArgumentParser('A tiny Flask application, including API')
    parser.add_argument('host', help='the host on which this application is running')
    parser.add_argument('port', type=int, help='the port on which this application is listening')
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port, debug=True)
