#!/usr/bin/env python3
""" Module for API authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Manages the API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Checks if authentication is required.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ Get the authorization header from a request.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Get current user.
        """
        return None
