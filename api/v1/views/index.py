#!/usr/bin/python3
"""This is the module for the /status endpoint"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def status():
    """Returns a JSON with the status of the API"""
    return jsonify({"status": "OK"})
