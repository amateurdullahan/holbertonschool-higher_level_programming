#!/usr/bin/python3
"""comment"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_city import City


if __name__ == "__main__":
    diesel = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]))
    Base.metadata.create_all(diesel)
    Session = sessionmaker(bind=diesel)
    Session.configure(bind=diesel)
    jam = Session()
    for city, state in jam.query(City, State).join(State).order_by(City.id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    jam.close()
