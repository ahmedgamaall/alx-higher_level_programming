#!/usr/bin/python3
"""a script that takes in an argument and displays all
values in the states table of hbtn_0e_0_usa where name
matches the argument"""


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
    cmnd = """SELECT *
                FROM states
                WHERE name LIKE '{:s}' ORDER BY id ASC""".format(argv[4])
    crsr.execute(cmnd)
    for r in crsr.fetchall():
        if r[1] == argv[4]:
            print(r)
    crsr.close()
    cnctn.close()
