#!/usr/bin/env python3
""" Module for Basic Authentication
"""
from flask import request
from typing import List, TypeVar


class BasicAuth:
    """ Basic Authentication class that inherits from Auth
    """

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """ Returns Base64 part of the Authorization header for Basic Auth"""
        if authorization_header is None or not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header.split(' ')[1]
