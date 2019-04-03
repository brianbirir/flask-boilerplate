import unittest
import os
import datetime
from flask import current_app
from src import create_app
from src.utils.security.jwt_security import encode_jwt, decode_jwt


# load app context to get secret key from config
app = create_app()
app.app_context().push()
SECRET = current_app.config['SECRET_KEY']

# set crypto algorithm type
algo = 'HS256'

# set expiry time for token to be 24 hours from time of creation
expiry_time = datetime.datetime.utcnow() + datetime.timedelta(hours=24)

payload = {
        "sub": 1,
        "iat": datetime.datetime.utcnow().timestamp(),
        "exp": expiry_time.timestamp()
    }

payload_1 = {
        "sub": 2,
        "iat": datetime.datetime.utcnow().timestamp(),
        "exp": expiry_time.timestamp()
    }


class JwtTest(unittest.TestCase):

    def test_secret(self):
        self.assertTrue(isinstance(SECRET.encode(encoding='utf-8'), bytes))

    def test_jwt_encode(self):
        auth_token = encode_jwt(alg=algo, payload=payload)
        self.assertTrue(isinstance(auth_token, bytes))

    def test_jwt_decode(self):
        auth_token = encode_jwt(alg=algo, payload=payload_1)
        payload_result = decode_jwt(auth_token, algo)
        self.assertEqual(payload_result, 2)


if __name__ == '__main__':
    unittest.main()
