#!/usr/bin/python3
"""list all objects from a database"""

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
    new_state = State(name="Louisiana")
    session.add(new_state)
    state = session.query(State).filter_by(name="Louisiana").firs()
    print(str(state.id))
    session.commit()
    session.close()
