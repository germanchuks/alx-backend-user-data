#!/usr/bin/env python3
"""Module to encrypt passwords"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Hashes a password using bcrypt."""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Checks if a provided password matches the hashed password."""
    return bcrypt.checkpw(password.encode(), hashed_password)
