#!/usr/bin/python3
"""
Script to list all State objects from the database using SQLAlchemy ORM
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """
    Connects to the database, queries all State objects, and prints them sorted by id
    """
    # Create engine to connect to MySQL database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Create a configured "Session" class and a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects, ordered by id
    states = session.query(State).order_by(State.id).all()

    # Print each state in the required format
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()


if __name__ == "__main__":
    main()
