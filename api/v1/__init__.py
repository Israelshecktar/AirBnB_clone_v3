#!/usr/bin/python3
"""This is the package initializer for the api/v1 module"""
from flask import Blueprint
from api.v1.views import index

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
