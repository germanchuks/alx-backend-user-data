#!/usr/bin/env python3
""" Module for Authentication
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """ Hashes a string password and returns the salted hash.
    """
    hashed_pword = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_pword
