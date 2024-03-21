#!/usr/bin/python3
"""a script that creates the State “California” with
the City “San Francisco” from the database hbtn_0e_100_usa."""

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

    n_state = State(name='California')
    n_city = City(name='San Francisco')
    n_state.cities.append(n_city)

    sess.add(n_state)
    sess.add(n_city)
    sess.commit()
    sess.close()
