#!/usr/bin/python3
'''
script that takes in the name of a state
as an argument and lists all cities of that state,
using the database hbtn_0e_4_usa
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
    sql = "SELECT cities.name FROM states\
         INNER JOIN cities ON states.id=cities.state_id\
             WHERE states.name LIKE BINARY %s ORDER BY cities.id ASC"
    cur.execute(sql, (state_name, ))
    query_rows = cur.fetchall()
    print(", ".join([row[0] for row in query_rows]))
    cur.close()
    conn.close()
