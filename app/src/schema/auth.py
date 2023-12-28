from src.extensions import ma
from src.views import api


class TokenGenerationSchema(ma.Schema):
    email = ma.Email(required=True)
    password = ma.String(required=True)
