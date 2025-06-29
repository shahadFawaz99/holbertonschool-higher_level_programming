#!/usr/bin/python3
"""Prints the State object with the name passed as argument from the database."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    # Create engine to connect to the MySQL database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Start a session
    session = Session(engine)

    # Safely query the State object matching the provided name
    state = session.query(State).filter(State.name == sys.argv[4]).first()

    # Print the result or Not found
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()
