#!/usr/bin/python3
'''
lists all states with a name starting with N
from the database hbtn_0e_0_usa
'''
from sys import argv
import MySQLdb


if __name__ == '__main__':

    user = argv[1]
    passwd = argv[2]
    db = argv[3]

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
    sql = "SELECT * FROM states ORDER BY id ASC"
    cur.execute(sql)
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1][0] == 'N':
            print(row)
    cur.close()
    conn.close()
