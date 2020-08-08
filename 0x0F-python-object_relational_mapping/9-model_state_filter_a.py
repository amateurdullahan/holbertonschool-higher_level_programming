#!/usr/bin/python3
"""comment"""
from model_state import Base, State
from SQLAlchemy import create_engine
from SQLAlchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    diesel = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]))
    Base.metadata.create_all(diesel)
    Session = sessionmaker(bind=diesel)
    jam = Session()
    result = jam.query(State).filter(State.name.like('%a%'))
    for states in result:
        print('{}: {}'.format(states.id, states.name))
