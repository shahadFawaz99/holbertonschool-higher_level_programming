#!/usr/bin/python3
"""
Module for defining State class using SQLAlchemy ORM
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create declarative base instance
Base = declarative_base()


class State(Base):
    """
    State class that represents the states table in the database
    """
    # Specify the table name
    __tablename__ = 'states'

    # Define id column: auto-generated, unique integer, primary key, not null
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # Define name column: string with max 128 characters, not null
    name = Column(String(128), nullable=False)
