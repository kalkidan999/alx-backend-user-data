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
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path[-1] != '/':
            path += '/'

        for paths in excluded_paths:
            if paths.endswith('*'):
                if path.startswith(paths[:-1]):
                    return False
            elif path == paths:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        returns None - request will be the Flask request object
        """
        if request is None:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """
        returns None - request will be the Flask request object
        """
        return None
