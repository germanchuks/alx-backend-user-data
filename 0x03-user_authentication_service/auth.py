#!/usr/bin/env python3
""" Module for Authentication
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """ Hashes a string password and returns the salted hash.
    """
    hashed_pword = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_pword


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Registers a new user.
        """
        try:
            is_existing_user = self._db.find_user_by(email=email)
            if is_existing_user:
                raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            new_user = self._db.add_user(email, hashed_password)
            return new_user
