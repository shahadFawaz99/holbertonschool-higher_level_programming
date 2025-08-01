#!/usr/bin/python3
"""
Script to fetch all City objects and display them with their State names
using SQLAlchemy ORM
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def main():
    """
    Connects to the database, queries all City objects with their State names,
    and prints them in the required format
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

    # Query all City objects with their associated State names,
    # ordered by city id
    cities = session.query(City, State).join(State).order_by(
        City.id
    ).all()

    # Print each city in the required format
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")

    # Close the session
    session.close()


if __name__ == "__main__":
    main()
