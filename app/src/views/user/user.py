from flask import abort, request
from flask_restx import Namespace, Resource
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity,
    get_jwt,
)


ns_user = Namespace("user", description="Users endpoints")


@ns_user.route("/users")
class Users(Resource):
    pass