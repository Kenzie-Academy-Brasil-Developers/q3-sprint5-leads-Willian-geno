from flask import Flask
from app.configs import database,migfration
from app.routes import init_app


def create_app():
    app = Flask(__name__)

    database.init_app(app)
    migfration.init_app(app)
    init_app(app)

    return app 
