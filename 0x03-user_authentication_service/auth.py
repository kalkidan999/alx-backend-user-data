#!/usr/bin/env python3
"""
Auth file
"""


from ast import Bytes
import email

import bcrypt
from sqlalchemy import null
from sqlalchemy.orm.exc import NoResultFound
from db import DB
from user import Base, User


def _hash_password(password: str) -> str:
    """takes in a password string arguments
    and returns bytes"""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed


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
