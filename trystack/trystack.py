from flask import Flask,Blueprint
from flask_restful import Api

from .config import Config


apiv1_bp = Blueprint(name = "apiv1_bp", import_name = __name__ , url_prefix= "/api/v1")
apiv1 = Api(apiv1_bp) 

from . import resource

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(apiv1_bp)
    return app