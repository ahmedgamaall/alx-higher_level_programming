#!/usr/bin/python3
""" a script that lists all State objects, and corresponding
City objects, contained in the database hbtn_0e_101_usa."""

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

    allCt = sess.query(State.id, State.name, City.id, City.name)\
        .join(City).all()
    for ct in allCt:
        print("{:d}: ({:s}) >> {:d}: ({:s})"
              .format(ct[0], ct[1], ct[2], ct[3]))
    sess.close()
