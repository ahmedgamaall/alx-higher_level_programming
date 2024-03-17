#!/usr/bin/python3
"""write a script 14-model_city_fetch_by_state.py that prints
all City objects from the database hbtn_0e_14_usa:"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    eng = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                    sys.argv[2],
                                                    sys.argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    secc = Session()

    cts = secc.query(State.name, City.id, City.name).\
        filter(State.id == City.state_id).order_by(City.id)
    for cty in cts:
        print("{:s}: ({:d}) {:s}".format(cty[0], cty[1], cty[2]))
    secc.close()
