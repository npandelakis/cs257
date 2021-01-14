'''
books.py
Written by Ross Grogan-Kaylor and Nick Pandelakis for cs257

python3 bookinfo.py -b substring # prints list of books whose titles contain substring
python3 bookinfo.py -a substring # prints list of authors whose names contain substring, and all books by each such author
python3 bookinfo.py year1 year2 # prints list of books published between min(year1, year2) and max(year1, year2)
'''

import csv
import argparse

# Interesting: "-b", "--book" vs. "b, --book": "-b", "--book" is the one you want (treats -b and --book as referring to the
# same argument); "-b, --book" treats -b and --book as referring to the same argument, but where -b can be specified with no args

def get_parsed_arguments():
    # Set up command line arguments.
    with open("prolog.txt", "r") as prolog, open("epilog.txt", "r") as epilog:
        parser = argparse.ArgumentParser(description = prolog.read(), epilog = epilog.read())

    parser.add_argument("bookscsv", metavar="bookscsv", help = "The .csv file storing the table of books and authors.")
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
    print(parsed_arguments)
    return parsed_arguments 



    # Read from CSV.
    # This code was taken from the first example in https://docs.python.org/3/library/csv.html#examples.
    # with open('books.csv', newline='') as f:
    #     reader = csv.reader(f)
    #     for row in reader:
    #         print(row)





def main():
    arguments = get_parsed_arguments()
    filtered = csv.reader(open(arguments.bookscsv, 'r'))
    authlist = set()


    # Save filtered as lists because the filter object can only be iterated over once.
    if arguments.year1:
        filtered = list(filter(lambda p: arguments.year1 <= p[1] and arguments.year2 >= p[1], filtered))

    if arguments.books:
        filtered = list(filter(lambda p: any(sub.lower() in p[0].lower() for sub in arguments.books), filtered))

    if arguments.authors:
        filtered = list(filter(lambda p: any(sub.lower() in p[2].lower() for sub in arguments.authors), filtered))
        for row in filtered:
            authlist.add(row[2])
        authlist = sorted(authlist)

    
    if authlist != set():
        for auth in authlist:
            print(auth)
            for row in list(filtered):
                if row[2] == auth:
                    print('    ' + row[0] + ', ' + row[1])
    else:
        for row in filtered:
            print(row[0] + ', ' + row[1] + ', ' + row[2])

if __name__ == '__main__':
    main()







