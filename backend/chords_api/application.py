"""
application.py
- creates a Flask app instance and registers the database object
"""

from flask import Flask


def create_app(app_name='CHORDS_API'):
    app = Flask(app_name)
    app.config.from_object('chords_api.config.BaseConfig')

    from chords_api.api import api
    app.register_blueprint(api, url_prefix="/api")

    from chords_api.models import db
    db.init_app(app)

    return app
