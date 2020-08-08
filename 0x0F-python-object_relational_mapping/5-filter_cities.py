#!/bin/usr/python3
"""comidant"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    curse = db.cursor()
    curse.execute("SELECT cities.name FROM cites INNERJOIN\
    states ON cities.state_id = states.id WHERE states.name = '{}'\
    ORDER BY cities.id".format(argv[4]))
    cities = curse.fetchall()
    print(", ".join([row[0] for row in cities]))
    cur.close()
    db.close()
