'''
    api.py
    Grace de Benedetti and Nick Pandelakis
    23 February 2021

    Flask API to support the webapp project for cs257.
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
from decimal import Decimal

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
    country_dict = get_world_data(start_year, end_year)
    return json.dumps(country_dict)

def get_world_data (start_year,end_year):
    connection = connect_to_database()
    cursor = connection.cursor()
    #query = "SELECT country_attacks_per_year.country_id, country_attacks_per_year.year, country_attacks_per_year.number_of_attacks, countries.country_name FROM country_attacks_per_year, countries WHERE country_attacks_per_year.country_id = countries.id;"
    query = '''SELECT country_name, country_codes, sum(number_of_attacks)
            FROM country_attacks_per_year AS c JOIN countries ON c.country_id = countries.id
            WHERE countries.id IS NOT NULL AND c.year >= %s  AND c.year <= %s
            GROUP BY (country_name, country_codes);'''
    cursor.execute(query, (start_year, end_year))
    country_dict = {}
    for row in cursor:
      country_dict[row[1]] = {'country_name' : row[0], 'number_of_attacks' : int(row[2]), 'fillColor' : '#F48FB1'}
    return country_dict

@api.route('/countries/<country_code>')
def get_country(country_code):
    #Allow for lowercase country codes
    country_code = country_code.upper()
    start_year = request.args.get('start_year', default = 1960)
    end_year = request.args.get('end_year', default = 2018)
    country_attacks = get_country_attacks(country_code, start_year, end_year)
    return json.dumps(country_attacks)

def get_country_attacks(country_code, start_year, end_year):
    country_ids_tuple = get_country_ids(country_code)
    connection = connect_to_database()
    cursor = connection.cursor()
    query = '''SELECT id, year, month, day, latitude, longitude, summary
            FROM attacks
            WHERE country_id in %s
            AND year >= %s
            And year <= %s;'''
    cursor.execute(query, (country_ids_tuple, start_year, end_year))
    country_attacks_dict = {}
    for row in cursor:
        #return lat and long as strings to preserve precise decimal values
        country_attacks_dict[row[0]] = {'year' : int(row[1]),
                                'month' : int(row[2]),
                                'day' : int(row[3]),
                                'latitude' : str(row[4]),
                                'longitude' : str(row[5]),
                                'summary' : row[6]}

    return country_attacks_dict

def get_country_ids(country_code) -> tuple:
    connection  = connect_to_database()
    cursor = connection.cursor()
    query = '''SELECT id FROM countries WHERE country_codes = %s'''
    cursor.execute(query, (country_code,))

    country_id_list = []

    for row in cursor:
        country_id_list.append(row[0])

    #tuple type to allow for easy plugin to the query. This is necessary since some
    #countries share a country code, like East Germany and West Germany.
    return tuple(country_id_list)
