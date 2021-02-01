'''
convert.py
This program converts one large kaggle csv into smaller csvs that correspond
with a specific database.
Written by Nick Pandelakis for cs257
'''

import csv


def create_athletes_csv(reader_list):
    writer = csv.writer(open('athletes.csv', 'w'))
    name_index = 1 
    i = 1
    for row in reader_list[1:]:
        # Add athletes by index to csv, ignore potentially different spellings after the athlete has been added
        if i == int(row[0]):
            writer.writerow([i, row[name_index]])
            i = i + 1


def create_sports_csv(reader_list):
    writer = csv.writer(open('sports.csv','w'))
    sport_index = 12
    sport_dict = create_id_dict(reader_list, sport_index)

    for key in sport_dict:
        writer.writerow([sport_dict[key], key])
    
def create_events_csv(reader_list):
    writer = csv.writer(open('events.csv','w'))
    event_index = 13
    event_dict = create_id_dict(reader_list, event_index)

    for key in event_dict:
        writer.writerow([event_dict[key], key])

def create_teams_csv(reader_list):
    writer = csv.writer(open('teams.csv','w'))
    team_index = 6
    team_dict = create_id_dict(reader_list, team_index)

    for key in team_dict:
        writer.writerow([team_dict[key], key])

def create_nocs_csv(reader_list): 
    writer = csv.writer(open('nocs.csv','w'))
    noc_dict = {}
    noc_index = 0
    region_index = 1
    i = 1

    for row in reader_list[1:]:
        if row[noc_index] not in noc_dict:
            noc_dict[row[noc_index]] = [i, row[region_index]]
            i = i + 1

    for key in noc_dict:
        writer.writerow([noc_dict[key][0], key, noc_dict[key][1]])
   
def create_games_csv(reader_list):
    writer = csv.writer(open('games.csv','w'))
    game_dict = {}
    games_index = 8
    city_index = 11
    i = 1
    for row in reader_list[1:]:
        if row[games_index] not in game_dict:
            game_dict[row[games_index]] = [i, row[city_index]]
            i = i + 1
    
    for key in game_dict:
        game_list = key.split()
        writer.writerow([game_dict[key][0], key, game_list[0], game_list[1], game_dict[key][1]])    

def create_athlete_stats_csv(reader_list):
    writer = csv.writer(open('athlete_stats.csv','w'))
    games_reader_list = list(csv.reader(open('games.csv')))
    games_id_dict = get_id_dict(games_reader_list)
    athlete_stats_set = set()
    id_index = 0
    sex_index = 2
    age_index = 3
    height_index = 4
    weight_index = 5
    games_index = 8

    for row in reader_list[1:]:
        games_id = games_id_dict[row[games_index]]
        athlete_id = int(row[id_index])
        athlete_stats_set.add((athlete_id, games_id, row[sex_index], row[age_index], row[height_index], row[weight_index]))
    
    for stats in athlete_stats_set:
        writer.writerow([stats[0], stats[1], stats[2], stats[3], stats[4], stats[5]])
    


def create_results_csv(reader_list):
    writer = csv.writer(open('results.csv','w'))
    
    games_reader_list = list(csv.reader(open('games.csv')))
    games_id_dict = get_id_dict(games_reader_list)

    teams_reader_list = list(csv.reader(open('teams.csv')))
    teams_id_dict = get_id_dict(teams_reader_list)

    noc_reader_list = list(csv.reader(open('nocs.csv')))
    noc_id_dict = get_id_dict(noc_reader_list)

    sports_reader_list = list(csv.reader(open('sports.csv')))
    sports_id_dict = get_id_dict(sports_reader_list)

    event_reader_list = list(csv.reader(open('events.csv')))
    event_id_dict = get_id_dict(event_reader_list)

    athlete_id_index = 0
    team_index = 6
    noc_index = 7
    games_index = 8
    sport_index = 12
    event_index = 13
    medal_index = 14

    i = 1

    for row in reader_list[1:]:
        writer.writerow([
            i,
            row[athlete_id_index],
            teams_id_dict[row[team_index]],
            noc_id_dict[row[noc_index]],
            games_id_dict[row[games_index]],
            sports_id_dict[row[sport_index]],
            event_id_dict[row[event_index]],
            row[medal_index] ])
        
        i = i + 1

def get_id_dict(reader_list):
    '''
    get dictionary from linking table csv files
    '''
    id_dict = {}
    for row in reader_list:
        id_dict[row[1]] = row[0]
    return id_dict

def create_id_dict(reader_list, index):
    '''
    create dictionary for the creation of linking csv files
    '''
    id_dict = {}
    i = 1
    for row in reader_list[1:]:
        if row[index] not in id_dict:
            id_dict[row[index]] = i
            i = i + 1
    
    return id_dict



def main():
    athlete_results_list = list(csv.reader(open('athlete_events.csv', 'r')))
    noc_regions_list = list(csv.reader(open('noc_regions.csv','r')))
    create_athletes_csv(athlete_results_list)
    create_sports_csv(athlete_results_list)
    create_events_csv(athlete_results_list)
    create_teams_csv(athlete_results_list)
    create_nocs_csv(noc_regions_list)
    create_games_csv(athlete_results_list)
    create_athlete_stats_csv(athlete_results_list)
    create_results_csv(athlete_results_list)

if __name__ == '__main__':
    main()


