#!/usr/bin/python3
"""
Script 14-model_city_fetch_by_state.py that
prints all City objects from the database hbtn_0e_14_usa
"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker()
    session = Session(bind=engine)
    Base.metadata.create_all(engine)
    response = (session.query(State, City).filter(
        State.id == City.state_id).order_by(City.id).all())
    for state, city in response:
        print("{}: ({:d}) {}".format(state.name, city.id, city.name))
    session.close()
