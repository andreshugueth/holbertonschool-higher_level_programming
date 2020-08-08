#!/usr/bin/python3
'''
script that lists all cities
from the database hbtn_0e_4_usa
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
    sql = "SELECT cities.id, cities.name, states.name FROM states\
         INNER JOIN cities ON states.id=cities.state_id ORDER BY id ASC"
    cur.execute(sql)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
