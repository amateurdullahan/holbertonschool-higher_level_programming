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
    curse.execute("SELECT cities.id, cities.name, states.name\
                FROM cities INNER JOIN states ON cities.state_id = states.id\
                ORDER BY cities.id")
    cities = curse.fetchall()
    for city in cities:
        print(city)
    cur.close()
    db.close()
