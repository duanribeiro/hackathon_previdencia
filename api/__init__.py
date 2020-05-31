from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS
from config import DevConfig

mongo = PyMongo()


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevConfig)
    mongo.init_app(app)

    from api.blueprints import v1_blueprint
    app.register_blueprint(v1_blueprint)

    CORS(app)
    return app
