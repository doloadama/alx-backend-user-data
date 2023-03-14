#!/usr/bin/env python3
"""
0. User model
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class User(Base):
    """
    SQLAlchemy model named User
    for database table named users
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=True)
    hashed_password = Column(String(250), nullable=True)
    session = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
