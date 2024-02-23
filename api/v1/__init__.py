#!/usr/bin/python3
"""This is the package initializer for the api/v1 module"""
from flask import Blueprint
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
from api.v1.views import index
