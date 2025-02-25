from flask import Flask
from app.views.main import main
from app.views.auth import auth


def create_app():
    app=Flask(__name__)
    app.register_blueprint(main)
    app.register_blueprint(auth)
    return app