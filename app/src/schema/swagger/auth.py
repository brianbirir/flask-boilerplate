from marshmallow import fields

from src.views import api


# token generation request schema
token_generation_request = api.model(
    "TokenGenerationRequestSchema",
    {
        "email": fields.String(description="username of the user in the form of an email address"),
        "password": fields.String(description="password of the user"),
    },
)
