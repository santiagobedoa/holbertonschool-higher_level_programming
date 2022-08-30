#!/usr/bin/python3
"""List all states that matches the arg"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    if (len(argv) == 5):
        user = argv[1]
        password = argv[2]
        database = argv[3]
        argument = argv[4]
        config = {
            'user': user,
            'passwd': password,
            'host': 'localhost',
            'db': database,
            'port': 3306,
        }
        db = MySQLdb.connect(**config)

        with db.cursor() as cursor:
            """DON'T DO QUERY IN THIS FORM"""
            query = """
                SELECT * FROM states WHERE name
                LIKE '{:s}' ORDER BY id ASC""".format(argument)

            cursor.execute(query)

            data = cursor.fetchall()

        if not data:
            """
            print("Doesn't exist {0} state".format(argument))
            """
        else:
            [print(state) for state in data]

        db.close()

    else:
        """
        print("Usage: ./0-select_states.py username password database state")
        """
