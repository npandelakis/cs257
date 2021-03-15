AUTHORS: Nick Pandelakis and Grace de Benedetti

DATA: the dataset is a collection of individual terrorist attacks that occurred between 1960 and 2018.
Each attack has specific data associated with it including location, summary, and other statistics.

[Go to this link: https://www.start.umd.edu/gtd/access/, click "download" then unfortunately you must
register for an account to access the data.]

FEATURES CURRENTLY WORKING:
- world map with data on total number of terrorist attacks in the country when mouse hover over country
    - world map button on every page to be taken to the world map
- dynamic coloring for world map based on terrorist attacks
- click on a country in the world map to be taken to that country's map
- country map with pins for each terrorist attack and their summaries when mouse hover over pin
- click on a pin in the country map to be taken to that attack's page with additional information
- search functionality: search for a country and see country map with attack pins
    - search suggestions as you type, works for country name as well as country code
- filter the world or country map by years
-breadcrumbs

Before running, set the appropriate values for your database setup into a file called config.py:
user = ''
password = ''
database = ''
