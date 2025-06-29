#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    # Create engine using provided credentials
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )

    # Create session
    session = Session(engine)

    # Query all State objects, sorted by id
    for state in session.query(State).order_by(State.id).all():
        print(f"{state.id}: {state.name}")

    # Close session
    session.close()
