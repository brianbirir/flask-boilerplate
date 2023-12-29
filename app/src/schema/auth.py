from src.extensions import ma


class TokenGenerationSchema(ma.Schema):
    email = ma.Email(required=True)
    password = ma.String(required=True)
