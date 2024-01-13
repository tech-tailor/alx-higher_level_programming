#!/usr/bin/python3
""" This module to check database
"""


import sys
import MySQLdb


def list_state(user, password, database, state):
    """This function list a table
        from th database
    """

    db = MySQLdb.connect(
        user=user,
        password=password,
        database=database
        )
    cursor = db.cursor()

    myQuery = f"SELECT * FROM states WHERE BINARY name LIKE '{state}' ORDER BY id;"

    cursor.execute(myQuery)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    db.close()


if __name__ == "__main__":
    
    user, password, database, state = sys.argv[1:]
    list_state(user, password, database, state)
    
