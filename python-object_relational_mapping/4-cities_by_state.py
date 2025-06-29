#!/usr/bin/python3
"""
Module for listing all cities with their states
"""

import MySQLdb
import sys


def main():
    """
    Main function to connect to database and list all cities with states
    """
    # Validate 3 arguments
    if len(sys.argv) != 4:
        print("Usage: ./4-cities_by_state.py <username> <password> <database>")
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

        # Execute single JOIN query to get cities with their states
        mycursor.execute("""
            SELECT cities.id, cities.name, states.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            ORDER BY cities.id ASC
        """)

        # Display results
        for row in mycursor.fetchall():
            print(row)

        # Close cursor and connection
        mycursor.close()
        connection.close()

    except MySQLdb.Error as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
