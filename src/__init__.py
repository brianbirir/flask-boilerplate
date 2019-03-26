import os
from flask import Flask
from dotenv import load_dotenv


def create_app(config_object=''):

    # load dot env
    app_root = os.path.join(os.path.dirname(__file__), '..')
    dot_env_path = os.path.join(app_root, '.env')
    load_dotenv(dot_env_path)

    # database configs
    database_uri = os.getenv('DATABASE_URI')

    # initialize Flask app
    app = Flask(__name__)
    app.config.from_object(config_object)

    # home page route
    @app.route('/')
    def home():
        return 'Welcome home!'

    return app
