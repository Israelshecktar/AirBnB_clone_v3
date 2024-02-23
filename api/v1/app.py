#!/usr/bin/python3
"""This is the module for the Flask application"""
from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_storage(exception):
    """Closes the storage on app exit"""
    storage.close()


if __name__ == "__main__":
    host = getenv("HBNB_API_HOST") or "0.0.0.0"
    port = getenv("HBNB_API_PORT") or "5000"
    app.run(host=host, port=port, threaded=True)
