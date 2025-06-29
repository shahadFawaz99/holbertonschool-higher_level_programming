#!/usr/bin/python3
"""
Prints the State id from the database hbtn_0e_6_usa based on state name
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def main():
    if len(sys.argv) != 5:
        return

    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Create engine to connect to the MySQL database
    engine = create_engine(f"mysql+mysqldb://{user}:{password}@localhost:3306/{database}")

    # Bind Base metadata to the engine
    Base.metadata.bind = engine

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query the State table for a state matching the state_name
    state = session.query(State).filter(State.name == state_name).first()

    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()

if __name__ == "__main__":
    main()
