from trystack.util import jsonify
from trystack.model import project
from flask import request

class ProjectController:
    def get_projects():
        print(request.content_type)
        #if request.content_type != "application/json":
        #    return jsonify(status=415)

    def get_project(project_id):
        return jsonify(status=501)

    def create_project():
        return jsonify(status=501)

    def update_project(project_id):
        return jsonify(status=501)

    def delete_project(project_id):
        return jsonify(status=501)