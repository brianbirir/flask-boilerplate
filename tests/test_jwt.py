import unittest
import os
import datetime
from pathlib import Path
from dotenv import load_dotenv
from src.utils.security.jwt_security import encode_jwt, decode_jwt


env_path = Path('..') / '.env'
load_dotenv(dotenv_path=env_path)

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

secret = os.getenv('SECRET')
algo = 'HS256'


class JwtTest(unittest.TestCase):

    def test_secret(self):
        self.assertTrue(isinstance(secret.encode(encoding='utf-8'), bytes))

    def test_jwt_encode(self):
        auth_token = encode_jwt(alg=algo, secret=secret, payload=payload)
        self.assertTrue(isinstance(auth_token, bytes))

    def test_jwt_decode(self):
        auth_token = encode_jwt(alg=algo, secret=secret, payload=payload_1)
        payload_result = decode_jwt(auth_token, secret, algo)
        self.assertEqual(payload_result, 2)


if __name__ == '__main__':
    unittest.main()
