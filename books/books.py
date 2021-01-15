'''
books.py
Written by Ross Grogan-Kaylor and Nick Pandelakis for cs257
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


def filterBooks(filtered, books) -> list:
    return list(filter(lambda p: any(sub.lower() in p[0].lower() for sub in books), filtered))


def filterAuthors(filtered, authors) -> list:
    return list(filter(lambda p: any(sub.lower() in p[2].lower() for sub in authors), filtered))


def filterYears(filtered, year1, year2) -> list:
    return list(filter(lambda p: year1 <= p[1] and year2 >= p[1], filtered))


def getAuthorSet(filtered, authors) -> set:
    authset = set()

    if authors:
        for row in filtered:
            authset.add(row[2])
    
    return authset



def main():
    arguments = get_parsed_arguments()
    filtered  = csv.reader(open('books.csv', 'r'))


    if arguments.year1:
        filtered = filterYears(filtered, arguments.year1, arguments.year2)
    if arguments.books:
        filtered = filterBooks(filtered, arguments.books)
    if arguments.authors:
        filtered = filterAuthors(filtered, arguments.authors)

    authset = getAuthorSet(filtered, arguments.authors)
    
    if authset != set():
        for auth in authset:
            print(auth)
            for row in list(filtered):
                if row[2] == auth:
                    print('    ' + row[0] + ', ' + row[1])
    else:
        for row in filtered:
            print(row[0] + ', ' + row[1] + ', ' + row[2])

if __name__ == '__main__':
    main()







