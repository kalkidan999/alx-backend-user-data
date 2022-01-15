#!/usr/bin/env python3
"""
Auth Module
"""
from os import getenv
from typing import List, TypeVar
from flask import Flask, jsonify, abort, request, jsonify
from flask_cors import (CORS, cross_origin)
import os


class Auth():
    """Auth Class"""
    def require_auth(self, path: str, excluded_paths:
                     List[str]) -> bool:
        """ returns false - path and excluded_paths is used later
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        returns None - request will be the Flask request object
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        returns None - request will be the Flask request object
        """
        return None
