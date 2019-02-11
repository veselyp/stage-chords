"""
    config.py
    - settings for the flask application object
"""


class BaseConfig(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///stage-chords.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
