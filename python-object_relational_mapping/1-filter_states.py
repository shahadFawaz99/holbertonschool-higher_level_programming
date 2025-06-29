#!/usr/bin/python3
"""
Lists all states with a name starting with N (uppercase) from the database
Usage: ./1-filter_states.py username password database_name
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

    # Query to select states where name starts with 'N', ordered by id
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;"
    cursor.execute(query)

    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
