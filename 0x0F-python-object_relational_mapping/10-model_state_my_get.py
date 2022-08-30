#!/usr/bin/python3
"""list all objects from a database"""

from unicodedata import name
from sqlalchemy.orm import sessionmaker
from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == "__name__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}\
                            ".format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    state = session.query(State).filter_by(name=argv[4]).firs()
    if state is not None:
        print(str(state.id))
    else:
        print("Not found")
    session.close()
