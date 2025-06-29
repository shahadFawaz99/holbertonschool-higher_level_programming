#!/usr/bin/python3
"""
Module for filtering states by user input
"""

import MySQLdb
import sys


def main():
    """
    Main function to connect to database and filter states by name
    """
    if len(sys.argv) != 5:
        print("Usage: ./2-my_filter_states.py <username> <password> "
              "<database> <state_name>")
        sys.exit(1)

    try:
        connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3]
        )

        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM states WHERE name = '{}' ORDER BY id".format(
                sys.argv[4]
            )
        )

        for row in cursor.fetchall():
            print(row)

        cursor.close()
        connection.close()

    except MySQLdb.Error as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
