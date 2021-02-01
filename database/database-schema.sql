-- Designed by Nick Pandelakis
CREATE TABLE athletes (
    id SERIAL,
    athlete_name text
);

CREATE TABLE teams (
    id SERIAL,
    team_name text
);

CREATE TABLE events (
    id SERIAL,
    event_name text
);


CREATE TABLE games (
    id SERIAL,
    games text,
    year integer,
    season text,
    city text
);


CREATE TABLE nocs (
    id SERIAL,
    noc text,
	noc_region text
);

CREATE TABLE results (
    id SERIAL,
    athlete_id integer,
    team_id integer,
    noc_id integer,
    games_id integer,
    sport_id integer,
    event_id integer,
    medal text
);


CREATE TABLE sports (
    id SERIAL,
    sport_name text
);

CREATE TABLE athlete_stats (
	athlete_id integer,
	games_id integer,
	sex text,
	age integer,
	height integer,
	weight decimal(5,1)
);
