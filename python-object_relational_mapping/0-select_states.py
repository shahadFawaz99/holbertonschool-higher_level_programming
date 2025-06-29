#!/usr/bin/python3
"""
Lists all states from the database passed as argument
Usage: ./0-select_states.py username password database_name
"""

import sys
import MySQLdb

def main():
    if len(sys.argv) != 4:
        return

    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=user, passwd=password, db=db_name)
    cursor = db.cursor()

    # Execute query to get all states sorted by id ascending
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all results and print them
    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
