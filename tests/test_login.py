import unittest
import json
import requests
from flask_testing import TestCase
from flask import Flask
from flask_restful import Api
from src.auth import Login

class LoginTest(TestCase):

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True

        # resource routing
        api = Api(app)
        api.add_resource(Login, '/api/login')  # auth resource
        return app

    def test_successful_login(self):
        r = requests.post(
            'http://127.0.0.1:5000/api/login',
            data={"email":"test@gmail.com", "password":"1234567891"}
        )

        self.assert200(r)

    def test_wrong_credentials_login(self):
        r = requests.post(
            'http://127.0.0.1:5000/api/login',
            data={"email":"test@gmail.com", "password":"1234567"}
        )
        self.assert403(r)

    def test_non_existent_user_login(self):
        r = requests.post(
            'http://127.0.0.1:5000/api/login',
            data={"email":"test_another@gmail.com", "password":"1234567891"}
        )
        self.assert404(r)
    
if __name__ == '__main__':
    unittest.main()
