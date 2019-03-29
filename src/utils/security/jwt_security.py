# module that handles the securing of API using JSON Web Tokens
import jwt


def encode_jwt(alg='HS256', secret='', **payload):
    """
    Generate JWT authentication token
    :return: string
    """
    try:
        return jwt.encode(payload, secret, algorithm=alg)
    except Exception as e:
        return str(e)


def decode_jwt(encoded_jwt, secret, alg='HS256'):
    """
    Generate JWT authentication token
    :return: string
    """
    try:
        payload = jwt.decode(encoded_jwt, secret, algorithms=alg)
        return payload['payload']['sub']
    except Exception as e:
        return str(e)
