from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from config import config_by_name
from var_dump import var_dump

db = SQLAlchemy()


def create_app(env=None):

    app = Flask(__name__)
    app.config.from_object(config_by_name["dev"])

    api = Api(app)

    return app
