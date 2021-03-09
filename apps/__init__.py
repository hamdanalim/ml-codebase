from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from config import config_by_name
from apps.routes.route import api_pathv1

db = SQLAlchemy()
app = Flask(__name__)


def create_app(env=None):

    app = Flask(__name__)
    app.config.from_object(config_by_name["dev"])

    app.register_blueprint(api_pathv1, url_prefix="/api/v1")

    return app
