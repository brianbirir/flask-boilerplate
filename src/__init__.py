import os
from flask import Flask
from dotenv import load_dotenv
from flask_migrate import Migrate
from flask_restful import Api
from src.model import db
from src.user import User
from src.auth import Login


def create_app(config_object='config.DevelopmentConfig'):
    """
    :param config_object:
    :return: app

    This factory returns the initialized Flask app

    """

    # load dot env
    app_root = os.path.join(os.path.dirname(__file__), '..')
    dot_env_path = os.path.join(app_root, '.env')
    load_dotenv(dot_env_path)

    # initialize Flask app
    app = Flask(__name__)
    app.config.from_object(config_object)  # load configurations object

    # database initialization
    db.init_app(app)
    migrate = Migrate(app, db)

    # resource routing
    api = Api(app)
    api.add_resource(User, '/api/user', '/api/user/<int:user_id>')  # user resource
    api.add_resource(Login, '/api/login')  # auth resource

    return app
