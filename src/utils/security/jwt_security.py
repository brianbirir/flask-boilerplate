# module that handles the securing of API resources using JSON Web Tokens
import jwt
from datetime import datetime, timedelta


def set_payload(subject_id):
    """
    Generate payload from subject id and datetime objects
    :param subject_id:
    :return: dictionary object
    """
    # set expiry time for token to be 24 hours from time of creation
    expiry_time = datetime.utcnow() + timedelta(hours=24)

    payload = {
        "sub": subject_id,
        "iat": datetime.utcnow().timestamp(),
        "exp": expiry_time.timestamp()
    }
    return payload


def encode_jwt(subject_id='', secret='', alg='HS256'):
    """
    Generate JWT authentication token
    :return: string
    """
    try:
        return jwt.encode(set_payload(subject_id), secret, algorithm=alg)
    except jwt.ExpiredSignatureError:
        return "Token signature has expired. Please log in!"
    except Exception as e:
        return str(e)


def decode_jwt(encoded_jwt, secret='', alg='HS256'):
    """
    Generate JWT authentication token
    :return: int
    """
    try:
        payload = jwt.decode(encoded_jwt, secret, algorithms=alg)
        return payload['sub']
    except Exception as e:
        return str(e)
