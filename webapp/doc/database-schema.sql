--Written by Grace de Benedetti and Nick Pandelakis

CREATE TABLE countries (
	id SERIAL,
	country_name text
);

CREATE TABLE provinces (
	id SERIAL,
	province_name text
);

CREATE TABLE cities (
	id SERIAL,
	city_name text
);

CREATE TABLE attack_types (
	id SERIAL,
	attack_type text
);

CREATE TABLE target_types (
	id SERIAL,
	target_type text
);

CREATE TABLE perpetrator (
	id SERIAL,
	perpetrator text
);

CREATE TABLE target_subtypes (
	id SERIAL,
	target_subtype text
);

CREATE TABLE weapon_types (
	id SERIAL,
	weapon_type text
);

CREATE TABLE weapon_subtypes (
	id SERIAL,
	weapon_subtype text
);

CREATE TABLE property_damage (
	id SERIAL,
	damage_extent
);

CREATE TABLE attacks (
	id SERIAL,
	year INTEGER,
	month INTEGER,
	day INTEGER,
	country_id INTEGER,
	province_id INTEGER,
	city_id INTEGER,
	latitute DECIMAL(),
	longtitude DECIMAL(),
	summary text,
	attack_type_id INTEGER,
	success INTEGER,
	suicide INTEGER,
	target_type_id INTEGER,
	target_subtype_id INTEGER,
	target text,
	perp_id INTEGER,
	motive text,
	weapon_type_id INTEGER,
	weapon_subtype_id INTEGER,
	weapon_detail text,
	number_killed INTEGER,
	number_wounded INTEGER,
	property_damage_id INTEGER
);

CREATE TABLE country_attacks_per_year (
	country_id INTEGER,
	year INTEGER,
	number_of_attacks INTEGER
);

CREATE TABLE province_attacks_per_year (
	province_id INTEGER,
	year INTEGER,
	number_of_attacks INTEGER
);




