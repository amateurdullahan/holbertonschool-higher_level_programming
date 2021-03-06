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
    curse = db.cursor()
    curse.execute("SELECT * FROM states ORDER BY states.id")
    states = curse.fetchall()
    for state in states:
        if state[1][0] == "N":
            print(state)
    curse.close()
    db.close()
