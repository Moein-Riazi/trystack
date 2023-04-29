from functools import wraps
from flask import request
from trystack.util import jsonify

def json_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if request.content_type != "application/json":
            return jsonify(
                status = 415,
                metadata = {
                    "message": "Content Type is not Supported"
                }  
            )
        else:
            return f(*args, **kwargs)
    return wrapper