from datetime import timedelta

from flask import abort, request
from flask_restx import Namespace, Resource
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity,
    get_jwt,
)
from marshmallow import fields

from src.models import RevokedToken
from src.schema import TokenGenerationSchema

ns_token = Namespace("token", description="Token authorization endpoints")

token_generation_model = ns_token.model(
    "TokenGenerationRequestModel",
    {
        "email": fields.String(description="username of the user in the form of an email address"),
        "password": fields.String(description="password of the user"),
    },
)


@ns_token.route("/refresh")
class TokenRefresh(Resource):
    """Refreshes an access token

    a blocklisted refresh token will not be able to access this endpoint. Only
    refresh tokens access this route
    """

    @jwt_required(refresh=True)
    @ns_token.response(200, "Access token has been generated successfully after refresh")
    @ns_token.response(500, "Something went wrong")
    @ns_token.response(400, "No JWT identity provided")
    def post(self):
        current_user = get_jwt_identity()
        if not current_user:
            abort(400, "No JWT identity provided")
        access_token = create_access_token(
            identity=current_user, expires_delta=timedelta(days=1)
        )

        return (
            {
                "message": "Access token has been generated successfully after refresh",
                "access_token": access_token,
            },
            200,
        )


@ns_token.route("/revoke")
class RevokeToken(Resource):
    """Revoke both access and refresh token"""

    @jwt_required(verify_type=False)
    @ns_token.response(200, "Token has been revoked")
    @ns_token.response(500, "Something went wrong")
    @ns_token.response(400, "No JWT provided")
    def delete(self):
        # the access and refresh tokens need to be sent in the authorization header
        # hence this endpoint is called twice by sending the tokens separately
        token = get_jwt()

        if not token:
            abort(400, "No JWT provided")

        jti = token["jti"]
        token_type = token["type"]

        try:
            revoked_token_instance = RevokedToken(
                revoked_token=jti, token_type=token_type
            )
            revoked_token_instance.save_to_db()
            return {
                "message": f"{token_type.capitalize()} token has been revoked`"
            }, 200
        except Exception as e:
            return {"message": f"something went wrong: {str(e)}"}, 500


@ns_token.route("/generate")
class GenerateToken(Resource):
    """Token generation resource for user"""

    # @ns_token.expect(token_generation_model)
    @ns_token.response(200, "Token generated successfully")
    @ns_token.response(400, "Bad request")
    @ns_token.response(404, "Unable to generate token")
    @ns_token.doc(
        params={"email": "Email of logged in Farm Cloud dashboard user", "password": "User's password"}
    )
    def post(self):
        request_body = request.json
        schema = TokenGenerationSchema()
        validation_errors = schema.validate(request_body)

        if validation_errors:
            abort(400, str(validation_errors))

        email = request_body["email"]

        if not email:
            abort(400, "Missing email")

        access_token = create_access_token(
            identity=email, expires_delta=timedelta(days=1)
        )
        refresh_token = create_refresh_token(
            identity=email, expires_delta=timedelta(days=7)
        )
        return (
            {
                "message": f"Token generated for {email}",
                "access_token": access_token,
                "refresh_token": refresh_token,
                "email": email,
            },
            200,
        )
