# module that handles the securing of API resources using JSON Web Tokens
import jwt
from datetime import datetime, timedelta


def set_payload(subject_id):
    """
    Generate payload from subject id and datetime objects
    :param subject_id:
    :return: dictionary object
    """
    # set expiry time for token to be 2 hours from time of creation
    current_time = datetime.utcnow()
    expiry_time = current_time + timedelta(hours=24)  # add 2 hours to the current time

    payload = {
        "sub": subject_id,
        "iat": current_time.timestamp(),
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
    except Exception as e:
        return str(e)


def decode_jwt(encoded_jwt, secret='', alg='HS256'):
    """
    Decode JWT authentication token
    :return: int
    """
    try:
        payload = jwt.decode(encoded_jwt, secret, algorithms=alg)
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return "Signature expired. Please log in again."
    except jwt.InvalidTokenError:
        return "Invalid token. Please log in again."
