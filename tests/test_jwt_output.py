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
secret = os.getenv('SECRET')
algo = 'HS256'


class JwtTest:

    @staticmethod
    def test_secret():
        print(secret.encode(encoding='utf8'))

    @staticmethod
    def test_jwt_encode():
        auth_token = encode_jwt(alg=algo, secret=secret, payload=payload)
        print(auth_token)

    @staticmethod
    def test_jwt_decode():
        auth_token = encode_jwt(alg=algo, secret=secret, payload=payload)
        payload_result = decode_jwt(auth_token, secret, algo)
        print(payload_result)
        pass


if __name__ == '__main__':

    JwtTest.test_secret()
    JwtTest.test_jwt_encode()
    JwtTest.test_jwt_decode()
