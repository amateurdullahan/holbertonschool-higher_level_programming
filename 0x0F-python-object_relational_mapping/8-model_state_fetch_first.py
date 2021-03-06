#!/usr/bin/python3
"""comment"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    diesel = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]))
    Base.metadata.create_all(diesel)
    Session = sessionmaker(bind=diesel)
    jam = Session()
    states = jam.query(State).first()
    if states.id:
        print('{}: {}'.format(states.id, states.name))
    else:
        print("Nothing")
