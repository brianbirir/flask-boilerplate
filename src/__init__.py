from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from src.model import db
from src.user import User
from src.auth import Login, Logout


def create_app(config_object='config.DevelopmentConfig'):
    """
    :param config_object:
    :return: app

    This factory returns the initialized Flask app

    """

    # initialize Flask app
    app = Flask(__name__)
    app.config.from_object(config_object)  # load configurations object

    # database initialization
    db.init_app(app)
    migrate = Migrate(app, db)

    # resource routing
    api = Api(app)
    api.add_resource(User, '/api/user', '/api/user/<int:user_id>')  # user resource
    api.add_resource(Login, '/api/login')  # login resource
    api.add_resource(Logout, '/api/logout')  # logout resource

    return app
