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
    start_year = request.args.get('start_year', default = 1900)
    end_year = request.args.get('end_year', default = 2021)
    country_dict = get_world_data(start_year, end_year)
    return json.dumps(country_dict)

def get_world_data (start_year,end_year):
    connection = connect_to_database()
    cursor = connection.cursor()
    query = '''SELECT country_codes, sum(number_of_attacks)
            FROM country_attacks_per_year AS c JOIN countries ON c.country_id = countries.id
            WHERE countries.id IS NOT NULL AND c.year >= %s  AND c.year <= %s
            GROUP BY (country_codes) ORDER BY sum(number_of_attacks) DESC;'''
    cursor.execute(query, (start_year, end_year))

    #Copying colors from NY Times Covid Map
    color_palette = [
                    "#f2df91",
                    "#f9c467",
                    "#ffa83e",
                    "#ff8b24",
                    "#fd6a0b",
                    "#f04f09",
                    "#d8382e",
                    "#c62833",
                    "#AF1C43",
                    "#8A1739",
                    "#701547",
                    "#4C0D3E"
                    ]
    country_dict = {}

    #Starting values to assign fillColor
    index = 11
    min_number = 22000
    for row in cursor:
        if int(row[1]) >= min_number:
            fill_color = color_palette[index]
        else:
            index = index - 1
            min_number = min_number - 2000
            fill_color = color_palette[index]

        if row[0] != '-99':
            country_dict[row[0]] = {'country_code' : row[0], 'number_of_attacks' : int(row[1]), 'fillColor' : fill_color}
    return country_dict

@api.route('/countries/<country_code>')
def get_country(country_code):
    #Allow for lowercase country codes
    country_code = country_code.upper()
    start_year = request.args.get('start_year', default = 1900)
    end_year = request.args.get('end_year', default = 2021)
    country_ids_tuple = get_country_ids(country_code)
    country_attacks = get_country_attacks(country_ids_tuple, start_year, end_year)
    return json.dumps(country_attacks)

def get_country_attacks(country_ids_tuple, start_year, end_year):
    connection = connect_to_database()
    cursor = connection.cursor()
    query = '''SELECT id, year, month, day, latitude, longitude, summary
            FROM attacks
            WHERE country_id in %s
            AND year >= %s
            And year <= %s;'''
    cursor.execute(query, (country_ids_tuple, start_year, end_year))
    country_attacks_list = []
    for row in cursor:
        #return lat and long as strings to preserve precise decimal values
        country_attacks_list.append({ 'id' : int(row[0]),
                                'year' : int(row[1]),
                                'month' : int(row[2]),
                                'day' : int(row[3]),
                                'latitude' : str(row[4]),
                                'longitude' : str(row[5]),
                                'summary' : row[6]})

    return country_attacks_list

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

def get_country_name(country_code):
    country_code = country_code.upper()

    connection = connect_to_database()
    cursor = connection.cursor()
    query = '''SELECT country_name FROM countries WHERE country_codes = %s LIMIT 1;'''
    cursor.execute(query, (country_code,))

    country_name = None

    for row in cursor:
        country_name = row[0]

    return country_name

@api.route('/attack/<attack_id>')
def get_attack(attack_id):
    start_year = request.args.get('start_year', default = 1960)
    end_year = request.args.get('end_year', default = 2018)
    attack_info = get_attack_info(attack_id, start_year, end_year)
    return json.dumps(attack_info)

