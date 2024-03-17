#!/usr/bin/python3
"""a script that takes in arguments and displays all
values in the states table of hbtn_0e_0_usa where name
matches the argument. But this time, write one that is
safe from MySQL injections!"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    cnctn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        database=argv[3],
    )
    crsr = cnctn.cursor()
    param = argv[4]
    cmnd = """SELECT *
                FROM states
                WHERE name LIKE %s ORDER BY id ASC"""
    crsr.execute(cmnd, ('%' + param + '%',))
    for r in crsr.fetchall():
        print(r)
    crsr.close()
    cnctn.close()
