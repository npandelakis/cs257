'''
convert.py
This program converts the global terrorism database (in csv format) into smaller csvs that correspond to a specific database.
Written by Nick Pandelakis and Grace de Benedetti for cs257
'''

import csv

def create_countries_csv(reader_list):
    writer = csv.writer(open('countries.csv', 'w'))
    id_index = 7
    country_index = 8
    country_dict = create_id_dict(reader_list, id_index, country_index)

    for key in country_dict:
        writer.writerow([country_dict[key], key])

def create_country_attacks_per_year_csv(reader_list):
    writer = csv.writer(open('country_attacks_per_year.csv', 'w'))
    id_index = 7
    year_index = 1
    country_year_dict = {}
    for row in reader_list[1:]:
        if (row[id_index], row[year_index]) in country_year_dict:
            country_year_dict[(row[id_index], row[year_index])] += 1
        else:
            country_year_dict[(row[id_index], row[year_index])] = 1
            
    for key in country_year_dict:
        writer.writerow([key[0], key[1], country_year_dict[key]])


def create_attack_types_csv(reader_list):
    writer = csv.writer(open('attack_types.csv', 'w'))
    id_index = 28
    type_index = 29
    type_dict = create_id_dict(reader_list, id_index, type_index)

    for key in type_dict:
        writer.writerow([type_dict[key], key])




def create_target_types_csv(reader_list):
    writer = csv.writer(open('target_types.csv', 'w'))
    id_index = 34
    type_index = 35
    type_dict = create_id_dict(reader_list, id_index, type_index)

    for key in type_dict:
        writer.writerow([type_dict[key], key])



def create_target_subtypes_csv(reader_list):
    writer = csv.writer(open('target_subtypes.csv', 'w'))
    id_index = 36
    type_index = 37
    type_dict = create_id_dict(reader_list, id_index, type_index)

    for key in type_dict:
        writer.writerow([type_dict[key], key])


def create_weapon_types_csv(reader_list):
    writer = csv.writer(open('weapon_types.csv', 'w'))
    id_index = 81
    type_index = 82
    type_dict = create_id_dict(reader_list, id_index, type_index)

    for key in type_dict:
        writer.writerow([type_dict[key], key])


def create_weapon_subtypes_csv(reader_list):
    writer = csv.writer(open('weapon_subtypes.csv', 'w'))
    id_index = 83
    type_index = 84
    type_dict = create_id_dict(reader_list, id_index, type_index)

    for key in type_dict:
        writer.writerow([type_dict[key], key])


def create_prop_damage_csv(reader_list):
    writer = csv.writer(open('prop_damage.csv', 'w'))
    id_index = 105
    prop_damage_index = 106
    prop_damage_dict = create_id_dict(reader_list, id_index, prop_damage_index)

    for key in prop_damage_dict:
        writer.writerow([prop_damage_dict[key], key])

def create_attacks_csv(reader_list):
    writer = csv.writer(open('attacks.csv', 'w'))
    id_index = 0
    year_index = 1
    month_index = 2
    day_index = 3
    country_id_index = 7
    province_index = 11
    city_index = 12
    latitude_index = 13
    longitude_index = 14
    location_index = 17
    summary_index = 18
    success_index = 26
    suicide_index = 27
    attack_type_id_index = 28
    target_type_id_index = 34
    target_subtype_id_index = 36
    target_index = 39
    perp_index = 58
    motive_index = 64
    weapon_type_id_index = 81
    weapon_subtype_id_index = 83
    weapon_detail_index = 97
    number_killed_index = 98
    number_wounded_index = 101
    property_damage_id_index = 105

    for row in reader_list[1:]:
        writer.writerow([
            row[id_index],
            row[year_index],
            row[month_index],
            row[day_index],
            row[country_id_index],
            row[province_index],
            row[city_index],
            row[latitude_index],
            row[longitude_index],
            row[location_index],
            row[summary_index],
            row[attack_type_id_index],
            row[success_index],
            row[suicide_index],
            row[target_type_id_index],
            row[target_subtype_id_index],
            row[target_index],
            row[perp_index],
            row[motive_index],
            row[weapon_type_id_index],
            row[weapon_subtype_id_index],
            row[weapon_detail_index],
            row[number_killed_index],
            row[number_wounded_index],
            row[property_damage_id_index]
            ])


def create_id_dict(reader_list, id_index, name_index):
    '''Create dictionary for linking table csv files'''
    id_dict = {}
    for row in reader_list[1:]:
        if row[name_index] not in id_dict:
            id_dict[row[name_index]] = row[id_index]

    return id_dict






def main():
    terrorism_list = list(csv.reader(open('terrorism.csv', 'r')))
    create_countries_csv(terrorism_list)
    create_country_attacks_per_year_csv(terrorism_list)
    create_attack_types_csv(terrorism_list)
    create_target_types_csv(terrorism_list)
    create_target_subtypes_csv(terrorism_list)
    create_weapon_types_csv(terrorism_list)
    create_weapon_subtypes_csv(terrorism_list)
    create_prop_damage_csv(terrorism_list)
    create_attacks_csv(terrorism_list)








if __name__=='__main__':
    main()


