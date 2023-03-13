#!/usr/bin/env python3
"""4.Hash password"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import bcrypt


def __hash_password(password: str) -> bytes:
    """
    Takes in password string argument
    Returns bytes (salted_hashed)
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
