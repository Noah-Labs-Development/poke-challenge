"""
    1. Get the pokemon names and types from API

    2. Store the data in SQLite3

    3. Query the count of pokemon per type e.g.
    type      |   count
    -----------------------
    Fire      |   3
    Water     |   2
    Normal    |   4

    4. Save a json file in output with the result e.g.
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
        type            VARCHAR
    );
    """
    )

    # YOUR CODE GOES HERE
