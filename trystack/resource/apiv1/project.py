from flask_restful import Resource

class ProjectResource(Resource):
    def get(self):
        return{"Fuck": "You",}