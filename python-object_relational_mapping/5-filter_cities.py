#!/usr/bin/python3
"""
Module for listing all cities of a given state (safe from SQL injection)
"""

import MySQLdb
import sys


def main():
    """
    Main function to connect to database and list all cities of a given state
    """
    # Validate 4 arguments
    if len(sys.argv) != 5:
        print("Usage: ./5-filter_cities.py <username> <password> "
              "<database> <state_name>")
        sys.exit(1)

    try:
        # Connect to MySQL database
        connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3]
        )

        # Create cursor for executing queries
        mycursor = connection.cursor()
        # Execute safe query using parameters to prevent SQL injection
        mycursor.execute(
            "SELECT cities.name FROM cities "
            "JOIN states ON cities.state_id = states.id "
            "WHERE states.name = %s "
            "ORDER BY cities.id ASC",
            (sys.argv[4],)
        )

        # Fetch all city names
        cities = [row[0] for row in mycursor.fetchall()]
        # Print cities separated by comma, or nothing if empty
        print(", ".join(cities))

        # Close cursor and connection
        mycursor.close()
        connection.close()

    except MySQLdb.Error as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
