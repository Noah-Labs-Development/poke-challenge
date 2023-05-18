DB_CONNECTION_STRING = "./database.db"


CREATE_TABLES_SQL = """
PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS pokemon_types;

CREATE TABLE pokemon_types (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    pokemon_name    VARCHAR,
    type            VARCHAR
);
"""

BASE_API_URL = "https://pokeapi.co/api/v2"


POKEMON_NAMES = [
    "bulbasaur",
    "pidgeot",
    "charizard",
    "pikachu",
    "psyduck",
    "sandslash",
    "wartortle",
    "vileplume",
    "arcanine",
    "dugtrio",
    "vileplume",
    "growlithe",
    "onix",
    "cloyster",
]
