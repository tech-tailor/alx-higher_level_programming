#!/usr/bin/python3
""" This module to check database
"""


import sys
import MySQLdb


def list_state(user, password, database, state):
    """This function list a table
        from th database
    """

    # connect to the database
    db = MySQLdb.connect(
        host='localhost',
        user=user,
        password=password,
        database=database
        )
    cursor = db.cursor()

    # join the state name to the cities using the state_id
    myQuery = f"""
    SELECT  c.name
    FROM cities c
    JOIN states s ON c.state_id = s.id
    WHERE s.name = '{state}'
    """
    cursor.execute(myQuery)

    rows = cursor.fetchall()

    query_list = []
    for row in rows:
        query_list.append(row[0])
    str_result = ', '.join(query_list)
    print(str_result)

    db.close()


# do not import the function, only run on the CLI
if __name__ == "__main__":
    user, password, database, state = sys.argv[1:5]
    list_state(user, password, database, state)
