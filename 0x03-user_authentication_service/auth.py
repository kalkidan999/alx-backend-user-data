#!/usr/bin/env python3
"""
Auth file
"""


from ast import Bytes

import bcrypt


def _hash_password(password: str) -> str:
    """takes in a password string arguments
    and returns bytes"""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed
