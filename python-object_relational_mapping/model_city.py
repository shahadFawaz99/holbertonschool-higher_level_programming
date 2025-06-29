#!/usr/bin/python3
"""
Module for defining City class using SQLAlchemy ORM
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base


class City(Base):
    """
    City class that represents the cities table in the database
    """
    # Specify the table name
    __tablename__ = 'cities'

    # Define id column: auto-generated, unique integer, primary key, not null
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # Define name column: string with max 128 characters, not null
    name = Column(String(128), nullable=False)

    # Define state_id column: integer, not null, foreign key to states.id
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
