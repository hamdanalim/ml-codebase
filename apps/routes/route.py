from flask import Blueprint
from flask_restful import Api
from apps.resources.test import NamePost

# from apps.resources.resource import class
api_pathv1 = Blueprint("api_path", __name__)
api = Api(api_pathv1, default_mediatype="application/json")
api.add_resource(NamePost, "/name")
# api.add_resource(Protected, "/protected")
