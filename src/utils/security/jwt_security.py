# module that handles the securing of API resources using JSON Web Tokens
import jwt
from flask import current_app
from src import create_app

app = create_app()
app.app_context().push()
SECRET = current_app.config['SECRET_KEY']


def encode_jwt(alg='HS256', **payload):
    """
    Generate JWT authentication token
    :return: string
    """
    try:
        return jwt.encode(payload, SECRET, algorithm=alg)
    except Exception as e:
        return str(e)


def decode_jwt(encoded_jwt, alg='HS256'):
    """
    Generate JWT authentication token
    :return: string
    """
    try:
        payload = jwt.decode(encoded_jwt, SECRET, algorithms=alg)
        return payload['payload']['sub']
    except Exception as e:
        return str(e)
