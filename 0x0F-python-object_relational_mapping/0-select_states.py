#!/usr/bin/python3
"""a script that lists all states from the database hbtn_0e_0_usa"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    cnctn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        database=argv[3]
    )
    crsr = cnctn.cursor()
    crsr.execute("SELECT * FROM states ORDER BY id ASC")
    for r in crsr.fetchall():
        print(r)
    crsr.close()
    cnctn.close()
