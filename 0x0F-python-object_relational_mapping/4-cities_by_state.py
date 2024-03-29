#!/usr/bin/python3
"""list all cities"""

from sys import argv
import MySQLdb


def cities_by_state():
    """ SQL INFO FROM ARGV """
    sql_usrname = argv[1]
    sql_password = argv[2]
    sql_database = argv[3]

    host = "localhost"
    port = 3306

    """ SETTING MySQLdb Connection """
    db_connection = MySQLdb.connect(
        port=port,
        host=host,
        user=sql_usrname,
        password=sql_password,
        database=sql_database)

    cur = db_connection.cursor()

    """ EXECUTING SQL QUERY"""
    cur.execute(
        """
        SELECT cities.id, cities.name, states.name FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
        """)

    """ FETCHING DATA """
    states = cur.fetchall()

    for state in states:
        print(state)

    db_connection.close()


if __name__ == '__main__':
    cities_by_state()
