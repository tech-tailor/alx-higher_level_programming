#!/usr/bin/python3
""" This module to check database
"""


import sys
import MySQLdb


def list_state(user, password, database):
    """This function list a table
        from th database
    """

    # connect to the database
    db = MySQLdb.connect(
        user=user,
        password=password,
        database=database
        )
    cursor = db.cursor()

    # join the state name to the cities using the state_id
    myQuery = """
    SELECT c.id, c.name AS city_name, s.name AS state_name
    FROM cities c
    JOIN states s ON c.state_id = s.id;
    """
    cursor.execute(myQuery)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    db.close()


# do not import the function, only run on the CLI
if __name__ == "__main__":
    user, password, database = sys.argv[1:4]
    list_state(user, password, database)
