--
-- PostgreSQL database dump
--

-- Dumped from database version 13.1
-- Dumped by pg_dump version 13.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: attack_types; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.attack_types (
    id integer NOT NULL,
    attack_type text
);


--
-- Name: attack_types_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.attack_types_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: attack_types_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.attack_types_id_seq OWNED BY public.attack_types.id;


--
-- Name: attacks; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.attacks (
    id integer NOT NULL,
    year integer,
    month integer,
    day integer,
    country_id integer,
    province_id integer,
    city_id integer,
    latitute numeric,
    longtitude numeric,
    summary text,
    attack_type_id integer,
    success integer,
    suicide integer,
    target_type_id integer,
    target_subtype_id integer,
    target text,
    perp_id integer,
    motive text,
    weapon_type_id integer,
    weapon_subtype_id integer,
    weapon_detail text,
    number_killed integer,
    number_wounded integer,
    property_damage_id integer
);


--
-- Name: attacks_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.attacks_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: attacks_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.attacks_id_seq OWNED BY public.attacks.id;


--
-- Name: cities; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.cities (
    id integer NOT NULL,
    city_name text
);


--
-- Name: cities_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.cities_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: cities_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.cities_id_seq OWNED BY public.cities.id;


--
-- Name: countries; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.countries (
    id integer NOT NULL,
    country_name text
);


--
-- Name: countries_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.countries_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: countries_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.countries_id_seq OWNED BY public.countries.id;


--
-- Name: country_attacks_per_year; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.country_attacks_per_year (
    country_id integer,
    year integer,
    number_of_attacks integer
);


--
-- Name: perpetrator; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.perpetrator (
    id integer NOT NULL,
    perpetrator text
);


--
-- Name: perpetrator_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.perpetrator_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: perpetrator_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.perpetrator_id_seq OWNED BY public.perpetrator.id;


--
-- Name: property_damage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.property_damage (
    id integer NOT NULL,
    damage_extent text
);


--
-- Name: property_damage_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.property_damage_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: property_damage_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.property_damage_id_seq OWNED BY public.property_damage.id;


--
-- Name: province_attacks_per_year; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.province_attacks_per_year (
    province_id integer,
    year integer,
    number_of_attacks integer
);


--
-- Name: provinces; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.provinces (
    id integer NOT NULL,
    province_name text
);


--
-- Name: provinces_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.provinces_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: provinces_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.provinces_id_seq OWNED BY public.provinces.id;


--
-- Name: target_subtypes; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.target_subtypes (
    id integer NOT NULL,
    target_subtype text
);


--
-- Name: target_subtypes_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.target_subtypes_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: target_subtypes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.target_subtypes_id_seq OWNED BY public.target_subtypes.id;


--
-- Name: target_types; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.target_types (
    id integer NOT NULL,
    target_type text
);


--
-- Name: target_types_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.target_types_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: target_types_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.target_types_id_seq OWNED BY public.target_types.id;


--
-- Name: weapon_subtypes; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.weapon_subtypes (
    id integer NOT NULL,
    weapon_subtype text
);


--
-- Name: weapon_subtypes_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.weapon_subtypes_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: weapon_subtypes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.weapon_subtypes_id_seq OWNED BY public.weapon_subtypes.id;


--
-- Name: weapon_types; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.weapon_types (
    id integer NOT NULL,
    weapon_type text
);


--
-- Name: weapon_types_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.weapon_types_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: weapon_types_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.weapon_types_id_seq OWNED BY public.weapon_types.id;


--
-- Name: attack_types id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.attack_types ALTER COLUMN id SET DEFAULT nextval('public.attack_types_id_seq'::regclass);


--
-- Name: attacks id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.attacks ALTER COLUMN id SET DEFAULT nextval('public.attacks_id_seq'::regclass);


--
-- Name: cities id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.cities ALTER COLUMN id SET DEFAULT nextval('public.cities_id_seq'::regclass);


--
-- Name: countries id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.countries ALTER COLUMN id SET DEFAULT nextval('public.countries_id_seq'::regclass);


--
-- Name: perpetrator id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.perpetrator ALTER COLUMN id SET DEFAULT nextval('public.perpetrator_id_seq'::regclass);


--
-- Name: property_damage id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.property_damage ALTER COLUMN id SET DEFAULT nextval('public.property_damage_id_seq'::regclass);


--
-- Name: provinces id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.provinces ALTER COLUMN id SET DEFAULT nextval('public.provinces_id_seq'::regclass);


--
-- Name: target_subtypes id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.target_subtypes ALTER COLUMN id SET DEFAULT nextval('public.target_subtypes_id_seq'::regclass);


--
-- Name: target_types id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.target_types ALTER COLUMN id SET DEFAULT nextval('public.target_types_id_seq'::regclass);


--
-- Name: weapon_subtypes id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.weapon_subtypes ALTER COLUMN id SET DEFAULT nextval('public.weapon_subtypes_id_seq'::regclass);


--
-- Name: weapon_types id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.weapon_types ALTER COLUMN id SET DEFAULT nextval('public.weapon_types_id_seq'::regclass);


--
-- Data for Name: attack_types; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.attack_types (id, attack_type) FROM stdin;
\.


--
-- Data for Name: attacks; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.attacks (id, year, month, day, country_id, province_id, city_id, latitute, longtitude, summary, attack_type_id, success, suicide, target_type_id, target_subtype_id, target, perp_id, motive, weapon_type_id, weapon_subtype_id, weapon_detail, number_killed, number_wounded, property_damage_id) FROM stdin;
\.


--
-- Data for Name: cities; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.cities (id, city_name) FROM stdin;
\.


--
-- Data for Name: countries; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.countries (id, country_name) FROM stdin;
\.


--
-- Data for Name: country_attacks_per_year; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.country_attacks_per_year (country_id, year, number_of_attacks) FROM stdin;
\.


--
-- Data for Name: perpetrator; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.perpetrator (id, perpetrator) FROM stdin;
\.


--
-- Data for Name: property_damage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.property_damage (id, damage_extent) FROM stdin;
\.


--
-- Data for Name: province_attacks_per_year; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.province_attacks_per_year (province_id, year, number_of_attacks) FROM stdin;
\.


--
-- Data for Name: provinces; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.provinces (id, province_name) FROM stdin;
\.


--
-- Data for Name: target_subtypes; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.target_subtypes (id, target_subtype) FROM stdin;
\.


--
-- Data for Name: target_types; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.target_types (id, target_type) FROM stdin;
\.


--
-- Data for Name: weapon_subtypes; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.weapon_subtypes (id, weapon_subtype) FROM stdin;
\.


--
-- Data for Name: weapon_types; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.weapon_types (id, weapon_type) FROM stdin;
\.


--
-- Name: attack_types_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.attack_types_id_seq', 1, false);


--
-- Name: attacks_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.attacks_id_seq', 1, false);


--
-- Name: cities_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.cities_id_seq', 1, false);


--
-- Name: countries_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.countries_id_seq', 1, false);


--
-- Name: perpetrator_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.perpetrator_id_seq', 1, false);


--
-- Name: property_damage_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.property_damage_id_seq', 1, false);


--
-- Name: provinces_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.provinces_id_seq', 1, false);


--
-- Name: target_subtypes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.target_subtypes_id_seq', 1, false);


--
-- Name: target_types_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.target_types_id_seq', 1, false);


--
-- Name: weapon_subtypes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.weapon_subtypes_id_seq', 1, false);


--
-- Name: weapon_types_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.weapon_types_id_seq', 1, false);


--
-- PostgreSQL database dump complete
--

