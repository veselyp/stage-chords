"""
appserver.py
- creates an application instance and runs the dev server
"""
from chords_api.application import create_app

if __name__ == '__main__':
    app = create_app()
    app.run()
