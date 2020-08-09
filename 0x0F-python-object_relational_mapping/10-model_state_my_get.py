#!/usr/bin/python3
"""
script that prints the first State
object from the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    state_name = argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                           argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_filter = session.query(State).filter(
        State.name.like('%{}%'.format(state_name))).first()
    if not state_filter:
        print("Not found")
    else:
        print("{}".format(state_filter.id))
    session.close()
