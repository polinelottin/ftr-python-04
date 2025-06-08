from typing import Dict, Tuple
from flask import jsonify
from .http_unprocessable_entity import HttpUnprocessableEntity
from .http_bad_request import HttpBadRequest

def handle_error(error: Exception) -> Tuple[Dict, int]:
    if isinstance(error, (HttpUnprocessableEntity, HttpBadRequest)):
        return jsonify({
            "errors": [
                {
                    "title": error.name,
                    "detail": error.value
                }
            ]
        }), error.status_code

    return jsonify({
        "errors": [
            {
                "title": "Internal Server Error",
                "detail": str(error)
            }
        ]
    }), 500