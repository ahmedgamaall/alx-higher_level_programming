#!/usr/bin/python3
"""a script that lists all cities from the database hbtn_0e_4_usa"""


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
    crsr.execute(""" SELECT
                    cities.id,
                    cities.name,
                    states.name
                    FROM
                    cities
                    JOIN
                    states
                    ON
                    cities.state_id = states.id
                    ORDER BY id ASC""")
    for r in crsr.fetchall():
        print(r)
    crsr.close()
    cnctn.close()
