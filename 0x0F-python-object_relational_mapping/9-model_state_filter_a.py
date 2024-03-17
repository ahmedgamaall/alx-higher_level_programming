#!/usr/bin/python3
"""a script that lists all State objects that contain the
letter a from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    eng = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                    sys.argv[2],
                                                    sys.argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    secc = Session()

    stts = secc.query(State).order_by(State.id).\
        filter(State.name.like('%a%')).all()
    for st in stts:
        print("{:d}: {:s}".format(st.id, st.name))
