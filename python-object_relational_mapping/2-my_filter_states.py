#!/usr/bin/python3
"""
Lists all values in the states table of a database where name
matches the argument.
"""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    cur = db.cursor()
    query = ("SELECT * FROM states "
             "WHERE CONVERT(`name` USING Latin1) COLLATE Latin1_General_CS = '{}' "
             "ORDER BY id ASC;").format(sys.argv[4])
    cur.execute(query)
    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    db.close()
