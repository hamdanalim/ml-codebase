from flask_restful import Resource
from flask import jsonify, json


def make_error(status_code, sub_code, message, action):
    response = jsonify(
        {
            "status": status_code,
            "sub_code": sub_code,
            "message": message,
            "action": action,
        }
    )
    response.status_code = status_code
    return response