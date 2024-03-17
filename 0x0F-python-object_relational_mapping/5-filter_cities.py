#!/usr/bin/python3
"""a script that takes in the name of a state as an
argument and lists all cities of that state, using
the database hbtn_0e_4_usa"""


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
    cmnd = """SELECT
                cities.name
                FROM
                cities
                JOIN
                states
                ON
                cities.state_id = states.id
                WHERE
                states.name LIKE '{:s}'
                ORDER BY cities.id ASC""".format(argv[4])
    crsr.execute(cmnd)
    city_ns = []
    for r in crsr.fetchall():
        city_ns.append(r[0])
    rsult = ", ".join(city_ns)
    print(rsult)
    crsr.close()
    cnctn.close()
