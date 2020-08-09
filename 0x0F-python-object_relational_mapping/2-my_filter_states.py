#!/usr/bin/python3
"""n states"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    search = argv[4]
    curse = db.cursor()
    curse.execute("SELECT * FROM states WHERE BINARY states.name\
    = '{}' ORDER BY states.id ASC".format(argv[4]))
    states = curse.fetchall()
    for state in states:
            print(state)
    curse.close()
    db.close()
