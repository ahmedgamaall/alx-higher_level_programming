#!/usr/bin/python3
"""a script that lists all City objects
from the database hbtn_0e_101_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    eng = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                    sys.argv[2],
                                                    sys.argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    sess = Session()

    all = sess.query(City).order_by(City.id).all()
    for cts in all:
        print("{}: {} -> {}".format(cts.id, cts.name, cts.state.name))
    sess.close()
