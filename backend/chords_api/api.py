"""
api.py
- provides the API endpoints for consuming and producing
  REST requests and responses
"""

from flask import Blueprint, jsonify, request
from .models import db, Song, Playlist

api = Blueprint('api', __name__)


@api.route('/songs/')
def get_songs():
    try:
        songs = Song.query.all()
    except:
        return jsonify({'errors': 'No songs available'})
    return jsonify({'songs': [s.to_dict() for s in songs]})


@api.route('/songs/<int:id>', methods=('GET', 'PUT'))
def song(id):
    if request.method == 'GET':
        try:
            song = Song.query.get(id)
        except:
            return jsonify({'errors': 'No song available'})
        return jsonify({'song': song.to_dict()})
    elif request.method == 'PUT':
        data = request.get_json()
        song = Song.query.get(data['song'])
        db.session.commit()
        return jsonify(song.to_dict()), 201


@api.route('/playlists/', methods=('GET', 'PUT'))
def get_playlists():
    try:
        playlists = Playlist.query.all()
    except:
        return jsonify({'errors': 'No playlists available'})
    return jsonify({'songs': [s.to_dict() for s in playlists]})


@api.route('/playlists/<int:id>', methods=('GET', 'PUT'))
def playlist(id):
    if request.method == 'GET':
        try:
            playlist = Playlist.query.get(id)
        except:
            return jsonify({'errors': 'No playlist available'})
        return jsonify({'song': playlist.to_dict()})
    elif request.method == 'PUT':
        data = request.get_json()
        playlist = Song.query.get(data['playlist'])
        db.session.commit()
        return jsonify(playlist.to_dict()), 201

