'''
    book.py
    Ross Grogan-Kaylor and Nick Pandelakis
    January 2021

    Examples:
    python3 bookinfo.py -b substring # prints list of books whose titles contain substring
    python3 bookinfo.py -a substring # prints list of authors whose names contain substring, and all books by each such author
    python3 bookinfo.py year1 year2 # prints list of books published between min(year1, year2) and max(year1, year2)

    General:
    python3 bookinfo1.py [bookinfo2.py ... bookinfon.py] [-b substring] [-a substring] [year1 year2]

'''

import argparse

def get_parsed_arguments():
    parser = argparse.ArgumentParser(description='Prints various lists of books which satisfy given conditions from a given .csv file.')
    parser.add_argument('bookcsvs', metavar='bookcsv', nargs='+', help='one or more csv files of books to be searched through')
    parser.add_argument('--books', '-b', default='english', help='Specify to only return books whose titles contain the given string')
    parser.add_argument('--authors', '-a', default='english', help='Specify to only return authors whose names contain the given string, as well as the books they wrote')
    parsed_arguments = parser.parse_args()
    return parsed_arguments


if __name__ == '__main__':
    main()
