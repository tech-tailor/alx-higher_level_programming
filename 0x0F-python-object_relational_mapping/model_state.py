#!/usr/bin/python3

from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """
    This class inherit from sqlalchemy decleative base class
    the class creates a table with different attributes
    """
    __tablename__ = 'states'
    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
        unique=True,
        autoincrement=True
    )
    name = Column(String(128), nullable=False)
