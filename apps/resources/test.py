from flask import Flask, request
from flask_restful import Resource, reqparse
from flask import jsonify, json
from apps.error_handler.error import make_error


class NamePost(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "id",
        type=int,
        required=True,
    )
    parser.add_argument(
        "tv_program",
        type=str,
        required=True,
        help="tv_program cant be blank",
    )
    parser.add_argument(
        "is_multiscreen",
        type=str,
        required=True,
        help="is_multiscreen cant be blank",
    )

    def post(self):
        data = NamePost.parser.parse_args()

        id = data["id"]
        tv_program = data["tv_program"]
        is_multiscreen = data["is_multiscreen"]

        if not id:
            return make_error(400, 10, "id cant be blank", "cars")
        if not tv_program:
            return make_error(400, 10, "tv_program cant be blank", "cars")
        if not is_multiscreen:
            return make_error(400, 10, "is_multiscreen cant be blank", "cars")

        # return name
        if id != 4 or tv_program != "tvri":
            return make_error(400, 10, "error", "cars")
        else:
            return jsonify({"name": id, "code": 200, "message": "pesan"})
