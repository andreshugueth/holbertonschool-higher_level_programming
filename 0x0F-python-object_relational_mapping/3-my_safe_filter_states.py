#!/usr/bin/python3
'''
script that takes in arguments
and displays all values in the states table of hbtn_0e_0_usa
where name matches the argument
'''
from sys import argv
import MySQLdb


if __name__ == '__main__':

    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    state_name = argv[4]

    dbconnect = {
        'host': 'localhost',
        'port': 3306,
        'user': user,
        'passwd': passwd,
        'db': db,
        'charset': "utf8"
    }

    conn = MySQLdb.connect(**dbconnect)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY %s\
                ORDER BY states.id ASC", (state_name, ))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
