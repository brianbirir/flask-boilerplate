from flask_restx import Namespace, Resource
from flask_jwt_extended import jwt_required


ns_health = Namespace("healthz", description="Tests health of the RESTful API service")


@ns_health.route("/ping")
class Health(Resource):
    """Checks if RESTful API is up and running"""
    @ns_health.response(200, "RESTful API service is up and running")
    @jwt_required()
    def get(self):
        return {
            "message": "RESTful API service is up and running"
        }, 200
