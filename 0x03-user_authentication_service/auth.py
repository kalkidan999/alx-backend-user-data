#!/usr/bin/env python3
"""
Auth file
"""


from ast import Bytes
import email

import bcrypt
from flask import session
from sqlalchemy import null
from sqlalchemy.orm.exc import NoResultFound
from db import DB
from user import Base, User
import uuid


def _hash_password(password: str) -> str:
    """takes in a password string arguments
    and returns bytes"""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed


def _generate_uuid() -> str:
    """return a string representation of a new UUID"""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register User"""
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists.")
        except NoResultFound:
            hashed = _hash_password(password)
            newUser = self._db.add_user(email, hashed)
            return newUser

    def valid_login(self, email: str, password: str) -> str:
        """returns boolean track user by email and check
        password using bcrypt.checkpw"""
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode('utf-8'),
                                  user.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """return session ID as str"""
        try:
            new = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        session_id = _generate_uuid
        return session_id
