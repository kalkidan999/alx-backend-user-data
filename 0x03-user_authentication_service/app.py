#!/usr/bin/env python3
"""
Basic Flask app
"""


from flask import Flask, jsonify
from flask import request
app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def get_reuest():
    """get req"""
    data = jsonify(message='Bienvenue')
    return data


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
