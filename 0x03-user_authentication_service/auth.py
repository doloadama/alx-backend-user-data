#!/usr/bin/env python3
"""4.Hash password"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import bcrypt
from user import User
from sqlalchemy.orm.exc import NoResultFound


def __hash_password(password: str) -> bytes:
    """
    Takes in password string argument
    Returns bytes (salted_hashed)
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


from db import DB


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def resgister_user(self, email: str, password: str) -> User:
        """
        take mandatory email and password string arguments and 
        return a User object.
        If a user already exist with the passed email, raise a
        ValueError with the message User <user's email> already exists
        If not, hash the password with _hash_password, save the user to
        the database using self._db and return the User object.
        """
        try:
            self._db.query(User).filter(User.email == email).one()
            raise ValueError("User already exists")
        except NoResultFound:
            hashed_password = __hash_password(password)
            new_user = self._db.add_user(email, hashed_password)
            return new_user
