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
        if path is None:
            return True

        if excluded_paths is None or not excluded_paths:
            return True

        if path.endswith('/'):
            path = path[:-1]

        for excluded_path in excluded_paths:
            if excluded_path.endswith('/'):
                excluded_path = excluded_path[:-1]

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
