from flask import Flask

from config import config
from src.extensions import db, jwt, migrate, ma
from src.views import api

def create_app(config_name="default", **kwargs) -> Flask:
    app = Flask(__name__, static_url_path="/static", static_folder="static")
    
    # load configurations object
    app.config.from_object(config[config_name])

    # database initialization
    # from web import models

    db.init_app(app)
    migrate.init_app(app, db)

    # initialize jwt
    jwt.init_app(app)

    # initialize flask-marshmallow
    ma.init_app(app)

    # initialize flask-restx
    api.init_app(app)

    return app
