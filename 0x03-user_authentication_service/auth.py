#!/usr/bin/env python3
""" Module for Authentication
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """ Hashes a string password and returns the salted hash.
    """
    hashed_pword = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_pword


def _generate_uuid():
    """ Returns a string representation of a new UUID.
    """
    return str(uuid.uuid4())


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

    def valid_login(self, email: str, password: str) -> bool:
        """ Validates user credentials.
        """
        try:
            user = self._db.find_user_by(email=email)
            if bcrypt.checkpw(password.encode('utf-8'), user.hashed_password):
                return True
        except Exception:
            return False
        return False

    def create_session(self, email: str) -> str:
        """ Generates new UUID and store as user session ID in the database.
        """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return
