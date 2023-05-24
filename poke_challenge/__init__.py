"""
    1. Get the types for each pokemon from API
    e.g. bulbasaur is grass and poison

    2. Store the data in SQLite3
    e.g.
    pokemon_name    |   type
    --------------------------
    bulbasaur       |   grass
    bulbasaur       |   poison
    charmander      |   fire

    3. Print all the rows

    4. Query the count of pokemon per type e.g.
    type      |   count
    -----------------------
    Fire      |   3
    Water     |   2
    Normal    |   4

    5. Save a json file in output with the result e.g.
    {
      "Fire": 3,
      "Water": 2,
      "Normal": 4
    }
"""


import sqlite3

import requests


async def main():
    conn = sqlite3.connect("./database.db")
    conn.executescript(
        """
    PRAGMA foreign_keys = ON;

    DROP TABLE IF EXISTS pokemon_types;

    CREATE TABLE pokemon_types (
        id              INTEGER PRIMARY KEY AUTOINCREMENT,
        pokemon_name    VARCHAR,
        pokemon_type    VARCHAR
    );
    """
    )

    # YOUR CODE GOES HERE
