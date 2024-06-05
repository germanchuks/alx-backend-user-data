#!/usr/bin/env python3
""" Module of Session Authentication views
"""
from flask import jsonify, request, abort
from api.v1.views import app_views
import os
from models.user import User
from api.v1.app import auth


@app_views.route('/auth_session/login', methods=['POST'],
                 strict_slashes=False)
def login() -> str:
    """ POST /api/v1/auth_session/login
    Handles user login with session authentication
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400

    users = User.search({"email": email})
    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    # Create session ID and set cookie
    from api.v1.app import auth
    session_id = auth.create_session(user.id)
    response = jsonify(user.to_json())
    response.set_cookie(
        os.getenv('SESSION_NAME', '_my_session_id'), session_id)

    return response


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def logout() -> str:
    """ POST /api/v1/auth_session/login
    Handles user logout with session authentication
    """
    if not auth.destroy_session(request):
        abort(404)

    return jsonify({}), 200