def get_attack_info(attack_id, start_year, end_year):
    connection = connect_to_database()
    cursor = connection.cursor()
    query = '''SELECT attacks.id,
            year,
        	month,
        	day,
        	countries.country_name,
        	province,
        	city,
        	latitude,
        	longitude,
        	location,
        	summary,
        	attack_types.attack_type,
        	success,
        	suicide,
        	target_types.target_type,
        	target_subtypes.target_subtype,
        	target,
        	perp,
        	motive,
        	weapon_types.weapon_type,
        	weapon_subtypes.weapon_subtype,
        	weapon_detail,
        	number_killed,
        	number_wounded,
        	property_damage.damage_extent
            FROM attacks
            LEFT JOIN countries ON attacks.country_id = countries.id
            LEFT JOIN attack_types ON attacks.attack_type_id = attack_types.id
            LEFT JOIN target_types ON attacks.target_type_id = target_types.id
            LEFT JOIN target_subtypes ON attacks.target_subtype_id = target_subtypes.id
            LEFT JOIN weapon_types ON attacks.weapon_type_id = weapon_types.id
            LEFT JOIN weapon_subtypes ON attacks.weapon_subtype_id = weapon_subtypes.id
            LEFT JOIN property_damage ON attacks.property_damage_id = property_damage.id
            WHERE attacks.id = %s
            AND year >= %s
            And year <= %s;'''
    cursor.execute(query, (attack_id, start_year, end_year))

    attack_dict = {}

    for row in cursor:
        #return lat and long as strings to preserve precise decimal values
        #and because JSON doesn't like decimals
        attack_dict = {'id' : int(row[0]),
                        'Year' : int(row[1]),
                        'Month' : int(row[2]),
                        'Day' : int(row[3]),
                        'Country' : str(row[4]),
                    	'Province/State' : str(row[5]),
                    	'City' : str(row[6]),
                        'Latitude' : str(row[7]),
                        'Longitude' : str(row[8]),
                        'Location' : str(row[9]),
                        'summary' : str(row[10]),
                        'Attack Type': str(row[11]),
                    	'Success': "Yes" if str(row[12]) == '1' else "No",
                    	'Suicide' : "Yes" if str(row[13]) == '1' else "No",
                    	'Target Type' : str(row[14]),
                    	'Target Subtype' : str(row[15]),
                    	'Target' : str(row[16]),
                    	'Perpetrator' : str(row[17]),
                    	'Motive' : str(row[18]),
                    	'Weapon Type' : str(row[19]),
                    	'Weapon Subtype' : str(row[20]),
                    	'Weapon Detail' : str(row[21]),
                    	'Number Killed' : str(row[22]),
                    	'Number Wounded' : str(row[23]),
                    	'Property Damage Amount' : str(row[24])}

    return attack_dict


@api.route('/centroid/<country_code>')
def get_centroid(country_code):
    #centroid is necessary to center each country map
    country_code = country_code.upper()
    connection  = connect_to_database()
    cursor = connection.cursor()
    query = '''SELECT centroid_long,centroid_lat FROM countries WHERE country_codes = %s LIMIT 1;'''
    cursor.execute(query, (country_code,))

    centroid_coords = []
    for row in cursor:
        centroid_coords.append({"longitude" : str(row[0]), "latitude" : str(row[1])})

    return json.dumps(centroid_coords)

@api.route('/search/<search_text>')
def get_area(search_text):
    #Allow for lowercase country codes
    search_text = search_text.upper()
    start_year = request.args.get('start_year', default = 1960)
    end_year = request.args.get('end_year', default = 2018)
    country_ids_tuple = get_country_ids(search_text)
    country_attacks = get_country_attacks(country_ids_tuple, start_year, end_year)
    return json.dumps(country_attacks)

@api.route('/countrynames/<search_text>')
def get_countries(search_text):
    search_text = search_text.lower()
    upper_search_text = search_text.upper()
    country_name_search_text = search_text[0].upper() + search_text[1:]
    connection  = connect_to_database()
    cursor = connection.cursor()
    code_search_text = '%' + upper_search_text + '%'
    name_search_text = '%' + country_name_search_text + '%'
    query = '''SELECT country_name, country_codes FROM countries WHERE country_name LIKE %s OR country_codes LIKE %s LIMIT 15;'''
    cursor.execute(query, (name_search_text, code_search_text))
    country_options = []
    for row in cursor:
        #countryName = row[0]
        country_options.append({"country_name" : row[0], "country_code" : row[1]})
    return json.dumps(country_options)
