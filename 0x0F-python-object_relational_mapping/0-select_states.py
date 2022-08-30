#!/usr/bin/python3
"""List all states"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    if (len(argv) == 4):
        user = argv[1]
        password = argv[2]
        database = argv[3]
        config = {
            'user': user,
            'passwd': password,
            'host': 'localhost',
            'db': database,
            'port': 3306,
        }

        db = MySQLdb.connect(**config)
        cursor = db.cursor()

        query = "SELECT * FROM states ORDER BY id"
        cursor.execute(query)

        data = cursor.fetchall()
        db.close()
        [print(state) for state in data]
    else:
        print("Usage: ./0-select_states.py username password database")
