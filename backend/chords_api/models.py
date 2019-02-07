"""
models.py
- Data classes for the surveyapi application
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(80), unique=True, nullable=False)

