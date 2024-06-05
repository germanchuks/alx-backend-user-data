#!/usr/bin/env python3
""" Module for API authentication
"""
from flask import request
from typing import List, TypeVar
import os


class Auth:
    """ Manages the API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Checks if authentication is required.
        """
        if path is None:
            return True

        if excluded_paths is None or not excluded_paths:
            return True

        path = path.rstrip('/')

        for excluded_path in excluded_paths:
            if excluded_path.endswith('*'):
                if path.startswith(excluded_path.rstrip('*')):
                    return False
            else:
                excluded_path = excluded_path.rstrip('/')
                if path == excluded_path:
                    return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Get the authorization header from a request.
        """
        if request is None:
            return None

        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ Get current user.
        """
        return None

    def session_cookie(self, request=None):
        """ Returns a cookie value from a request.
        """
        if request is None:
            return None

        session_name = os.getenv('SESSION_NAME')
        if session_name is None:
            return None

        return request.cookies.get(session_name)
