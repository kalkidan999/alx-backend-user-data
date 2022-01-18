#!/usr/bin/env python3
"""
Basic Flask app
"""


import email
from flask import Flask, jsonify
from flask import request

from auth import Auth
app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def get_reuest():
    """get req"""
    data = jsonify(message='Bienvenue')
    return data


@app.route('/', methods=['POST'], strict_slashes=False)
def users():
    """endpt to register users"""
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        new = Auth.register_user(email, password)
        if new is not None:
            data = jsonify({"email": new.email,
                            "message": "user created"})
            return data
    except ValueError:
        return jsonify({"message": "email already registered"
                        }), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
