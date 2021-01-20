'''
books.py
Written by Ross Grogan-Kaylor and Nick Pandelakis for cs257
Revised by Nick Pandelakis for 1/22
A command line interface for searching the 'books.csv' file.
'''

import csv
import argparse

# Interesting: "-b", "--book" vs. "b, --book": "-b", "--book" is the one you want (treats -b and --book as referring to the
# same argument); "-b, --book" treats -b and --book as referring to the same argument, but where -b can be specified with no args

def get_parsed_arguments():
    # Set up command line arguments.
    with open("prolog.txt", "r") as prolog, open("epilog.txt", "r") as epilog:
        parser = argparse.ArgumentParser(description = prolog.read(), epilog = epilog.read())

    parser.add_argument("-b", "--books", nargs="+", help="One or more substrings to search for in the titles of books. "
                                                        "If one of the substrings contains a space, surround that substring"
                                                        " with quotes \"\".")
    parser.add_argument("-a", "--authors", nargs="+",
                        help="One or more substrings to search for in the names of authors. If one of the substrings contains "
                             "a space, surround that substring with quotes \"\".")
    # may need to fix, see python3 books.py books.csv -b 'the' 1800 1899 for example
    parser.add_argument("year1", nargs = "?", help="One of the years in the time "
                                                                 "interval [min(year1, year2), max(year1, year2)] "
                                                                 "within which to search for books.")
    parser.add_argument("year2", nargs = "?", help="One of the years in the time "
                                                                 "interval [min(year1, year2), max(year1, year2)] "
                                                                 "within which to search for books.")
    # Parse the command line.
    parsed_arguments = parser.parse_args()

    # Handle the years.
    year1 = parsed_arguments.year1
    if parsed_arguments.year2 is None:
        parsed_arguments.year2 = year1

    # Note that year1 or year2 might still be None.
    return parsed_arguments 


def filter_books(filtered, books) -> list:
    title_index = 0
    return list(filter(lambda p: any(sub.lower() in p[title_index].lower() for sub in books), filtered))


def filter_authors(filtered, authors) -> list: 
    author_index = 2
    return list(filter(lambda p: any(sub.lower() in p[author_index].lower() for sub in authors), filtered))


def filter_years(filtered, year1, year2) -> list:
    year_index = 1
    return list(filter(lambda p: year1 <= p[year_index] and year2 >= p[year_index], filtered))


def get_authorset(filtered, authors) -> set:
    authorset = set()

    if authors:
        for row in filtered:
            authorset.add(row[2])
    
    return authorset



def main():
    arguments = get_parsed_arguments()
    filtered  = csv.reader(open('books.csv', 'r'))
    title_index = 0
    year_index = 1
    author_index = 2 

    if arguments.year1:
        filtered = filter_years(filtered, arguments.year1, arguments.year2)
    if arguments.books:
        filtered = filter_books(filtered, arguments.books)
    if arguments.authors:
        filtered = filter_authors(filtered, arguments.authors)

    authorset = get_authorset(filtered, arguments.authors)
    
    if authorset != set():
        for author in authorset:
            print(author)
            for row in list(filtered):
                if row[author_index] == author:
                    print('    ' + row[title_index] + ', ' + row[year_index])
    else:
        for row in filtered:
            print(row[title_index] + ', ' + row[year_index] + ', ' + row[author_index])

if __name__ == '__main__':
    main()







