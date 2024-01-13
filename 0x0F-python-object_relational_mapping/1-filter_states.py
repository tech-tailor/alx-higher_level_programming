#!/usr/bin/python3
""" This module lists all state with a name
starting with N (upper N) from the 
database hbtn_0e_0_usa
"""


import sys
import MySQLdb


def list_state(user, password, database):
    """
    This function take user, password and database
    as args then print out list of states starting with
    N (upper N) from a 
    database.
    """

    db = MySQLdb.connect(
        user=user,
        password=password,
        database=database
        )
    cursor = db.cursor()

    myQuery = "SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id"

    cursor.execute(myQuery)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    db.close()


if __name__ == "__main__":
    user, password, database = sys.argv[1:4]
    list_state(user, password, database)
