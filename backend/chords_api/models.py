"""
models.py
- Data classes for the surveyapi application
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(80), unique=False, nullable=False)
    content = db.Column(db.String)
    duration = db.Column(db.Interval)


class PlaylistSong(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey('song.id'), nullable=False)
    order_no = db.Column(db.Integer)
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlist.id'))


class Playlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    song = db.relationship('PlaylistSong', backref='playlist', lazy=True)

