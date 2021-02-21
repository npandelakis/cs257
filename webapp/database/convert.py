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










if __name__=='__main__':
    main()


