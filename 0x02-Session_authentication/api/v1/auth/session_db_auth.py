#!/usr/bin/env python3
""" Module for Session database authentication
"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
from datetime import datetime, timedelta
import os


class SessionDBAuth(SessionExpAuth):
    """ Class for Session Authentication using database, that inherits from
    SessionExpAuth.
    """

    def create_session(self, user_id=None):
        """ Create and store a new instance of UserSession.
        """
        if user_id:
            session_id = super().create_session(user_id)
            if session_id is None:
                return None

            user_session = UserSession(user_id=user_id, session_id=session_id)
            user_session.save()

            return session_id

    def user_id_for_session_id(self, session_id=None):
        """ Returns the User ID by requesting UserSession in the database
        based on session_id.
        """
        if session_id is None:
            return None

        try:
            user_sessions = UserSession.search({"session_id": session_id})

            for user_session in user_sessions:
                created_at = user_session.get('created_at', None)
                if not created_at:
                    return
                exp_time = created_at + \
                    timedelta(seconds=self.session_duration)
                if (datetime.now() > exp_time):
                    return
                return user_session.get('user_id', None)
        except Exception:
            return

    def destroy_session(self, request=None):
        """ Destroys the UserSession based on the Session ID from the request
        cookie.
        """
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        user_sessions = UserSession.search({"session_id": session_id})
        if not user_sessions:
            return False

        for user_session in user_sessions:
            user_session.remove()

        return True
