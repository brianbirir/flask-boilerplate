"""API Base"""
from flask_restx import Api
from flask_jwt_extended.exceptions import JWTExtendedException
from jwt.exceptions import PyJWTError

from src.views.auth.token import ns_token
from src.views.health.ping import ns_health


api = Api(
    title="Generic RESTful API Service",
    version="1.0",
    description="A generic RESTful API"
)

# add namespaces
api_prefix = '/api/v1/'
api.add_namespace(ns_token, path=f'{api_prefix}/auth/')
api.add_namespace(ns_health, path=f'{api_prefix}/health/')

@api.errorhandler
def default_error_handler(error):
    # default status code
    status_code = getattr(error, "status_code", 500)

    if isinstance(error, JWTExtendedException) or isinstance(error, PyJWTError):
        return {"message": str(error)}, 401
    else:
        return {"message": str(error)}, status_code