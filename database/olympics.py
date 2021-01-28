'''
olympics.py
A command line interface for querying the olympics database.
Written by Nick Pandelakis for cs257
'''

import psycopg2
import argparse
from config import user, password, database

def connect_to_database():
    try:
        connection = psycopg2.connect(database = database, user = user, password = password)
        return connection
    except Exception as e:
        print(e)
        exit()

def get_parsed_arguments():
    '''Obtains and parses the command line arguments'''
    with open('.prolog.txt', 'r') as prolog, open('.epilog.txt', 'r') as epilog:
        parser = argparse.ArgumentParser(description = prolog.read(), epilog = epilog.read())
    
    parser.add_argument("-n", "--noc", help="One or more 3-letter NOC's to list the athletes for")

    parser.add_argument("-l", "--list", action = 'store_true', help="List the number of gold medals won by each NOC in descending order")

    parser.add_argument("-a", "--athlete", help="Lists a specific athlete, as well as their sex, height, and weight for each Olympic game they competed in.")

    parsed_arguments = parser.parse_args()
    return parsed_arguments

def query_noc_athletes(noc, cursor):
    try:
        query_string = noc 
        query = '''SELECT DISTINCT athlete_name FROM athletes JOIN results ON athletes.id = results.athlete_id JOIN nocs ON results.noc_id = nocs.id WHERE nocs.noc = %s'''
        cursor.execute(query, (query_string,))
        return cursor
    except Exception as e:
        print(e)
        exit()

def query_noc_gold_medals(cursor):
    try:
        query = '''SELECT noc, count(medal) FROM results JOIN nocs ON results.noc_id = nocs.id WHERE medal = 'Gold' GROUP BY nocs.noc ORDER BY COUNT(Medal) DESC;'''
        cursor.execute(query)
        return cursor
    except Exception as e:
        print(e)
        exit()

def query_athlete_stats(athlete, cursor):
    try:
        













def print_noc_athletes(noc, cursor):
    print('===== All Athletes from ' + noc + ' =====')
    for row in cursor:
        print(row[0])
    print()

def print_noc_gold_medals(cursor):
    print('===== NOCS and their total gold medals =====')
    for row in cursor:
        print(row[0], row[1])
    print()    




def main():
    arguments = get_parsed_arguments()
    connection = connect_to_database()
    cursor = connection.cursor()

    if arguments.noc: 
        noc_athletes = query_noc_athletes(arguments.noc, cursor)
        print_noc_athletes(arguments.noc, noc_athletes)
    if arguments.list:
        noc_gold_medals = query_noc_gold_medals(cursor)
        print_noc_gold_medals(noc_gold_medals)
    if arguments.athlete:
        athlete_stats = query_athlete_stats(arguments, cursor)
        print_athlete_stats(arguments.athlete, athlete_stats) if __name__ == '__main__': main()
